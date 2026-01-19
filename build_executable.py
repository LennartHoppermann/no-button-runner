"""
PyInstaller Build-Skript
Erstellt eine Windows .exe aus dem Python-Programm
"""

import PyInstaller.__main__
import os
import sys
from pathlib import Path


def build_executable():
    """Baue das Programm zu .exe"""
    
    project_root = Path(__file__).parent
    output_dir = project_root / "dist"
    
    print("🔨 Baue Valentine's Day Programm...")
    print(f"📁 Projekt: {project_root}")
    
    PyInstaller.__main__.run([
        'run.py',
        '--onefile',                    # Einzelne .exe Datei
        '--windowed',                   # Keine Console
        '--name=Valentine',             # Name der .exe
        '--icon=assets/heart.ico',      # Icon (optional)
        f'--distpath={output_dir}',
        f'--buildpath={project_root / "build"}',
        f'--specpath={project_root / "build"}',
        '--add-data=restaurant_config.json:.',
        '--add-data=src:src',
    ])
    
    print(f"\n✅ Fertig! Die .exe befindet sich in: {output_dir}")
    print(f"📍 Pfad: {output_dir / 'Valentine.exe'}")


if __name__ == "__main__":
    # Prüfe ob PyInstaller installiert ist
    try:
        build_executable()
    except ImportError:
        print("❌ PyInstaller ist nicht installiert!")
        print("Installiere es mit: pip install pyinstaller")
        sys.exit(1)
