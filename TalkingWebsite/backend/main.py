# need to run the backend each time:
# uvicorn main:app --reload




import openai, os
from functions.text_to_speech import convert_text_to_speech
from functions.openai_requests import convert_audio_to_text, get_chat_response
from functions.database import store_messages, reset_messages
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware





app = FastAPI()

# CORS Origins
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4174",
    "http://localhost:4173",
    "http://localhost:3000",
]


# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_headers=["*"],
    allow_methods=["*"],
    allow_credentials=True,
)

@app.get("/check")
async def check_health():
    return {"response": "working properly"}


#testing
@app.get("/post-audio-get/")
async def get_audio():
    audio_input = open("voice.mp3", "rb")
    message_decoded = convert_audio_to_text(audio_input)
    message_decoded = convert_audio_to_text(audio_input)
    if not message_decoded:
        raise HTTPException(status_code=400, detail="Failed to decode audio")
<<<<<<< HEAD
    
# reset

@app.get("/reset")
async def reset_conversation():
    reset_messages()
    return {"response": "conversation reset"}



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
=======
    chat_response = get_chat_response(message_decoded)
    store_messages(message_decoded, chat_response)
    print(chat_response)
    audio_output = convert_text_to_speech(chat_response)
    if not audio_output:
        raise HTTPException(status_code=400, detail="Failed audio output")
    def iterfile():
       yield audio_output
    return StreamingResponse(iterfile(), media_type="application/mpeg")

>>>>>>> 387c0116d9e5e128a56f519c4515067ec5c6b728
