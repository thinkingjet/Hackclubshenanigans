import requests, os

# API key for Eleven Labs text-to-speech service
ELEVEN_LABS_API_KEY = "7f155758d3a775aee9f4d1d1516c3673"

# Function to convert text to speech using Eleven Labs API
def convert_text_to_speech(message):
  # Define the request payload with the text message and voice settings
  body = {
    "text": message,
    "voice_settings": {
        "stability": 0,
        "similarity_boost": 0
    }
  }

  # Construct request headers and the API endpoint URL
  headers = { "xi-api-key": ELEVEN_LABS_API_KEY, "Content-Type": "application/json", "accept": "audio/mpeg" }
  endpoint = "https://api.elevenlabs.io/v1/text-to-speech/9gQturXfOo84Pwo2hsU0"

  try:
    # Send a POST request to the API with the message payload and headers
    response = requests.post(endpoint, json=body, headers=headers)
    # Uncomment the following lines to save the response content to a file
    # with open('output.mp3', 'wb') as f:
    #     for chunk in response.iter_content(chunk_size=1024):
    #         if chunk:
    #             f.write(chunk)
  except Exception as e:
     # Print the exception message if the request fails
     print(e)
     return

  # Check if the request was successful
  if response.status_code == 200:
      # Uncomment the following lines to save the audio data to a file
      # with open("output.wav", "wb") as f:
      #     f.write(audio_data)
      return response.content
  else:
    # Return None if the request was not successful
    return
