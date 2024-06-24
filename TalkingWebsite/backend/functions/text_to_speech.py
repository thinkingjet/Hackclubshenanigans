import requests, os
ELEVEN_LABS_API_KEY = "7f155758d3a775aee9f4d1d1516c3673"


def convert_text_to_speech(message):
  body = {
    "text": message,
    "voice_settings": {
        "stability": 0,
        "similarity_boost": 0
    }
  }


  # Construct request headers and url
  headers = { "xi-api-key": ELEVEN_LABS_API_KEY, "Content-Type": "application/json", "accept": "audio/mpeg" }
  endpoint = "https://api.elevenlabs.io/v1/text-to-speech/9gQturXfOo84Pwo2hsU0"

  try:
    response = requests.post(endpoint, json=body, headers=headers)
    # with open('output.mp3', 'wb') as f:
    #     for chunk in response.iter_content(chunk_size=1024):
    #         if chunk:
    #             f.write(chunk)
  except Exception as e:
     print(e)
     return

  if response.status_code == 200:
      # with open("output.wav", "wb") as f:
      #     f.write(audio_data)
      return response.content
  else:
    return
