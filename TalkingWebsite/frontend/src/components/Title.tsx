import { useState } from "react";
import axios from "axios";


function Title({ setMessages }: Props) {
  const [isResetting, setIsResetting] = useState(false);

  const resetConversation = async () => {
    setIsResetting(true);

    await axios
      .get("http://localhost:8000/reset", {
        headers: {
          "Content-Type": "application/json",
        },
      })
      .then((res) => {
        if (res.status == 200) {
          setMessages([]);
        }

<div className="flex justify-between items-center w-full p-4 text-white font-bold shadow" style={{
      background: 'linear-gradient(to right, #2f2f2f, #1b1b1b, #2f2f2f)', 
      color: '#ffffff', 
      padding: '20px',
      boxShadow: '0 0 10px rgba(0, 0, 0, 0.3)',
      border: '1px solid #ffffff'
    }}>
      <div className="italic">Tesla AI Sales Rep</div>
      <button
        onClick={resetConversation}
        className={
          "transition-all duration-300 text-blue-300 hover:text-pink-500 " +
          (isResetting && "animate-pulse")
        }
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          strokeWidth={1.5}
          stroke="currentColor"
          className="w-6 h-6"
        ></svg>