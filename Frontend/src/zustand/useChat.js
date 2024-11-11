import { create } from "zustand";


const useChat= create((set)=>({
    // chatText:[{user:"abcdehffejlld", bot:"defkdsklfsdkfs"}],
    chatText:[],

    setChatText:(messages)=>set({messages}),
}))

export default useChat;
