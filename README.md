# No Button Runner - Valentine's Day Web App 💝

A fun and interactive Valentine's Day web app that asks "Will you be my Valentine?" with a twist!

## Features

- **Interactive Landing Page**: Presents the question "Will you be my Valentine?" with Yes and No buttons
- **Dodging No Button**: The No button jumps to random positions when you try to hover over it, always staying within the visible screen
- **Notification System**: Sends you a notification (via webhook) when your Valentine clicks Yes
- **Restaurant Details Page**: After clicking Yes, shows a beautiful page with your restaurant reservation details

## Quick Start

1. **Configure your webhook**: Open `script.js` and replace `YOUR_WEBHOOK_URL_HERE` with your actual webhook URL
2. **Customize restaurant details**: Edit `restaurant.html` with your actual restaurant information
3. **Deploy**: Upload to GitHub Pages, Netlify, or any static hosting service

For detailed setup instructions, see [CONFIG.md](CONFIG.md).

## How It Works

1. Your Valentine sees the landing page with the question
2. When they try to hover over "No", it jumps away to a random position
3. When they click "Yes", you receive a notification instantly
4. They're redirected to a page showing your romantic dinner plans

## Files

- `index.html` - Main landing page with the question
- `restaurant.html` - Restaurant details page shown after Yes is clicked
- `style.css` - Beautiful Valentine's Day themed styling
- `script.js` - Interactive logic for button dodging and notifications
- `CONFIG.md` - Detailed configuration guide

## Live Demo

Simply open `index.html` in your browser or deploy to any static hosting service.

## Technologies

- Pure HTML, CSS, and JavaScript - no frameworks needed!
- Responsive design works on desktop and mobile
- Uses Fetch API for webhook notifications

Happy Valentine's Day! 💕
