# import base64
# import oneai
# import asyncio
# import mic_registration as mr

# oneai.api_key = "aa5e46af-9c98-4434-86ac-9fcfab494df1"
# pipeline = oneai.Pipeline(steps=[
#     oneai.skills.Transcribe()
# ])

# async def main():
#     with open('C:/Users/marcu/Downloads/kids.wav', 'rb') as inputf:
#         output = await pipeline.run_async(inputf)

#     print(output.text)

# asyncio.run(main())
import threading
import pyaudio
import requests
import time
import wave
import os
import oneai

# Initialize variables
oneai.api_key = "aa5e46af-9c98-4434-86ac-9fcfab494df1"  # Replace with your One AI API key
recording = True  # Flag to control audio capture loop
audio_buffer = b""
buffer_size = 0
chunk_threshold = 44100 * 40  # Adjust the threshold as needed (e.g., 10 seconds of audio)

def start_audio_capture():
    global audio_buffer, buffer_size
    
    sample_rate = 44100
    channels = 1

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    frames_per_buffer=1024)

    while recording:
        audio_chunk = stream.read(1024)
        audio_buffer += audio_chunk
        buffer_size += len(audio_chunk)

        if buffer_size >= chunk_threshold:
            send_audio_chunk_for_transcription()
        
    stream.stop_stream()
    stream.close()
    p.terminate()

def send_audio_chunk_for_transcription():
    global audio_buffer, buffer_size

    try:
        # Save audio chunk to a temporary file
        temp_file_path = "temp_audio_chunk.wav"
        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(audio_buffer)

        # Create a pipeline for transcription
        pipeline = oneai.Pipeline(steps=[
            oneai.skills.Transcribe()
        ])

        # Send the audio chunk for transcription
        with open(temp_file_path, 'rb') as input_file:
            response = pipeline.run(input_file)

        # Print the API response
        print("API response:", response)

    except Exception as e:
        print("API request failed with error:", e)

    # Clear the audio buffer
    audio_buffer = b""
    buffer_size = 0
    # os.remove(temp_file_path)

def stop_audio_capture():
    global recording
    recording = False  # Set the flag to stop the audio capture loop

# Start audio capture in a separate thread
audio_thread = threading.Thread(target=start_audio_capture)
audio_thread.start()

# Let the audio capture run for a while
time.sleep(20)

# Stop audio capture
stop_audio_capture()
audio_thread.join()
