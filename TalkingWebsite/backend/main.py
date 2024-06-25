# Import necessary modules and functions
import openai, os
from functions.text_to_speech import convert_text_to_speech
from functions.openai_requests import convert_audio_to_text, get_chat_response
from functions.database import store_messages, reset_messages
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Define allowed origins for CORS
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4174",
    "http://localhost:4173",
    "http://localhost:3000",
]

# Adding CORS middleware to handle cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_headers=["*"],
    allow_methods=["*"],
    allow_credentials=True,
)

# Endpoint to check if the server is running properly
@app.get("/check")
async def check_health():
    return {"response": "working properly"}

# Commented out testing endpoint for audio processing
# @app.get("/post-audio-get/")
# async def get_audio():
#     audio_input = open("voice.mp3", "rb")
#     message_decoded = convert_audio_to_text(audio_input)
#     if not message_decoded:
#         raise HTTPException(status_code=400, detail="Failed to decode audio")
#     chat_response = get_chat_response(message_decoded)
#     store_messages(message_decoded, chat_response)
#     audio_output = convert_text_to_speech(chat_response)
#     if not audio_output:
#         raise HTTPException(status_code=400, detail="Failed audio output")
#     def iterfile():
#         yield audio_output
#     return StreamingResponse(iterfile(), media_type="application/mpeg")

# Endpoint to reset the conversation in the database
@app.get("/reset")
async def reset_conversation():
    reset_messages()
    return {"response": "conversation reset"}

# Endpoint to handle audio file uploads, process the audio and return a response
@app.post("/post-audio/")
async def post_audio(file: UploadFile = File(...)):
    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())
    audio_input = open(file.filename, "rb")
    message_decoded = convert_audio_to_text(audio_input)
    if not message_decoded:
        raise HTTPException(status_code=400, detail="Failed to decode audio")
    chat_response = get_chat_response(message_decoded)
    store_messages(message_decoded, chat_response)
    if not chat_response:
        raise HTTPException(status_code=400, detail="Failed chat response")
    audio_output = convert_text_to_speech(chat_response)
    if not audio_output:
        raise HTTPException(status_code=400, detail="Failed audio output")
    def iterfile():
        yield audio_output
    return StreamingResponse(iterfile(), media_type="application/octet-stream")



"""
Importing Necessary Modules and Functions:

This section imports all required modules and custom functions for the backend. OpenAI for AI interactions, os for file operations, FastAPI for the web framework, and various custom functions for text-to-speech and database interactions.
Setting Up CORS Middleware:

The origins list contains URLs that are allowed to interact with the backend server. The CORS middleware is added to the FastAPI app to handle cross-origin requests, enabling the frontend to communicate with the backend securely.
Health Check Endpoint:

The /check endpoint is a simple route to verify that the server is running correctly. When accessed, it returns a JSON response indicating the server's status.
Commented Out Testing Endpoint:

This commented section shows a previously used or test endpoint for processing audio files. It demonstrates the steps of converting audio to text, getting a chat response, and then converting that response back to speech, although it's currently disabled.
Reset Conversation Endpoint:

The /reset endpoint allows resetting the conversation stored in the database. It's useful for clearing previous interactions and starting fresh, returning a confirmation response when successful.
Handling Audio File Uploads:

The /post-audio endpoint handles uploading audio files. It saves the uploaded file, converts the audio to text, gets a chat response, converts the response back to audio, and streams the audio back to the client. Error handling ensures that any failures in the process return appropriate HTTP status codes and error messages.

"""