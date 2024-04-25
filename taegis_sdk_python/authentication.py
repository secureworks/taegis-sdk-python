"""authentication.py

Authenication implementations for Taegis.
"""

import logging
import os
from getpass import getpass
from time import time
from typing import Any, Dict, Tuple, Union, Optional
import threading

from oauthlib.oauth2 import BackendApplicationClient
from requests import HTTPError, post
from requests_oauthlib import OAuth2Session
from taegis_sdk_python.config import get_config, write_to_config
from taegis_sdk_python.errors import (
    InvalidAuthenticationMethod,
    MissingAccessTokenError,
)
from taegis_sdk_python.tokens import get_token_exp

try:
    from simplejson import JSONDecodeError
except ImportError:  # pragma: no cover
    from json.decoder import JSONDecodeError

logger = logging.getLogger(__name__)

LOCK = threading.RLock()


def check_username(
    request_url: str, username: str
) -> Dict[str, Any]:  # pragma: no cover
    """Check if the user needs to login via password or sso.

    Parameters
    ----------
    request_url : str
        Taegis Environment URL
    username : str
        Username

    Returns
    -------
    Dict[str, Any]
        JSON response from username check
    """
    logger.debug("Checking login type for username...")
    username_endpoint = "/auth/username"

    response = post(
        f"{request_url}{username_endpoint}", json={"username": username}, timeout=300
    )
    logger.debug(response)

    return response.json()


