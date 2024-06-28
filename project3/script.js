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

    // Animate feature cards on scroll
    const featureCards = document.querySelectorAll('.feature-card');
    const observerOptions = {
        threshold: 0.5
    };

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fadeInUp');
            }
        });
    }, observerOptions);

    featureCards.forEach(card => {
        observer.observe(card);
    });
});
