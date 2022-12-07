from google.cloud import speech
import os

os.environ['http_proxy'] = 'http://127.0.0.1:7890'
os.environ['https_proxy'] = 'http://127.0.0.1:7890'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'shell.json'

# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
gcs_uri = "gs://cloud-samples-data/speech/brooklyn_bridge.raw"

def transcribe_speech():
  audio = speech.RecognitionAudio(uri=gcs_uri)
  print(audio)

  config = speech.RecognitionConfig(
      encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
      sample_rate_hertz=16000,
      language_code="en-US",
  )

  # Detects speech in the audio file
  response = client.recognize(config=config, audio=audio)

  for result in response.results:
    print("Transcript: {}".format(result.alternatives[0].transcript))


transcribe_speech()