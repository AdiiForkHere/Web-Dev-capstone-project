let questions = document.querySelectorAll(".question");
let current = 0;
let time = 10;

let timerEl = document.getElementById("timer");

questions[current].style.display = "block";

let interval = setInterval(() => {
    time--;
    timerEl.innerText = time;

    if (time === 0) {
        questions[current].style.display = "none";
        current++;

        if (current < questions.length) {
            questions[current].style.display = "block";
            time = 10;
        } else {
            clearInterval(interval);
            document.getElementById("submitBtn").style.display = "block";
        }
    }
}, 1000);