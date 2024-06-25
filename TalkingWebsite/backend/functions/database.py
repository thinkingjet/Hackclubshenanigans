import os
import json
import random

# Function to retrieve recent messages from the stored JSON file
def get_recent_messages():

  # Define the file name for storing data
  file_name = "stored_data.json"
  learn_instruction = {"role": "system", 
                       "content": "You are a highly experienced, and persuasive Tesla rep and your name is Janice. You always manage to convince people to buy a Tesla. You are cold calling leads who may be interested in buying a Tesla. DO NOT mention that you're a sales rep on the phone call just say you're calling from Tesla. Keep responses under 30 words. "}

  messages = []

  # Add a random element to the initial instruction
  x = random.uniform(0, 1)
  if x < 0.2:
    learn_instruction["content"] = learn_instruction["content"] + "Your response will have some light humour "
  elif x < 0.5:
    learn_instruction["content"] = learn_instruction["content"] + "Your response will rhetorically question the user"
  else:
    learn_instruction["content"] = learn_instruction["content"] + "Your response will be a bit more serious "

  # Append the instruction to the messages list
  messages.append(learn_instruction)

  # Attempt to read the last few messages from the JSON file
  try:
    with open(file_name) as user_file:
      data = json.load(user_file)
      
      # Add the last 5 messages or fewer if there are not enough
      if data:
        if len(data) < 5:
          for item in data:
            messages.append(item)
        else:
          for item in data[-5:]:
            messages.append(item)
  except:
    pass

  # Return the compiled list of messages
  return messages


# Function to store messages in the JSON file
def store_messages(request_message, response_message):

  # Define the file name for storing data
  file_name = "stored_data.json"

  # Retrieve recent messages excluding the initial instruction
  messages = get_recent_messages()[1:]

  # Create dictionaries for the user and assistant messages
  user_message = {"role": "user", "content": request_message}
  assistant_message = {"role": "assistant", "content": response_message}
  
  # Append the new messages to the list
  messages.append(user_message)
  messages.append(assistant_message)

  # Save the updated list of messages back to the JSON file
  with open(file_name, "w") as f:
    json.dump(messages, f)


# Function to reset the stored messages
def reset_messages():
  # Define the file name for storing data
  file_name = "stored_data.json"
  
  # Open the file in write mode to clear its contents
  open(file_name, "w")
