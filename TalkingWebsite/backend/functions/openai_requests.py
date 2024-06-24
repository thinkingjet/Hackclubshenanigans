import  os
from functions.database import get_recent_messages

# TODO: The 'openai.organization' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(organization=os.getenv("OPEN_AI_ORG"))'

from openai import OpenAI
client = OpenAI(api_key="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")


# Open AI whisper STT
def convert_audio_to_text(audio_file):
  try:
    transcript = client.audio.transcriptions.create(model="whisper-1", file=audio_file, response_format="text")
    return transcript
  except Exception as e:
    print(e)
    return


def get_chat_response(message_input):

  messages = get_recent_messages()
  user_message = {"role": "user", "content": message_input }
  messages.append(user_message)

  try:
    response =  client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=messages
    )
    message_text = response.choices[0].message.content
    return message_text
  except Exception as e:
    print(e)
    return
