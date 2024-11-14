import json
import os
from configparser import ConfigParser

from from_root import from_root


class Utils:
    @staticmethod
    def load_json(filepath):
        """
        Reads json file and convert it to dictionary.

        Args:
            filepath (filepath): a path to json file.
        """
        with open(str(filepath), "r") as file:
            return json.load(file)

    @staticmethod
    def get_localized_text(key: str) -> str:
        """Retrieve a localized string for a given key."""
        locale = os.getenv("LOCALE")
        translations = Utils.load_json(from_root('resources/i18n/locales.json'))
        return translations[locale][key]

