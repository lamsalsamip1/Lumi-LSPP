import Chat from "./components/Chat"
import Send from "./components/Send"

const Chatbot = () => {
  return (
    <div className=" mt-20 mx-auto w-full px-8 pt-4 pb-4 h-screen flex flex-col items-center">
      <div className="flex-1  mb-32 ">
        <Chat />
      </div>
      <div  className=" fixed bottom-0 left-0 right-0 ">
        <Send />
      </div>
    </div>
  )
}

export default Chatbot
