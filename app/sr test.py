import speech_recognition as sr
r = sr.Recognizer()

while True:  # Infinite loop to keep recording and recognizing
        with sr.Microphone() as source:
            print("Speak:")
            try:
                # Record the audio for a maximum of 5 seconds
                audio = r.listen(source, phrase_time_limit=3)

                # Recognize the audio using Google's service
                text = r.recognize_google(audio, language="da-DK")
                print("You said : {}".format(text))
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
            except Exception as e:
                print(f"An error occurred: {e}")