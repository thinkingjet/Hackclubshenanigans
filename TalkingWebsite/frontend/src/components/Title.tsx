import { useState } from "react";
import axios from "axios";

type Props = {
  setMessages: any;
};

// Title component to display the header and reset button
function Title({ setMessages }: Props) {
  // State hook to manage the resetting status
  const [isResetting, setIsResetting] = useState(false);

  // Function to reset the conversation by calling the reset endpoint
  const resetConversation = async () => {
    setIsResetting(true); // Set resetting status to true

    await axios
      .get("http://localhost:8000/reset", {
        headers: {
          "Content-Type": "application/json",
        },
      })
      .then((res) => {
        if (res.status == 200) {
          setMessages([]); // Clear the messages if the reset was successful
        }
      })
      .catch((err) => {
        console.error(err); // Log any errors
      });

    setIsResetting(false); // Set resetting status to false
  };

  return (
    <div
      className="flex justify-between items-center w-full p-4 text-white font-bold shadow"
      style={{
        background: 'linear-gradient(to right, #2f2f2f, #1b1b1b, #2f2f2f)', 
        color: '#ffffff', 
        padding: '20px',
        boxShadow: '0 0 10px rgba(0, 0, 0, 0.3)',
        border: '1px solid #ffffff'
      }}
    >
      <div className="italic">Tesla AI Sales Rep</div>
      <button
        onClick={resetConversation}
        className={
          "transition-all duration-300 text-blue-300 hover:text-pink-500 " +
          (isResetting && "animate-pulse") // Add a pulsing animation if resetting
        }
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          strokeWidth={1.5}
          stroke="currentColor"
          className="w-6 h-6"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            d="M16.023 9.348h4.992v-.001M2.985 19.644v-4.992m0 0h4.992m-4.993 0l3.181 3.183a8.25 8.25 0 0013.803-3.7M4.031 9.865a8.25 8.25 0 0113.803-3.7l3.181 3.182m0-4.991v4.99"
          />
        </svg>
      </button>
    </div>
  );
}

export default Title;
