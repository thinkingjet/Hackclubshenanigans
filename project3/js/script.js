// js/script.js

// Enhanced parallax scrolling effect
document.addEventListener('scroll', function() {
    const parallaxSections = document.querySelectorAll('.parallax');
    parallaxSections.forEach(section => {
        const scrollPosition = window.pageYOffset;
        const offset = scrollPosition * 0.5; // Adjust the multiplier to change the speed
        section.style.backgroundPositionY = offset + 'px';
    });
});
