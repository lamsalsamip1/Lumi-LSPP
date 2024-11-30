import { create } from "zustand";



const useChat = create((set) => ({
    chatText: [],
    setChatText: (newChatText) => set({ chatText: newChatText }),
    lastContext:"",
    setLastContext:(newContext)=>set({lastContext:newContext}),
    message:"",
    setMessage:(newMessage)=>set({message:newMessage}),
    promptClick: false,
    setPromptClick: (newPrompt) => set({ promptClick: newPrompt })
}));

export default useChat;
