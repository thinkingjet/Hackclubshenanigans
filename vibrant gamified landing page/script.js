document.addEventListener('DOMContentLoaded', () => {
    const startBtn = document.getElementById('start-btn');

    startBtn.addEventListener('click', () => {
        alert('Game is starting soon!');
        // Alternatively, you can redirect to another page:
        // window.location.href = 'game.html';
    });
});
