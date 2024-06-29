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

    // Points system
    const pointsDisplay = document.getElementById('points');
    const progressBar = document.getElementById('progress-bar');
    let points = 0;

    document.getElementById('increment-points').addEventListener('click', () => {
        points += 10;
        pointsDisplay.textContent = points;
        progressBar.style.width = `${Math.min(points, 100)}%`;

        // Play sound effect on button click
        const clickSound = document.getElementById('click-sound');
        clickSound.currentTime = 0;
        clickSound.play();
    });
});

// Function to update leaderboard
function updateLeaderboard(username, points) {
    const leaderboardList = document.getElementById('leaderboard-list');
    const listItem = document.createElement('li');
    listItem.innerHTML = `
        <span>${username}</span>
        <span>${points} points</span>
    `;
    leaderboardList.appendChild(listItem);
}

// Example usage:
// Call updateLeaderboard(username, points) when points are updated
// updateLeaderboard('User123', 50);
// js/script.js

document.addEventListener('DOMContentLoaded', () => {
    console.log('Document is ready');

    // Fetch leaderboard data
    fetch('http://localhost:3000/users')
        .then(response => response.json())
        .then(users => {
            users.forEach(user => {
                updateLeaderboard(user.username, user.points);
            });
        })
        .catch(error => console.error('Error fetching data:', error));

    // Function to update leaderboard
    function updateLeaderboard(username, points) {
        const leaderboardList = document.getElementById('leaderboard-list');
        const listItem = document.createElement('li');
        listItem.innerHTML = `
            <span>${username}</span>
            <span>${points} points</span>
        `;
        leaderboardList.appendChild(listItem);
    }

    // Example usage:
    // Call updateLeaderboard(username, points) when points are updated
    // updateLeaderboard('User123', 50);

    // Other existing functions...
});

// js/script.js

document.addEventListener('DOMContentLoaded', () => {
    console.log('Document is ready');

    // Fetch leaderboard data
    fetch('http://localhost:3000/users')
        .then(response => response.json())
        .then(users => {
            users.forEach(user => {
                updateLeaderboard(user.username, user.points);
            });
        })
        .catch(error => console.error('Error fetching data:', error));

    // Existing code...

    const pointsDisplay = document.getElementById('points');
    const progressBar = document.getElementById('progress-bar');
    let points = 0;
    const username = 'CurrentUser'; // Replace with dynamic username as needed

    document.getElementById('increment-points').addEventListener('click', () => {
        points += 10;
        pointsDisplay.textContent = points;
        progressBar.style.width = `${Math.min(points, 100)}%`;

        // Play sound effect on button click
        const clickSound = document.getElementById('click-sound');
        clickSound.currentTime = 0;
        clickSound.play();

        // Update points on the server
        fetch(`http://localhost:3000/users/1`, { // Replace with dynamic user ID as needed
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ points })
        })
        .then(response => response.json())
        .then(updatedUser => {
            // Clear existing leaderboard
            const leaderboardList = document.getElementById('leaderboard-list');
            leaderboardList.innerHTML = '';

            // Fetch updated leaderboard data
            fetch('http://localhost:3000/users')
                .then(response => response.json())
                .then(users => {
                    users.forEach(user => {
                        updateLeaderboard(user.username, user.points);
                    });
                })
                .catch(error => console.error('Error fetching data:', error));
        })
        .catch(error => console.error('Error updating data:', error));
    });

    // Function to update leaderboard
    function updateLeaderboard(username, points) {
        const leaderboardList = document.getElementById('leaderboard-list');
        const listItem = document.createElement('li');
        listItem.innerHTML = `
            <span>${username}</span>
            <span>${points} points</span>
        `;
        leaderboardList.appendChild(listItem);
    }
});


// js/script.js

document.addEventListener('DOMContentLoaded', () => {
    console.log('Document is ready');

    // Fetch leaderboard data
    fetch('http://localhost:3000/users')
        .then(response => response.json())
        .then(users => {
            users.forEach(user => {
                updateLeaderboard(user.username, user.points);
            });
        })
        .catch(error => console.error('Error fetching data:', error));

    const pointsDisplay = document.getElementById('points');
    const progressBar = document.getElementById('progress-bar');
    let points = 0;
    const username = 'CurrentUser'; // Replace with dynamic username as needed

    document.getElementById('increment-points').addEventListener('click', () => {
        points += 10;
        pointsDisplay.textContent = points;
        progressBar.style.width = `${Math.min(points, 100)}%`;

        // Play sound effect on button click
        const clickSound = document.getElementById('click-sound');
        clickSound.currentTime = 0;
        clickSound.play();

        // Update points on the server
        fetch(`http://localhost:3000/users/1`, { // Replace with dynamic user ID as needed
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ points })
        })
        .then(response => response.json())
        .then(updatedUser => {
            // Clear existing leaderboard
            const leaderboardList = document.getElementById('leaderboard-list');
            leaderboardList.innerHTML = '';

            // Fetch updated leaderboard data
            fetch('http://localhost:3000/users')
                .then(response => response.json())
                .then(users => {
                    users.forEach(user => {
                        updateLeaderboard(user.username, user.points);
                    });
                })
                .catch(error => console.error('Error fetching data:', error));
        })
        .catch(error => console.error('Error updating data:', error));
    });

    // Function to update leaderboard
    function updateLeaderboard(username, points) {
        const leaderboardList = document.getElementById('leaderboard-list');
        const listItem = document.createElement('li');
        listItem.innerHTML = `
            <span>${username}</span>
            <span>${points} points</span>
        `;
        leaderboardList.appendChild(listItem);
    }

    // Avatar selection and upload
    const avatarImg = document.getElementById('avatar-img');
    const avatarUpload = document.getElementById('avatar-upload');
    const changeAvatarButton = document.getElementById('change-avatar');

    changeAvatarButton.addEventListener('click', () => {
        avatarUpload.click();
    });

    avatarUpload.addEventListener('change', (event) => {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                avatarImg.src = e.target.result;
                // Save avatar to local storage or send to server
                localStorage.setItem('userAvatar', e.target.result);
            };
            reader.readAsDataURL(file);
        }
    });

    // Load avatar from local storage
    const savedAvatar = localStorage.getItem('userAvatar');
    if (savedAvatar) {
        avatarImg.src = savedAvatar;
    }
});