def get_oauth_from_env(environment: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Retrieve CLIENT_ID and CLIENT_SECRET credentials from environment.

    Variables may be renamed:
        from taegis_sdk_python.config import write_to_config
        write_to_config("charlie", "CLIENT_ID", "CHARLIE_CLIENT_ID")

    Parameters
    ----------
    environment : str
        Taegis environment identifier

    Returns
    -------
    Tuple[Optional[str], Optional[str]]
        CLIENT_ID and CLIENT_SECRET
    """
    config = get_config()
    client_id_env_var = config.get(environment, "CLIENT_ID", fallback="CLIENT_ID")
    client_secret_env_var = config.get(
        environment, "CLIENT_SECRET", fallback="CLIENT_SECRET"
    )

    client_id = os.environ.get(client_id_env_var)
    client_secret = os.environ.get(client_secret_env_var)

    return client_id, client_secret


def get_token(environment: str, request_url: str) -> str:  # pragma: no cover
    """Retrieve an access token from Taegis.

    Parameters
    ----------
    environment : str
        Taegis environment identifier
    request_url : str
        Endpoint URL for Taegis environment

    Returns
    -------
    str
        access token
    """
    access_token = get_cached_token(environment)

    if not access_token:
        with LOCK:
            access_token = get_cached_token(environment)

            if not access_token:
                client_id, client_secret = get_oauth_from_env(environment)
                if client_id and client_secret:
                    access_token = get_token_by_oauth(
                        request_url, client_id, client_secret
                    )
                else:
                    username = input("Username: ")
                    response = check_username(request_url, username)

                    if response.get("login_type") == "username-password":
                        access_token = get_token_by_password_grant(
                            request_url, username
                        )
                    elif response.get("login_type") == "sso":
                        access_token = get_token_by_sso_device_code(request_url)
                    else:
                        raise InvalidAuthenticationMethod(
                            message="No known authentication method for user"
                        )

                write_to_config(environment, "access_token", access_token)

    return access_token


def get_cached_token(env: str) -> Union[str, None]:  # pragma: no cover
    """Get cached token from config file."""
    config = get_config()

    # check for token and expiry in config
    token = str(config.get(env, "access_token", fallback=""))
    if token and get_token_exp(token) >= int(time()) + 15:
        return token

    return None


def get_token_by_oauth(
    request_url: str, client_id: str, client_secret: str
) -> str:  # pragma: no cover
    # pragma: no cover
    """Get token based on CLIENT_ID and CLIENT_SECRET values.

    Parameters
    ----------
    request_url : str
        Endpoint URL for Taegis environment
    client_id : str
        Taegis CLIENT_ID
    client_secret : str
        Taegis CLIENT_SECRET

    Returns
    -------
    str
        Access token
    """
    auth_uri = "/auth/api/v2/auth/token"

    client = BackendApplicationClient(client_id=client_id)
    oauth_client = OAuth2Session(client=client)

    response = oauth_client.fetch_token(
        token_url=f"{request_url}{auth_uri}",
        client_id=client_id,
        client_secret=client_secret,
    )

    access_token = response.get("access_token")

    if not access_token:
        raise MissingAccessTokenError(
            message="Access token not found",
            comments=["Check client_id and client_secret credentials"],
        )

    return access_token


def get_token_by_password_grant(
    request_url: str,
    username: str,
    password: Optional[str] = None,
) -> str:  # pragma: no cover
    """Get an access token by username/password with mfa.

    Parameters
    ----------
    request_url : str
        Endpoint URL for Taegis environment
    username : str
        User to authenticate

    Returns
    -------
    str
        Access token

    Raises
    ------
    requests.HTTPError
        Any issue with retrieving token via HTTP
    """
    auth_uri = "/universal-auth/token"

    if not password:
        password = getpass("Password: ")

    response = post(
        f"{request_url}{auth_uri}",
        json={"username": username, "password": password, "grant_type": "password"},
        timeout=300,
    )

    if access_token := response.json().get("access_token"):
        return access_token

    try:
        mfa_token = response.json().get("mfa_token")
    except JSONDecodeError as exc:
        raise HTTPError(response.text, response=response) from exc

    if not mfa_token:
        raise HTTPError(response.text, response=response)

    mfa_input = input("MFA Token: ")

    response = post(
        f"{request_url}{auth_uri}",
        json={
            "mfa_token": mfa_token,
            "otp": mfa_input,
            "grant_type": "http://ctpx.secureworks.com/grant-type/mfa-otp",
        },
        timeout=300,
    )
    response.raise_for_status()
    try:
        access_token = response.json().get("access_token")
    except JSONDecodeError as exc:
        raise HTTPError(response.text, response=response) from exc

    if not access_token:
        raise MissingAccessTokenError(
            message="Access token not found",
            comments=["Check credentials and MFA input."],
            nested_exception=HTTPError(response.text, response=response),
        )

    return access_token


def get_token_by_sso_device_code(
    request_url: str,
) -> Union[str, None]:  # pragma: no cover
    """Get a user token via Device Code authorization.

    Parameters
    ----------
    request_url : str
        Base Environment URL

    Returns
    -------
    Union[str, None]
        Access Token
    """
    logger.debug("Trying by SSO device code auth url...")
    init_endpoint = "/universal-auth/device/code/auth"
    token_endpoint = "/universal-auth/device/code/token"

    response = post(f"{request_url}{init_endpoint}", timeout=300)

    try:
        device_code_flow = response.json()
    except JSONDecodeError as exc:
        raise HTTPError(response.text, response=response) from exc

    if device_code_flow.get("verification_uri_complete"):
        print(
            f"Copy URL into a browser: {device_code_flow.get('verification_uri_complete')}"
        )
    elif device_code_flow.get("verification_uri") and device_code_flow.get("user_code"):
        print(
            "Copy URL into a browser: "
            f"{device_code_flow.get('verification_uri')}"
            f"?user_code={device_code_flow.get('user_code')}"
        )
    else:
        logger.error(f"Cannot login via SSO:{response.text}...")
        return None

    response = post(
        f"{request_url}{token_endpoint}",
        json={
            "device_code": device_code_flow.get("device_code"),
            "interval": device_code_flow.get("interval"),
        },
        timeout=300,
    )
    response.raise_for_status()

    try:
        access_token = response.json().get("access_token")
    except JSONDecodeError as exc:
        raise HTTPError(response.text, response=response) from exc

    if not access_token:
        raise MissingAccessTokenError(
            message="Access token not found",
            comments=["Check credentials provided to SSO provider."],
            nested_exception=HTTPError(response.text, response=response),
        )

    return access_token
