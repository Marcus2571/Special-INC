import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "output.wav"
IS_RECORDING = False

p = pyaudio.PyAudio()

def start_recording(self):
    IS_RECORDING = True
    while IS_RECORDING:
        self.stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)


        print("* recording")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
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