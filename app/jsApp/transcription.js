class SpeechRecognitionHandler {
    constructor() {
        this.recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
        this.recognition.interimResults = true;
        this.recognition.continuous = true;
        this.recognition.lang = "da-DK";
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
            console.log(event);
            if (event.results[currentIndex].isFinal) {
                this.transcript += transcript + " ";
                document.getElementById("text").innerHTML = this.transcript;
            } else {
                partialTranscript += transcript;
                document.getElementById("text").innerHTML = this.transcript + partialTranscript;
            }
        };

    }

    translateBtn.addEventListener("click", () => {
        let text = fromText.value.trim(),
        translateFrom = selectTag[0].value,
        translateTo = selectTag[1].value;
        if(!text) return;
        toText.setAttribute("placeholder", "Translating...");
        let apiUrl = `https://api.mymemory.translated.net/get?q=${text}&langpair=${translateFrom}|${translateTo}`;
        fetch(apiUrl).then(res => res.json()).then(data => {
            toText.value = data.responseData.translatedText;
            data.matches.forEach(data => {
                if(data.id === 0) {
                    toText.value = data.translation;
                }
            });
            toText.setAttribute("placeholder", "Translation");
        });
    });

    toggleListening() {
        this.listening = !this.listening;

        if (!this.listening) {
            this.recognition.stop();
        } else {
            this.recognition.start();
        }
    }
}

const speechHandler = new SpeechRecognitionHandler();