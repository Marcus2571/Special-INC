# import speech_recognition as sr
# import asyncio
# r = sr.Recognizer()

# async def RecordMic():
#     while True:  # Infinite loop to keep recording and recognizing
#         with sr.Microphone() as source:
#             print("Speak:")
#             try:
#                 # Record the audio for a maximum of 5 seconds
#                 audio = r.listen(source, phrase_time_limit=3)     
# async def RecognizeSpeech():


#                 # Recognize the audio using Google's service
#                 text = r.recognize_google(audio, language="da-DK")
#                 print("You said : {}".format(text))
#             except sr.UnknownValueError:
#                 print("Google Speech Recognition could not understand audio")
#             except sr.RequestError as e:
#                 print("Could not request results from Google Speech Recognition service; {0}".format(e))
#             except Exception as e:
#                 print(f"An error occurred: {e}")

import asyncio
import websockets
import pyaudio
from google.cloud import speech_v1p1beta1 as speech

import os

# Set the path to your JSON service account key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/matty/Desktop/Special Inc/Special-Inc/app/ihatemylife.json"

CHUNK_SIZE = 1600  # Adjust based on your preference
SAMPLE_RATE = 16000
LANGUAGE_CODE = "da-DK"

async def audio_streaming():
    client = speech.SpeechClient()

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=SAMPLE_RATE,
        language_code=LANGUAGE_CODE,
    )
    streaming_config = speech.StreamingRecognitionConfig(
        config=config, interim_results=True
    )

    async with websockets.connect("wss://speech.googleapis.com/v1p1beta1/speech:streamingRecognize") as websocket:
        # Send the initial streaming request
        await websocket.send(
            '{"streaming_config": ' + streaming_config.to_json_string() + "}"
        )

        audio_stream = pyaudio.PyAudio().open(
            format=pyaudio.paInt16,
            channels=1,
            rate=SAMPLE_RATE,
            input=True,
            frames_per_buffer=CHUNK_SIZE,
        )

        print("Streaming audio...")
        while True:
            audio_chunk = audio_stream.read(CHUNK_SIZE)
            await websocket.send(audio_chunk)
            response = await websocket.recv()
            print(response)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(audio_streaming())
