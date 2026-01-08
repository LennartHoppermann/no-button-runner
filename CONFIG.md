# Valentine's Day Web App Configuration Guide 💕

This guide will help you set up the webhook notification system for your Valentine's Day web app.

## Quick Setup

1. **Choose a notification method** (pick one):
   - Webhook.site (easiest for testing)
   - Telegram Bot
   - Discord Webhook
   - Email via Zapier/IFTTT
   - Custom webhook endpoint

2. **Update the webhook URL** in `script.js`:
   - Open `script.js`
   - Replace `YOUR_WEBHOOK_URL_HERE` on line 2 with your actual webhook URL

3. **Customize restaurant details** in `restaurant.html`:
   - Update restaurant name, address, date/time
   - Replace Google Maps link with actual location
   - Replace restaurant website link

## Notification Setup Options

### Option 1: Webhook.site (Easiest - For Testing)
1. Go to https://webhook.site
2. Copy your unique URL
3. Paste it in `script.js` as the `WEBHOOK_URL`
4. You'll receive notifications on the webhook.site page

### Option 2: Telegram Bot
1. Create a bot with [@BotFather](https://t.me/botfather)
2. Get your bot token
3. Get your chat ID by messaging [@userinfobot](https://t.me/userinfobot)
4. Use URL format: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/sendMessage?chat_id=<YOUR_CHAT_ID>&text=`
5. Update `script.js` to send the message properly

### Option 3: Discord Webhook
1. Go to your Discord server settings
2. Navigate to Integrations → Webhooks
3. Create a new webhook
4. Copy the webhook URL
5. Paste it in `script.js` as the `WEBHOOK_URL`

### Option 4: Email via Zapier
1. Create a free Zapier account
2. Create a Zap with Webhook trigger
3. Add Email action
4. Copy the webhook URL
5. Paste it in `script.js` as the `WEBHOOK_URL`

## Deployment

### Option 1: GitHub Pages (Free & Easy)
1. Push your code to GitHub
2. Go to repository Settings → Pages
3. Select your branch and root folder
4. Your site will be live at `https://yourusername.github.io/repository-name/`

### Option 2: Netlify (Free & Easy)
1. Sign up at https://netlify.com
2. Drag and drop your folder or connect your GitHub repo
3. Your site will be live instantly

### Option 3: Vercel (Free & Easy)
1. Sign up at https://vercel.com
2. Import your GitHub repository
3. Deploy with one click

## Testing Locally

1. Open `index.html` in your web browser directly, or
2. Use a local server:
   ```bash
   # If you have Python 3:
   python -m http.server 8000
   
   # If you have Node.js:
   npx http-server
   ```
3. Open http://localhost:8000 in your browser

## Customization Tips

- **Colors**: Edit `style.css` to change the color scheme
- **Text**: Update the question and button labels in `index.html`
- **Restaurant Info**: Edit all details in `restaurant.html`
- **Emojis**: Feel free to add more emojis to make it more personal! 💕

## How It Works

1. When your Valentine hovers over the "No" button, it jumps to a random position
2. The button always stays within the visible screen area
3. When they click "Yes", a notification is sent to you via the configured webhook
4. They're then redirected to a page showing your restaurant reservation details

Enjoy your Valentine's Day! 💝
