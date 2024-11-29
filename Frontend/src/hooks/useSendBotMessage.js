import { useState } from "react"
import useChat from "../zustand/useChat";
import toast from "react-hot-toast"

const useSendMessage = () => {
    const [loading, setLoading] = useState(false);
    const { chatText, setChatText } = useChat();

    const sendMessage = async (message) => {
        setLoading(true)
        try {
            const res = await fetch(`/api/chat`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ user_input: message})
            })

            const data = await res.json();
            console.log(data)
            if(data.error){
                throw new Error(data.error)
            }
            setChatText([...chatText,{ user: message, bot: data.response }])
            console.log(chatText)

        } catch (error) {
            toast.error(error.message)
        } finally {
            setLoading(false)
        }
    }

   
    return {sendMessage,loading}
}

export default useSendMessage

