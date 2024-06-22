import os
import json
import random

# Save messages for retrieval later on
def get_recent_messages():

  # Define the file name
  file_name = "stored_data.json"
  learn_instruction = {"role": "system", 
                       "content": "You are a highly experienced, and persuasive Tesla rep and your name is Janice. You always manage to convince people to buy a Tesla. You are cold calling leads who may be intersted in buying a tesla. Talk to them and convince them to buy one.  DO NOT mention that you're a sales rep on the phone call just say you're calling from Tesla. Keep responses under 30 words. "}

  messages = []

  # Add Random Element
  x = random.uniform(0, 1)
  if x < 0.2:
    learn_instruction["content"] = learn_instruction["content"] + "Your response will have some light humour "
  elif x < 0.5:
    learn_instruction["content"] = learn_instruction["content"] + "Your response will rhetorically question the user"
  else:
    learn_instruction["content"] = learn_instruction["content"] + "Your response will be a bit more serious "

  # Append instruction to message
  messages.append(learn_instruction)

  # Get last messages
  try:
    with open(file_name) as user_file:
      data = json.load(user_file)
      
      # Append last 5 rows of data
      if data:
        if len(data) < 5:
          for item in data:
            messages.append(item)
        else:
          for item in data[-5:]:
            messages.append(item)
  except:
    pass

  
  # Return messages
  return messages


