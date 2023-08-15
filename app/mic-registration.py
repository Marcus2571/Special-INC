import pyaudio
import wave

from queue import Queue
from threading import Thread

CHUNK = 1024
AUDIO_FORMAT = pyaudio.paInt16
CHANNELS = 1
FRAME_RATE = 16000
RECORD_SECONDS = 20


def start_recording(self):
    p = pyaudio.PyAudio()
    IS_RECORDING = True
    while IS_RECORDING:
        self.stream = p.open(format=AUDIO_FORMAT,
                        channels=CHANNELS,
                        rate=FRAME_RATE,
                        input=True,
                        frames_per_buffer=CHUNK)


        print("* recording")

        frames = []

        for i in range(0, int(FRAME_RATE / CHUNK * RECORD_SECONDS)):
            data = self.stream.read(CHUNK)
            frames.append(data)

        print("* done recording")

        self.stream.stop_stream()
        self.stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

def stop_recording(self):
    IS_RECORDING = False