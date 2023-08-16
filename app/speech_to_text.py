import azure.cognitiveservices.speech as speechsdk
import pyaudio

def audio_callback(in_data, frame_count, time_info, status):
    return in_data, pyaudio.paContinue

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=16000,
                input=True,
                frames_per_buffer=1024,
                stream_callback=audio_callback)

speech_config = speechsdk.SpeechConfig(subscription="5cd62141dc314dc8ac222e33fe049e34", region="northeurope")
audio_stream = speechsdk.AudioDataStream(stream=stream)

speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_stream)

result_future = speech_recognizer.start_continuous_recognition()

try:
    result_future.result()  # This will block until recognition is stopped
except KeyboardInterrupt:
    pass

# Clean up
stream.stop_stream()
stream.close()
p.terminate()
