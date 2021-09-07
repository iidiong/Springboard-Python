class BloggleGame {
    constructor(boardId, seconds = 60) {
        this.seconds = seconds;
        this.showTimer();
        this.score = 0;
        this.words = new Set();
        this.board = $("#" + boardId);

        this.timer = setInterval(this.tick.bind(this), 1000);
        $(".add-word", this.board).on("submit", this.handleSubmit.bind(this));
    }
    /* show correct word list */
    showWord(word) {
        console.log(word)
        let wordList = $("<li></li>").text(word);
        $(".words", this.board).append(wordList);
    }

    showScore() {
        $(".score", this.board).text(this.score);
    }
    /* show message  */
    showMessage(msg, cls) {
        $(".msg", this.board).text(msg).removeClass().addClass().addClass(`msg ${cls}`);
    }

    /* Handles word submited  */
    async handleSubmit(event) {
        event.preventDefault();
        const $word = $(".word", this.board);
        let word = $word.val();
        if (!word) return;

        if (this.words.has(word)) {
            this.showMessage(`Already found ${word}`, "err");
            return;
        }

        const response = await axios.get("/check-word", { params: { word: word } });
        if (response.data.result === "not-word") {
            this.showMessage(` ${word} is not a valid English word`, "err");
        } else if (response.data.result === "not-on-board") {
            this.showMessage(` ${word} is not a valid word on this board`, "err");
        } else {
            this.showWord(word);
            this.score += word.length;
            this.showScore();
            this.words.add(word);
            this.showMessage(`Added: ${word}`, "ok");
        }
        $word.val("").focus();
    }

    showTimer() {
        $(".timer", this.board).text(this.seconds);
    }

    async tick() {
        this.seconds -= 1;
        this.showTimer();

        if (this.seconds === 0) {
            clearInterval(this.timer);
            await this.scoreGame();
        }
    }
    async scoreGame() {
        $(".add-word", this.board).hide();
        const response = await axios.post("/post-score", { score: this.score });
        if (response.data.brokeRecord) {
            this.showMessage(`New recored: ${this.score}`, "ok");
        } else {
            this.showMessage(`Final score: ${this.score}`, "ok")
        }
    }
}