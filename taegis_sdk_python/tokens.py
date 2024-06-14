"""JSON Web Token utilities."""

from typing import Any, Dict

import jwt


def decode_token_claims(access_token: str) -> Dict[str, Any]:
    """Decode and parse JWT claims.

    Parameters
    ----------
    access_token : str
        Access token

    Returns
    -------
    Dict[str, Any]
        JWT Claims as a Dictionary
    """
    return jwt.decode(access_token, options={"verify_signature": False})


def get_token_exp(access_token: str) -> int:
    """Get Token expiration from claims.

    Parameters
    ----------
    access_token : str
        Access token

    Returns
    -------
    int
        Token expiration timestamp
    """

    return decode_token_claims(access_token).get("exp", 0)


def get_token_tenant_id(access_token: str) -> str:
    """Get the user base tenant id from access token.

    Returns
    -------
    str
        Tenant ID
    """

    return decode_token_claims(access_token).get(
        "https://missione/octolabs/io/tenantIds"
    )
