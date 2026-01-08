# Valentine’s Day Project: “Willst du mein Valentinstagsschatz sein?”

Eine kleine, interaktive Web-Oberfläche als Valentinstags-Überraschung: Meine Freundin bekommt eine simple Frage angezeigt, die sie nur mit **Ja** oder **Nein** beantworten kann. Der Twist: Sobald sie versucht, mit der Maus auf **Nein** zu gehen, „flieht“ der Button und springt zufällig an eine andere Stelle. Bei **Ja** wird sie auf eine zweite Seite weitergeleitet, auf der das Restaurant (und optional weitere Details) gelistet ist, in das wir gemeinsam gehen.

## Idee und Ziel
Dieses Projekt ist bewusst leichtgewichtig und spielerisch aufgebaut. Ziel ist ein kurzer, witziger Moment mit einem klaren Outcome:
- **Interaktion + Überraschung** (das „Nein“ ist absichtlich schwer zu klicken)
- **Ein eindeutiges “Ja” führt zur Auflösung** (Restaurant-Seite)

## Features
- **Startseite mit klarer Frage**: „Willst du mein Valentinstagsschatz sein?“
- **Zwei Call-to-Actions**:
  - **Ja**: führt zur Restaurant-Seite (Weiterleitung / Routing).
  - **Nein**: weicht der Maus aus, indem der Button bei Annäherung random die Position verändert.
- **Restaurant-Seite**:
  - Darstellung des Restaurants, z. B. Name, Adresse, Uhrzeit (optional), Link zur Website oder Google Maps.
  - Saubere, übersichtliche Darstellung als “Plan für den Abend”.

## UX-Logik: Wie der “Nein”-Button ausweicht
Der “Nein”-Button reagiert auf Mouse-Events (z. B. `mouseenter`, `mouseover` oder eine Distanzprüfung zur Cursor-Position). Sobald ein Trigger ausgelöst wird:
1. Es wird eine neue zufällige Position berechnet (z. B. innerhalb des Viewports).
2. Der Button wird dorthin verschoben (per `position: absolute` / `fixed` und aktualisierten `top/left` Werten).
3. Dabei wird sichergestellt, dass der Button nicht außerhalb des sichtbaren Bereichs landet (Viewport-Grenzen + Button-Abmessungen).

Optional (je nach Umsetzung):
- kleine Animation beim Springen (kurze Transition)
- wiederholte Neuberechnung, falls die neue Position zu nah am Cursor liegt

## Technik (Beispiel)
Das Projekt ist als klassische kleine Frontend-App umsetzbar, z. B. mit:
- **React / Next.js** oder **Vanilla HTML/CSS/JS**
- Styling: CSS / Tailwind / einfache Komponentenstruktur
- Routing: interne Routen (z. B. `/` und `/restaurant`) oder Redirect auf eine externe Restaurant-URL
