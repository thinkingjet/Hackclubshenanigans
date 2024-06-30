// script.js

document.addEventListener('DOMContentLoaded', () => {
    const questionElement = document.getElementById('question');
    const answerButtonsElement = document.getElementById('answer-buttons');
    const nextButton = document.getElementById('next-btn');

    let currentQuestionIndex = 0;

    const questions = [
        {
            question: 'What is the capital of France?',
            answers: [
                { text: 'Berlin', correct: false },
                { text: 'Madrid', correct: false },
                { text: 'Paris', correct: true },
                { text: 'Lisbon', correct: false }
            ]
        },
        {
            question: 'Which planet is known as the Red Planet?',
            answers: [
                { text: 'Earth', correct: false },
                { text: 'Mars', correct: true },
                { text: 'Jupiter', correct: false },
                { text: 'Saturn', correct: false }
            ]
        },
        {
            question: 'What is the largest ocean on Earth?',
            answers: [
                { text: 'Atlantic Ocean', correct: false },
                { text: 'Indian Ocean', correct: false },
                { text: 'Arctic Ocean', correct: false },
                { text: 'Pacific Ocean', correct: true }
            ]
        }
    ];

    function startQuiz() {
        currentQuestionIndex = 0;
        nextButton.classList.add('hide');
        showQuestion(questions[currentQuestionIndex]);
    }

    function showQuestion(question) {
        questionElement.innerText = question.question;
        answerButtonsElement.innerHTML = '';
        question.answers.forEach(answer => {
            const button = document.createElement('button');
            button.innerText = answer.text;
            button.classList.add('btn');
            if (answer.correct) {
                button.dataset.correct = answer.correct;
            }
            button.addEventListener('click', selectAnswer);
            answerButtonsElement.appendChild(button);
        });
    }

    function selectAnswer(e) {
        const selectedButton = e.target;
        const correct = selectedButton.dataset.correct;
        Array.from(answerButtonsElement.children).forEach(button => {
            setStatusClass(button, button.dataset.correct);
        });
        if (questions.length > currentQuestionIndex + 1) {
            nextButton.classList.remove('hide');
        } else {
            nextButton.innerText = 'Restart';
            nextButton.classList.remove('hide');
        }
    }

    function setStatusClass(element, correct) {
        clearStatusClass(element);
        if (correct) {
            element.classList.add('correct');
        } else {
            element.classList.add('wrong');
        }
    }

    function clearStatusClass(element) {
        element.classList.remove('correct');
        element.classList.remove('wrong');
    }

    nextButton.addEventListener('click', () => {
        currentQuestionIndex++;
        if (questions.length > currentQuestionIndex) {
            showQuestion(questions[currentQuestionIndex]);
        } else {
            startQuiz();
        }
    });

    startQuiz();
});
