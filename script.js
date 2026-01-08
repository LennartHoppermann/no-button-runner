// Configuration for webhook notification
const WEBHOOK_URL = 'YOUR_WEBHOOK_URL_HERE'; // Replace with your actual webhook URL (Telegram, Discord, Zapier, etc.)

// Get button elements
const yesBtn = document.getElementById('yes-btn');
const noBtn = document.getElementById('no-btn');

// Function to make the No button jump to a random position within the viewport
function moveNoButton() {
    // Get viewport dimensions
    const viewportWidth = window.innerWidth;
    const viewportHeight = window.innerHeight;
    
    // Get button dimensions
    const btnWidth = noBtn.offsetWidth;
    const btnHeight = noBtn.offsetHeight;
    
    // Calculate maximum positions to keep button fully visible
    const maxX = viewportWidth - btnWidth - 20; // 20px padding from edge
    const maxY = viewportHeight - btnHeight - 20;
    
    // Generate random positions (minimum 20px from edges)
    const randomX = Math.random() * (maxX - 20) + 20;
    const randomY = Math.random() * (maxY - 20) + 20;
    
    // Set the button to fixed position
    noBtn.style.position = 'fixed';
    noBtn.style.left = randomX + 'px';
    noBtn.style.top = randomY + 'px';
    noBtn.style.transform = 'none';
}

// Add mouseover event to No button
noBtn.addEventListener('mouseover', moveNoButton);

// Add mouseenter event as backup (for faster detection)
noBtn.addEventListener('mouseenter', moveNoButton);

// Handle Yes button click
yesBtn.addEventListener('click', async function() {
    // Disable button to prevent multiple clicks
    yesBtn.disabled = true;
    yesBtn.textContent = 'Sending... 💌';
    
    try {
        // Send notification via webhook
        if (WEBHOOK_URL && WEBHOOK_URL !== 'YOUR_WEBHOOK_URL_HERE') {
            await fetch(WEBHOOK_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    message: '💕 She said YES! Your Valentine accepted! 💕',
                    timestamp: new Date().toISOString()
                })
            }).catch(err => {
                console.log('Notification error (non-blocking):', err);
                // Continue even if webhook fails
            });
        }
        
        // Wait a moment for the webhook to send
        await new Promise(resolve => setTimeout(resolve, 500));
        
        // Redirect to restaurant page
        window.location.href = 'restaurant.html';
    } catch (error) {
        console.error('Error:', error);
        // Redirect anyway even if notification fails
        window.location.href = 'restaurant.html';
    }
});

// Optional: Add click event to No button for fun (it will just jump away)
noBtn.addEventListener('click', function(e) {
    e.preventDefault();
    moveNoButton();
});
