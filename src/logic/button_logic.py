"""
Logik für den ausweichenden "Nein"-Button
Der Button teleportiert sich innerhalb des Fensters, wenn sich die Maus nähert
"""

import random
import math
from src.utils.config import ESCAPE_DISTANCE


class ButtonLogic:
    def __init__(self):
        self.button = None
        self.root = None
        self.button_x = 0
        self.button_y = 0
        self.mouse_x = 0
        self.mouse_y = 0
        self.is_tracking = False
    
    def bind_button(self, button, root):
        """
        Binde die Ausweich-Logik an den Button
        """
        self.button = button
        self.root = root
        
        # Initiale Button-Position mit place() setzen
        self.button.place(x=0, y=0)
        
        # Fenster-Events für Mausverfolgung
        self.root.bind("<Motion>", self._on_mouse_motion)
        self.root.bind("<Enter>", self._on_mouse_enter)
        self.root.bind("<Leave>", self._on_mouse_leave)
    
    def _on_mouse_enter(self, event):
        """Tracking starten, wenn Maus ins Fenster kommt"""
        self.is_tracking = True
    
    def _on_mouse_leave(self, event):
        """Tracking stoppen, wenn Maus das Fenster verlässt"""
        self.is_tracking = False
    
    def _on_mouse_motion(self, event):
        """Wird ausgelöst, wenn die Maus sich bewegt"""
        if not self.is_tracking:
            return
        
        # Aktuelle Mausposition
        self.mouse_x = event.x
        self.mouse_y = event.y
        
        # Aktuelle Button-Position
        button_width = self.button.winfo_width()
        button_height = self.button.winfo_height()
        
        if button_width <= 1 or button_height <= 1:
            # Button hat noch keine Größe, kann nicht berechnet werden
            return
        
        # Button-Mitte
        button_center_x = self.button_x + button_width // 2
        button_center_y = self.button_y + button_height // 2
        
        # Abstand zwischen Maus und Button-Mitte
        distance = math.sqrt(
            (self.mouse_x - button_center_x) ** 2 + 
            (self.mouse_y - button_center_y) ** 2
        )
        
        # Wenn Maus zu nah kommt ODER Maus ist auf dem Button, sofort verschieben
        if distance < ESCAPE_DISTANCE or self._is_mouse_on_button():
            self._move_button()
    
    def _is_mouse_on_button(self):
        """Prüfe, ob die Maus auf dem Button ist"""
        button_width = self.button.winfo_width()
        button_height = self.button.winfo_height()
        
        mouse_on_x = self.button_x <= self.mouse_x <= self.button_x + button_width
        mouse_on_y = self.button_y <= self.mouse_y <= self.button_y + button_height
        
        return mouse_on_x and mouse_on_y
    
    def _move_button(self):
        """Verschiebe den Button an eine zufällige Position"""
        # Fenster-Dimensionen
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()
        
        # Button-Dimensionen
        button_width = self.button.winfo_width()
        button_height = self.button.winfo_height()
        
        # Sicherheitsabstand vom Fensterrand (in Pixeln)
        margin = 30
        
        # Zufällige Position berechnen (innerhalb des Fensters)
        max_x = max(margin, window_width - button_width - margin)
        max_y = max(margin, window_height - button_height - margin)
        
        new_x = random.randint(margin, int(max_x))
        new_y = random.randint(margin, int(max_y))
        
        # Stelle sicher, dass der neue Punkt nicht zu nah bei der Maus ist
        # (um zu verhindern, dass der Button sofort wieder springt)
        distance_to_mouse = math.sqrt(
            (new_x - self.mouse_x) ** 2 + 
            (new_y - self.mouse_y) ** 2
        )
        
        if distance_to_mouse < ESCAPE_DISTANCE * 2:
            # Versuche einen anderen Punkt zu finden
            for _ in range(5):  # Maximal 5 Versuche
                new_x = random.randint(margin, int(max_x))
                new_y = random.randint(margin, int(max_y))
                distance_to_mouse = math.sqrt(
                    (new_x - self.mouse_x) ** 2 + 
                    (new_y - self.mouse_y) ** 2
                )
                if distance_to_mouse >= ESCAPE_DISTANCE * 2:
                    break
        
        # Button verschieben
        self.button_x = new_x
        self.button_y = new_y
        self.button.place(x=new_x, y=new_y)

