"""
Konfetti-Animation Modul
"""

import tkinter as tk
import random
from threading import Thread
import time


class ConfettiAnimation:
    """Zeige Konfetti-Animation"""
    
    def __init__(self, root, duration=3, color="#d63384"):
        self.root = root
        self.duration = duration
        self.color = color
        self.canvas = None
        self.particles = []
        self.is_running = False
        self.stop_event = None
    
    def start(self):
        """Starte die Konfetti-Animation"""
        if self.is_running:
            return
        
        self.is_running = True
        self.stop_event = False
        
        # Canvas für Animation erstellen
        self.canvas = tk.Canvas(
            self.root,
            bg=self.root.cget("bg"),
            highlightthickness=0,
            width=self.root.winfo_width(),
            height=self.root.winfo_height()
        )
        self.canvas.place(x=0, y=0)
        
        # Starte Animation in separatem Thread
        animation_thread = Thread(target=self._animate, daemon=True)
        animation_thread.start()
    
    def stop(self):
        """Stoppe die Animation gracefully"""
        self.stop_event = True
        self.is_running = False
        try:
            if self.canvas:
                self.canvas.destroy()
        except:
            pass
    
    def _animate(self):
        """Animiere das Konfetti"""
        # Erstelle Partikel
        for _ in range(50):
            x = random.randint(0, self.root.winfo_width())
            y = random.randint(-50, 0)
            vx = random.uniform(-3, 3)
            vy = random.uniform(2, 5)
            size = random.randint(3, 8)
            
            color = random.choice([
                self.color, 
                "#a0325f",
                "#d63384",
                "#2d6a4f",
                "#a4161a"
            ])
            
            self.particles.append({
                "id": self.canvas.create_oval(x, y, x+size, y+size, fill=color, outline=""),
                "x": x,
                "y": y,
                "vx": vx,
                "vy": vy,
                "rotation": 0
            })
        
        # Animiere Partikel
        start_time = time.time()
        while time.time() - start_time < self.duration and self.is_running and not self.stop_event:
            for particle in self.particles:
                # Update Position
                particle["x"] += particle["vx"]
                particle["y"] += particle["vy"]
                particle["vy"] += 0.1  # Gravitation
                particle["rotation"] += random.uniform(-5, 5)
                
                # Move Canvas Item (nur wenn Canvas noch existiert)
                try:
                    self.canvas.coords(
                        particle["id"],
                        particle["x"],
                        particle["y"],
                        particle["x"] + 5,
                        particle["y"] + 5
                    )
                except Exception:
                    pass  # Canvas wurde zerstört, ignorieren
            
            try:
                self.root.update()
            except Exception:
                break
            time.sleep(0.02)
        
        # Cleanup (nur wenn nicht bereits zerstört)
        if not self.stop_event:
            try:
                if self.canvas:
                    self.canvas.destroy()
            except:
                pass
        
        self.is_running = False
        self.particles = []
