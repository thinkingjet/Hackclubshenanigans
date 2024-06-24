import React, { useState } from "react";
import Title from "./Title";
import axios from "axios";
import RecordMessage from "./RecordMessage";

const Controller = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [messages, setMessages] = useState([]);

  const createBlobURL = (data) => {
    const blob = new Blob([data], { type: "audio/mpeg" });
    return URL.createObjectURL(blob);
  };

  const handleStop = async (blobUrl) => {
    setIsLoading(true);

    try {
      const myMessage = { sender: "me", blobUrl };
      const messagesArr = [...messages, myMessage];

      const response = await fetch(blobUrl);
      const blob = await response.blob();

      const formData = new FormData();
      formData.append("file", blob, "myFile.wav");

      const res = await axios.post("http://localhost:8000/post-audio", formData, {
        headers: {
          "Content-Type": "audio/mpeg",
        },
        responseType: "arraybuffer",
      });

      const audioBlob = res.data;
      const audio = new Audio();
      audio.src = createBlobURL(audioBlob);

      const janiceMessage = { sender: "Janice", blobUrl: audio.src };
      setMessages([...messagesArr, janiceMessage]);

    } catch (error) {
      console.error("Error posting audio:", error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div>
      <Title />
      <RecordMessage onStop={handleStop} />
      {isLoading && <p>Loading...</p>}
      <ul>
        {messages.map((message, index) => (
          <li key={index}>
            <p>{message.sender}</p>
            <audio controls src={message.blobUrl}></audio>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Controller;
