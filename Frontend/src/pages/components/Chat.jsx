import { lumi, roboticon } from "../../assets";
import useChat from "../../zustand/useChat";
import ReactMarkdown from 'react-markdown';
import { prompts } from '../../constants'
import useSendMessage from "../../hooks/useSendBotMessage";


const Chat = () => {
  const { chatText,setMessage} = useChat();
  const {loading,sendMessage}= useSendMessage();

  const handlePromptClick = async (prompt) => {
    setMessage(prompt);
    await sendMessage(prompt);
    setMessage("");

  }
  return (
    <div className="h-screen w-screen " >
      {chatText.length === 0 &&
        <div className="flex flex-col items-center justify-between gap-8">
          <div className="flex flex-col justify-center items-center h-full">
            <img src={roboticon} className="w-16 sm:w-20 md:w-24" />
            <div className="flex flex-row gap-2 justify-center items-center">
              <span className=" font-bold text-gray-800 text-[16px] md:text-[20px] lg:text-[28px] ">Chat with</span>
              <img src={lumi} className=" w-16 md:w-20 lg:w-24" />
            </div>
            <p className="text-graytext align-middle sm:w-80 md:w-96 text-center px-8">Empowering your academic journey with real-time answers, up-to-date insights, and the future of higher education at your fingertips.</p>

          </div>
          <div className="flex flex-col items-center justify-center bg-gray-50 p-4 rounded-lg shadow-md w-fit">
            <p className="text-md font-semibold text-primdark mb-4">Prompt Suggestions</p>
            <ul className="w-full space-y-3">
              {
                prompts.map((prompt, index) => (
                  <li key={index}
                  disabled = {loading}
                  onClick={() => handlePromptClick(prompt.title)}
                  className=" cursor-pointer flex justify-between items-center bg-white border border-gray-200 rounded-lg shadow-sm px-4 py-2 hover:bg-gray-100 transition-all">
                    <span className="text-gray-800 font-medium text-sm">{prompt.title}</span>
                  </li>
                ))
              }
            </ul>
          </div>

        </div>

      }
      {chatText.length > 0 &&
        <ul className=" w-screen px-2 sm:px-40 lg:px-64 xl:px-72 overflow-y-auto max-h-[calc(100vh-160px)]">
          {chatText.map((messagePair, index) => {
            return (
              <div key={index} className="w-full flex flex-col">

                <div className="m-2  flex justify-end">
                  <li className="text-white text-right px-4 py-2 rounded-lg bg-primdark text-[20px] lg:text-[16px] w-fit ">
                    {messagePair.user}
                  </li>
                </div>
                <div className="m-2 flex justify-start">
                  <li className="text-black text-left px-4 py-2 rounded-lg bg-white text-[20px] lg:text-[16px] w-fit">
                    <ReactMarkdown
                      components={{
                        a: ({ href, children }) => (
                          <a
                            href={href}
                            className="text-blue-500 underline hover:text-blue-700 font-bold"
                            target="_blank"
                            rel="noopener noreferrer" // Safe for external links
                          >
                            {children}
                          </a>
                        ),
                      }}
                    >
                      {messagePair.bot}</ReactMarkdown>
                  </li>
                </div>

              </div>

            );
          })}
        </ul>
      }
    </div>
  )
}

export default Chat
