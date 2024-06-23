import { useState } from "react";
import axios from "axios";

function Title({ setMessages }: Props) {
    const [isResetting, setIsResetting] = useState(false);
  
    const resetConversation = async () => {
      setIsResetting(true);}}