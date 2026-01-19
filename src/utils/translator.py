"""
Mehrsprachigkeits-Modul (i18n)
"""

from src.utils.config import CONFIG, CURRENT_LANGUAGE


class Translator:
    """Klasse für Übersetzungen"""
    
    def __init__(self, language=None):
        self.language = language or CURRENT_LANGUAGE
        self.messages = CONFIG.get("messages", {})
    
    def get(self, key, default=""):
        """Hole Übersetzung"""
        if self.language in self.messages:
            return self.messages[self.language].get(key, default)
        return default
    
    def set_language(self, language):
        """Wechsle Sprache"""
        self.language = language


# Globale Translator-Instanz
translator = Translator()
