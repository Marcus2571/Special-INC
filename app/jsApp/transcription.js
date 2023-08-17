class SpeechRecognitionHandler {
    constructor() {
        this.recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
        this.recognition.interimResults = true;
        this.recognition.continuous = true;
        this.recognition.lang = "es-ES";
        this.listening = false;
        this.transcript = "";

        this.recognition.onstart = () => {
            console.log("Starting listening, speak into the microphone");
            this.handleSpeechEvent();
        };

        this.recognition.onend = () => {
            console.log(this.listening ? "Continue listening" : "Stopped listening");
            if (this.listening) {
                this.recognition.start();
            }
        };

        this.recognition.onnomatch = () => {
            console.log("I found no match")
            this.recognition.stop();
        }

        this.recognition.onerror = () => {
            console.log("I died")
        }
    }

    handleSpeechEvent() {
        this.recognition.onresult = event => {
            let partialTranscript = "";
            let currentIndex = event.resultIndex;
            let transcript = event.results[currentIndex][0].transcript;
            if (event.results[currentIndex].isFinal) {
                this.transcript += transcript + " ";
                document.getElementById("text").innerHTML = this.transcript;
                translateTranscript(this.transcript, "es-ES", "da-DK");
            } else {
                partialTranscript += transcript;
                document.getElementById("text").innerHTML = this.transcript + partialTranscript;
            }
        };

    }

    toggleListening() {
        this.listening = !this.listening;

        if (!this.listening) {
            this.recognition.stop();
        } else {
            this.recognition.start();
        }
    }
}

function translateTranscript(text, langFrom, langTo) {
    let toText = document.getElementById("toText");
    let apiUrl = `https://api.mymemory.translated.net/get?q=${text}&langpair=${langFrom}|${langTo}`;
    console.log("hit");
    fetch(apiUrl).then(res => res.json()).then(data => {
        toText.innerHTML = data.responseData.translatedText;
        data.matches.forEach(data => {
            if(data.id === 0) {
                console.log(data.translation);
                toText.innerHTML = data.translation;
            }
        });
    });
};

const speechHandler = new SpeechRecognitionHandler();