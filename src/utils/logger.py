"""
Logging-Modul für History und Antworten
"""

import json
import os
from datetime import datetime
from pathlib import Path


class EventLogger:
    """Speichere Ereignisse und Antworten"""
    
    def __init__(self):
        self.log_dir = Path(__file__).parent.parent.parent / "data"
        self.log_dir.mkdir(exist_ok=True)
        self.log_file = self.log_dir / "history.json"
    
    def log_answer(self, answer):
        """Speichere die Antwort"""
        try:
            history = self._load_history()
            
            entry = {
                "timestamp": datetime.now().isoformat(),
                "answer": answer,
                "date": datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            }
            
            history.append(entry)
            
            with open(self.log_file, 'w', encoding='utf-8') as f:
                json.dump(history, f, ensure_ascii=False, indent=2)
            
            return True
        except Exception as e:
            print(f"Fehler beim Speichern der Antwort: {e}")
            return False
    
    def _load_history(self):
        """Lade bestehende History"""
        try:
            if self.log_file.exists():
                with open(self.log_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            print(f"Fehler beim Laden der History: {e}")
        
        return []
    
    def get_history(self):
        """Hole komplette History"""
        return self._load_history()


# Globale Logger-Instanz
logger = EventLogger()
