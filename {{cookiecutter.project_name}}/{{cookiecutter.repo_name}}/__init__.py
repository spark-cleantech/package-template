"""{{ cookiecutter.project_short_description }}."""

# Copyright  {{ cookiecutter.copyright_year }} (C) Spark Cleantech SAS (SIREN 909736068) - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential

try:
    # NOTE: the `version.py` file must not be present in the git repository
    #   as it is generated by setuptools at install time
    from .version import __version__
except ImportError:  # pragma: no cover
    # Local copy or not installed with setuptools
    __version__ = "999"

__all__ = ["__version__"]