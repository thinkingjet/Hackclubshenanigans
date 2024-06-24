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
