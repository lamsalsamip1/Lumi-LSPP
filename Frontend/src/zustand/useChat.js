import { create } from "zustand";



const useChat = create((set) => ({
    chatText: [],
    setChatText: (newChatText) => set({ chatText: newChatText }),
    message:"",
    setMessage:(newMessage)=>set({message:newMessage})
}));

export default useChat;
