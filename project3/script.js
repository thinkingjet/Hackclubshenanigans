// js/script.js

document.addEventListener('DOMContentLoaded', () => {
    console.log('Document is ready');

    // Smooth scrolling for navigation links
    document.querySelectorAll('nav ul li a').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();

            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Typewriter effect for hero text
    const heroTitle = document.getElementById('hero-title');
    const heroTagline = document.getElementById('hero-tagline');
    const heroText = heroTitle.textContent;
    heroTitle.textContent = '';

    let index = 0;

    function typeWriter() {
        if (index < heroText.length) {
            heroTitle.textContent += heroText.charAt(index);
            index++;
            setTimeout(typeWriter, 100);
        } else {
            heroTagline.classList.add('fadeIn');
        }
    }

    typeWriter();
});
