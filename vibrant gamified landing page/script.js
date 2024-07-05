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

    // Countdown timer
    const countdown = document.getElementById('countdown');
    const daysSpan = document.getElementById('days');
    const hoursSpan = document.getElementById('hours');
    const minutesSpan = document.getElementById('minutes');
    const secondsSpan = document.getElementById('seconds');

    // Set the date we're counting down to
    const targetDate = new Date('2024-08-31T00:00:00').getTime();

    // Update the count down every 1 second
    const countdownFunction = setInterval(() => {
        const now = new Date().getTime();
        const distance = targetDate - now;

        // Time calculations for days, hours, minutes, and seconds
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Display the result
        daysSpan.innerHTML = days;
        hoursSpan.innerHTML = hours;
        minutesSpan.innerHTML = minutes;
        secondsSpan.innerHTML = seconds;

        // If the count down is finished, write some text
        if (distance < 0) {
            clearInterval(countdownFunction);
            countdown.innerHTML = "The game is live!";
        }
    }, 1000);

    // Remove loader after content is loaded
    window.addEventListener('load', () => {
        document.body.classList.remove('loading');
        const loader = document.getElementById('loader');
        if (loader) {
            loader.remove();
        }
    });

    // Add loading class to body
    document.body.classList.add('loading');

    // Handle form submission
    const contactForm = document.getElementById('contact-form');

    contactForm.addEventListener('submit', (event) => {
        event.preventDefault();

        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const message = document.getElementById('message').value;

        if (name && email && message) {
            alert('Thank you for your message!');
            contactForm.reset();
        } else {
            alert('Please fill out all fields.');
        }
    });

    // Handle newsletter form submission
    const newsletterForm = document.getElementById('newsletter-form');

    newsletterForm.addEventListener('submit', (event) => {
        event.preventDefault();

        const email = document.getElementById('newsletter-email').value;

        if (email) {
            alert('Thank you for subscribing to our newsletter!');
            newsletterForm.reset();
        } else {
            alert('Please enter a valid email address.');
        }
    });

    // Animation on scroll
    const animatedElements = document.querySelectorAll('.animated');

    const animateOnScroll = () => {
        const scrollPosition = window.pageYOffset + window.innerHeight;

        animatedElements.forEach(element => {
            if (scrollPosition > element.offsetTop + 100) {
                element.classList.add('visible');
            }
        });
    };

    window.addEventListener('scroll', animateOnScroll);
    animateOnScroll(); // Initial call to animate elements already in view
});
