import { useState } from "react";
import useChat from "../zustand/useChat";
import toast from "react-hot-toast";

const useClearHistory = () => {
    const [loadingc, setLoadingc] = useState(false);
    const { setChatText } = useChat();  // Access the setChatText function

    const clearHistory = async () => {
        setLoadingc(true);
        try {
            const res = await fetch(`https://lumi-lspp-eehwhca8ahe5dchp.centralindia-01.azurewebsites.net/clear_history`, {
                method: "GET",  // Ensure this matches your Flask backend
                headers: { "Content-Type": "application/json" },
            });

            const data = await res.json();
            console.log(data);  // Check if the response is successful
            if (data.error) {
                throw new Error(data.error);
            }

            // Clear the chat history in the frontend
            setChatText([]);  // This will empty the chat history

            toast.success("Conversation history cleared!");
        } catch (error) {
            console.error("Error clearing history:", error); // Add error handling and logging
            toast.error(error.message);
        } finally {
            setLoadingc(false);
        }
    };

    return { clearHistory, loadingc };
};


export default useClearHistory;
