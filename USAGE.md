# 📋 Anleitung - Valentine's Day Programm

## 🎯 Features

✨ **Implementierte Features:**
- ✅ Ausweichender "Nein"-Button (unmöglich zu klicken)
- ✅ **Konfetti-Animation** beim Ja-klick
- ✅ **Sound-Effekte** für Interaktionen
- ✅ **JSON-Konfiguration** (restaurant_config.json) - einfach editierbar
- ✅ **Mehrsprachigkeit** (Deutsch/Englisch)
- ✅ **Event-Logging** (Antworten werden gespeichert in `data/history.json`)
- ✅ **Easter Eggs** (Konami-Code: ↑↑↓↓←→←→BA)
- ✅ **Dark Mode** Basis-Vorbereitung
- ✅ **Modernes Design** (elegant, minimalistisch)

---

## 🚀 Verwendung

### Start
```powershell
# Einfach die BAT-Datei doppelklicken
start.bat

# Oder manuell:
python run.py
```

### Restaurant-Daten anpassen
Öffne `restaurant_config.json` und bearbeite:
```json
{
  "restaurant": {
    "name": "Dein Restaurant",
    "address": "Deine Adresse",
    "time": "Deine Uhrzeit",
    "phone": "Deine Telefonnummer",
    "website": "https://example.com",
    "google_maps": "https://maps.google.com"
  }
}
```

### Sprache wechseln
In `restaurant_config.json` ändere:
```json
"language": "de"    // Deutsch
"language": "en"    // Englisch
```

### Eigene Nachrichten hinzufügen
Bearbeite die `messages` in `restaurant_config.json`

---

## 🎮 Easter Eggs

**Konami-Code:** Drücke nacheinander: `↑ ↑ ↓ ↓ ← → ← → B A`
- Zeigt eine geheime Nachricht an

---

## 📊 Antwort-History

Die Antworten werden automatisch in `data/history.json` gespeichert:
```json
[
  {
    "timestamp": "2026-01-17T...",
    "answer": "Ja",
    "date": "17.01.2026 14:30:00"
  }
]
```

---

## 📦 Executable erstellen (.exe)

### Installation
```powershell
pip install pyinstaller
```

### Build
```powershell
python build_executable.py
```

Die `.exe` wird in `dist/Valentine.exe` erstellt!

---

## 📂 Projekt-Struktur

```
no-button-runner/
├── src/
│   ├── main.py              # Einstiegspunkt
│   ├── ui/
│   │   ├── main_window.py   # Startfenster
│   │   ├── restaurant_window.py
│   │   ├── confetti.py      # Konfetti-Animation
│   │   ├── easter_eggs.py   # Easter Eggs
│   │   └── ui_utils.py      # UI-Helfer
│   ├── logic/
│   │   └── button_logic.py  # Nein-Button Logik
│   └── utils/
│       ├── config.py        # Konfiguration
│       ├── audio.py         # Sound-Effekte
│       ├── logger.py        # Event-Logging
│       └── translator.py    # Mehrsprachigkeit
├── data/                    # Speicherort für history.json
├── restaurant_config.json   # Konfigurationsdatei
├── run.py                   # Start-Skript
├── start.bat                # Windows-Shortcut
└── requirements.txt
```

---

## ⚙️ Konfiguration

### `restaurant_config.json`
```json
{
  "restaurant": {...},      // Restaurant-Daten
  "messages": {             // Übersetzungen
    "de": {...},
    "en": {...}
  },
  "theme": "light",         // light oder dark
  "language": "de"          // de oder en
}
```

---

## 🐛 Troubleshooting

**Problem:** Programm öffnet sich nicht
- Python 3.12+ installiert? `python --version`
- Im korrekten Ordner? `cd no-button-runner`

**Problem:** Button reagiert zu langsam
- `ESCAPE_DISTANCE` in `src/utils/config.py` erhöhen

**Problem:** Keine Sounds gehört
- Windows-Sounds aktiviert?
- Volume-Einstellung prüfen

---

## 🎨 Design anpassen

Farben ändern in `src/utils/config.py`:
```python
COLORS = {
    "primary": "#d63384",      # Dein Farbe
    "success": "#2d6a4f",
    # ... etc
}
```

---

## 📝 Lizenz

Privates Projekt - mit ❤️ gemacht

---

**Viel Spaß mit der Überraschung!** 💕
