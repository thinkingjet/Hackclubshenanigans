import { useState } from "react";
import Title from "./Title";
import axios from "axios";
import RecordMessage from "./RecordMessage";

const Controller = () => {
  // State hooks to manage loading status and messages array
  const [isLoading, setIsLoading] = useState(false);
  const [messages, setMessages] = useState<any[]>([]);

  // Function to create a URL for the audio blob
  function createBlobURL(data: any) {
    const blob = new Blob([data], { type: "audio/mpeg" });
    const url = window.URL.createObjectURL(blob);
    return url;
  }

  // Handle the stop event of the recording
  const handleStop = async (blobUrl: string) => {
    setIsLoading(true); // Set loading status to true
    const myMessage = { sender: "me", blobUrl }; // Create a message object for the user
    const messagesArr = [...messages, myMessage]; // Append the new message to the existing messages array
    fetch(blobUrl)
      .then((res) => res.blob()) // Fetch the blob from the blob URL
      .then(async (blob) => {
        const formData = new FormData();
        formData.append("file", blob, "myFile.wav"); // Append the blob to the FormData object

        await axios
          .post("http://localhost:8000/post-audio", formData, {
            headers: {
              "Content-Type": "audio/mpeg",
            },
            responseType: "arraybuffer",
          })
          .then((res: any) => {
            const blob = res.data; // Get the binary data from the response
            const audio = new Audio();
            audio.src = createBlobURL(blob); // Create a blob URL for the audio data

            // Uncomment the following lines to add Janice's message to the messages array
            // const JaniceMessage = { sender: "Janice", blobUrl: audio.src };
            // messagesArr.push(JaniceMessage);
            // setMessages(messagesArr);

            setIsLoading(false); // Set loading status to false
            audio.play(); // Play the audio
          })
          .catch((err: any) => {
            console.error(err); // Log any errors
            setIsLoading(false); // Set loading status to false
          });
      });
  };

  return (
    <div className="h-screen overflow-y-hidden">
      {/* Title component */}
      <Title setMessages={setMessages} />

      <div className="flex flex-col justify-between h-full overflow-y-scroll pb-96">
        {/* Conversation area */}
        <div className="mt-5 px-5">
          {messages?.map((audio, index) => {
            return (
              <div
                key={index + audio.sender}
                className={
                  "flex flex-col " +
                  (audio.sender == "Janice" && "flex items-end")
                }
              >
                {/* Sender name */}
                <div className="mt-4 ">
                  <p
                    className={
                      audio.sender == "Janice"
                        ? "text-right mr-2 italic text-green-500"
                        : "ml-2 italic text-blue-500"
                    }
                  >
                    {audio.sender}
                  </p>

                  {/* Audio message */}
                  <audio
                    src={audio.blobUrl}
                    className="appearance-none"
                    controls
                  />
                </div>
              </div>
            );
          })}

          {/* Display a message when there are no messages and not loading */}
          {messages.length == 0 && !isLoading && (
            <div className="text-center font-light italic mt-10" >
              No messages yet, start recording!
            </div>
          )}

          {/* Display a loading indicator when messages are being processed */}
          {isLoading && (
            <div className="text-center font-light italic mt-10 animate-pulse">
              Loading...
            </div>
          )}
        </div>

        {/* Recorder component */}
        <div className="fixed center-0 w-full py-12 text-center">
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


// The Controller component manages the core functionality of 
// the application, including recording, handling, and playing audio messages. 
// It uses state hooks to track the loading status and the array of messages. 
// The createBlobURL function generates a URL for the audio blob data. 
// The handleStop function is called when recording stops, sending 
// the audio data to the server and playing the response. 
// The component renders the Title and RecordMessage components, 
// and dynamically displays the recorded messages.
//  It also handles loading indicators and empty state messages, 
//  ensuring a smooth user experience.






