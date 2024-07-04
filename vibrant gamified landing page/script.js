document.addEventListener('DOMContentLoaded', () => {
    const startBtn = document.getElementById('start-btn');

    startBtn.addEventListener('click', () => {
        alert('Game is starting soon!');
        // Alternatively, you can redirect to another page:
        // window.location.href = 'game.html';
    });
});
document.addEventListener('DOMContentLoaded', () => {
    const startBtn = document.getElementById('start-btn');

    startBtn.addEventListener('click', () => {
        alert('Game is starting soon!');
        // Alternatively, you can redirect to another page:
        // window.location.href = 'game.html';
    });

    // Smooth scroll for navigation links
    const navLinks = document.querySelectorAll('nav ul li a');

    navLinks.forEach(link => {
        link.addEventListener('click', (event) => {
            event.preventDefault();
            const targetId = link.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);
            
            window.scrollTo({
                top: targetSection.offsetTop - 20,
                behavior: 'smooth'
            });
        });
    });
});
