import oneai
import base64

with open("<YOUR-FILE-PATH>", "rb") as f:
  textParsed = base64.b64encode(f.read())
oneai.api_key = "<YOUR-API-KEY-HERE>"
pipeline = oneai.Pipeline(
  steps = [
		oneai.skills.Transcribe(
  		speaker_detection=True,
		),
  ]
)

conversation = oneai.Conversation(
  textParsed
)

output = pipeline.run(conversation)