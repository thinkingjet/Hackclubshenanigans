import { useState } from "react";
import Title from "./Title";
import axios from "axios";
import RecordMessage from "./RecordMessage";

const Controller = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [messages, setMessages] = useState<any[]>([]);

  function createBlobURL(data: any) {
    
    const blob = new Blob([data], { type: "audio/mpeg" });
    const url = window.URL.createObjectURL(blob);
    return url;
  }

  const handleStop = async (blobUrl: string) => {
    setIsLoading(true);
    const myMessage = { sender: "me", blobUrl };
    fetch(blobUrl)
    .then((res) => res.blob())
    .then(async (blob) => {
      const formData = new FormData();
      formData.append("file", blob, "myFile.wav");const messagesArr = [...messages, myMessage];
        {/* Recorder */}
        <div className="fixed center-0 w-full py-12 text-center" 
     >
          <div className="flex justify-center items-center w-full">
            <div>
              <RecordMessage handleStop={handleStop} />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Controller;