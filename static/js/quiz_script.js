class Question {
    constructor(questionText, options, correctAnswer) {
        this.questionText = questionText;
        this.options = options;
        this.correctAnswer = correctAnswer;
    }
}

const questions = [
    new Question("Какое число следующее после 7?", ["8", "9", "10", "11"], "9"),
    new Question("Какое число следующее после 10?", ["11", "12", "13", "14"], "11"),
    new Question("Какое число следующее после 13?", ["14", "15", "16", "17"], "15"),
    new Question("Какое число следующее после 16?", ["17", "18", "19", "20"], "18"),
    new Question("Какое число следующее после 19?", ["20", "21", "22", "23"], "21"),
    new Question("Какое число следующее после 22?", ["23", "24", "25", "26"], "24"),
    new Question("Какое число следующее после 25?", ["26", "27", "28", "29"], "27"),
    new Question("Какое число следующее после 28?", ["29", "30", "31", "32"], "30"),
    new Question("Какое число следующее после 31?", ["32", "33", "34", "35"], "33"),
    new Question("Какое число следующее после 34?", ["35", "36", "37", "38"], "36")
];

let currentQuestionIndex = 0;

function displayCurrentQuestion() {
    let questionElement = document.getElementById(`question-${currentQuestionIndex + 1}`);
    let optionsElements = document.getElementsByClassName(`option-${currentQuestionIndex + 1}`);

    if (currentQuestionIndex < questions.length) {
        questionElement.textContent = questions[currentQuestionIndex].questionText;

        for (let i = 0; i < optionsElements.length; i++) {
            optionsElements[i].textContent = questions[currentQuestionIndex].options[i];
        }
    } else {
        questionElement.textContent = "Всё!";
    }
}

function checkAnswer(answerIndex) {
    if (questions[currentQuestionIndex].options[answerIndex] === questions[currentQuestionIndex].correctAnswer) {
        alert('Правильно!');
    } else {
        alert('Неправильно!');
    }

    currentQuestionIndex++;

    displayCurrentQuestion();
}

const optionsElements = document.getElementsByClassName('option');

for (let i = 0; i < optionsElements.length; i++) {
    optionsElements[i].addEventListener('click', () => {
        checkAnswer(i);
    });
}

displayCurrentQuestion();