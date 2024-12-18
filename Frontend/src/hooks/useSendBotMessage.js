import { useState } from "react";
import useChat from "../zustand/useChat";
import toast from "react-hot-toast";

const useSendMessage = () => {
  const [loading, setLoading] = useState(false);
  const { chatText, setChatText, lastContext, setLastContext } = useChat();

  const sendMessage = async (message) => {
    setLoading(true);
    try {
      console.log(
        JSON.stringify({
          user_input: message,
          last_context: lastContext,
          conversation_history: chatText,
        })
      );
      // const res = await fetch(`https://lumi-lspp-eehwhca8ahe5dchp.centralindia-01.azurewebsites.net/chat`, {
      const res = await fetch(
        `https://lumi-lspp-eehwhca8ahe5dchp.centralindia-01.azurewebsites.net/chat`,
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            user_input: message,
            last_context: lastContext,
            conversation_history: chatText,
          }),
        }
      );

      const data = await res.json();
      console.log(data);
      if (data.error) {
        throw new Error(data.error);
      }
      setChatText([...chatText, { user: message, assistant: data.response }]);
      console.log("API returned context:", data.context);

      setLastContext(data.context);
      // console.log(chatText)
      // console.log(lastContext)
    } catch (error) {
      toast.error(error.message);
    } finally {
      setLoading(false);
    }
  };

  return { sendMessage, loading };
};

export default useSendMessage;
