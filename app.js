// Custom JavaScript functionality
function updateProgress(elementId, value) {
    document.getElementById(elementId).style.width = value + '%';
}

// Add click effects
document.addEventListener('DOMContentLoaded', function() {
    // Add ripple effect to cards
    const cards = document.querySelectorAll('.glass-card');
    cards.forEach(card => {
        card.addEventListener('click', function(e) {
            const ripple = document.createElement('span');
            const rect = card.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;
            
            ripple.style.cssText = `
                position: absolute;
                width: ${size}px;
                height: ${size}px;
                background: rgba(255,255,255,0.3);
                border-radius: 50%;
                transform: translate(${x}px, ${y}px) scale(0);
                animation: ripple 0.6s ease-out;
                pointer-events: none;
            `;
            
            card.appendChild(ripple);
            setTimeout(() => ripple.remove(), 600);
        });
    });
});