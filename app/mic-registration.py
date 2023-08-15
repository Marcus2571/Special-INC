import pyaudio
import wave
import speech_recognition as sr

from queue import Queue
from threading import Thread

CHUNK = 1024
AUDIO_FORMAT = pyaudio.paInt16
CHANNELS = 1
FRAME_RATE = 16000
RECORD_SECONDS = 3

messages = Queue()
recording = Queue()

re = sr.Recognizer()

def speech_recognition():
    while not messages.empty():
        frames = recording.get()
        with wave.open('myfile.wav', 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(2)  # 2 bytes per sample for paInt16 format
            wf.setframerate(FRAME_RATE)
            wf.writeframes(b''.join(frames))

        with sr.AudioFile("myfile.wav") as source:
            audio_data = re.record(source)  # Load audio data

        try:
            text = re.recognize_google(audio_data, language="da-DK")
            print("Transcription:", text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


def record_mic():
    p = pyaudio.PyAudio()
    stream = p.open(format=AUDIO_FORMAT,
                    channels=CHANNELS,
                    rate=FRAME_RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    frames = []

    while not messages.empty():
        data = stream.read(CHUNK)
        frames.append(data)
        if len(frames) >= (FRAME_RATE * RECORD_SECONDS) / CHUNK:
            recording.put(frames.copy())
            frames = []

def start_recording():
    messages.put(True)
    record = Thread(target=record_mic)
    record.start()
    print("recording startet")
    transcribe = Thread(target=speech_recognition)
    transcribe.start()

try:
    start_recording()
except KeyboardInterrupt:
    exit()