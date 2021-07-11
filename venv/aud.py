import pyaudio
import wave

filename = "recorded.wav"
chunk = 2048
FORMAT = pyaudio.paInt16
channels = 1
sample_rate = 44100
record_seconds = 1
p = pyaudio.PyAudio()
index = int(input())
stream = p.open(format=FORMAT,channels=channels,
                rate=sample_rate,input=True,input_device_index=index,
                frames_per_buffer=chunk)

frames = []
print("Recording...")
for i in range(int(44100 / chunk * record_seconds)):
    data = stream.read(chunk)
    # if you want to hear your voice while recording
    # stream.write(data)
    frames.append(data)
print("Finished recording.")
# stop and close stream
stream.stop_stream()
stream.close()
# terminate pyaudio object
p.terminate()
# save audio file
# open the file in 'write bytes' mode
wf = wave.open(filename, "wb")
# set the channels
wf.setnchannels(channels)
# set the sample format
wf.setsampwidth(p.get_sample_size(FORMAT))
# set the sample rate
wf.setframerate(sample_rate)
# write the frames as bytes
wf.writeframes(b"".join(frames))
# close the file
wf.close()
