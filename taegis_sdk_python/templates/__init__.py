"""Taegis SDK Templates."""

from pathlib import Path
from typing import Union

from taegis_sdk_python.config import get_config, write_config, write_to_config
from taegis_sdk_python.templates._jinja2 import load_jinja2_template_environment


def check_template_config_presets():
    """Template Config Presets."""
    config = get_config()

    if "templates" not in config:
        config.add_section("templates")

    if "path" not in config["templates"]:
        config["templates"]["jinja2"] = "."

    write_config(config)


def set_template_path(path: Union[Path, str]):
    """Set Jinja2 Template directory."""
    if isinstance(path, str):
        path = Path(path)

    if not path.exists():
        raise OSError(f"{path} does exist")

    if not path.is_dir():
        raise OSError(f"{path} is not a directory")

    write_to_config("templates", "jinja2", str(path))


check_template_config_presets()

__all__ = ["load_jinja2_template_environment"]
