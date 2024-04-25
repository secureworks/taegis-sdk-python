"""config.py

Taegis SDK Configuration management.
"""

from configparser import ConfigParser
from pathlib import Path
import threading
from filelock import FileLock

LOCK = threading.RLock()


def get_config_file() -> Path:
    """Return config file path and ensure config file exists.

    Returns
    -------
    Path
        Path object to config file.
    """
    config_dir = Path().home() / ".taegis_sdk_python"
    config_fp = config_dir / "config"
    config_dir.mkdir(mode=0o755, parents=True, exist_ok=True)
    config_fp.touch(exist_ok=True, mode=0o600)
    return config_fp


def get_config() -> ConfigParser:
    """Get configuration file contents.

    Returns
    -------
    ConfigParser
        Config object
    """
    config = ConfigParser()
    with get_config_file().open() as f:  # pylint: disable=invalid-name
        config.read_file(f)
    return config


def write_config(config: ConfigParser):
    """Write configuration file.

    Parameters
    ----------
    config : ConfigParser
        Config object
    """
    config_fp = get_config_file()
    lock_file = config_fp.with_suffix(".lock")
    file_lock = FileLock(lock_file)

    with file_lock:
        with config_fp.open(mode="w") as f:  # pylint: disable=invalid-name
            config.write(f)

    lock_file.unlink(missing_ok=True)


def write_to_config(section: str, key: str, value: str):
    """Write a key/value pair to config file under section.

    Parameters
    ----------
    section : str
        Section name
    key : str
        Key
    value : str
        Value
    """
    config = get_config()

    if not config.has_section(section):
        config.add_section(section)

    config[section][key] = value

    write_config(config)
