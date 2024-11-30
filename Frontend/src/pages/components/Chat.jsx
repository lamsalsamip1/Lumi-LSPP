import { lumi, roboticon } from "../../assets";
import useChat from "../../zustand/useChat";
import ReactMarkdown from 'react-markdown';
import { prompts } from '../../constants';
import useSendMessage from "../../hooks/useSendBotMessage";
import { useEffect, useRef } from 'react';



const Chat = () => {
  const { chatText, setMessage } = useChat();
  const { setPromptClick} = useChat();
  const { loading, sendMessage } = useSendMessage();
  const messagesEndRef = useRef(null);

  useEffect(() => {
    if (messagesEndRef.current && chatText.length > 0) {
      messagesEndRef.current.scrollIntoView({ behavior: "smooth" });
    }
  }, [chatText]);
  


  const handlePromptClick = async (prompt) => {
    setMessage(prompt);
    setPromptClick(true);
    await sendMessage(prompt);
    setPromptClick(false);
    setMessage("");
  };

  return (
    <div className="w-screen h-screen flex flex-col">
      <div
    className="flex-grow overflow-y-auto max-h-[calc(100vh-80px)] px-2 sm:px-40 lg:px-64 xl:px-72 pt-[96px] mb-16"
  >

      {chatText?.length === 0 && (
        <div className="flex flex-col items-center justify-between gap-8">
          <div className="flex flex-col justify-center items-center flex-grow">
            <img src={roboticon} className="w-16 sm:w-20 md:w-24" />
            <div className="flex flex-row gap-2 justify-center items-center">
              <span className="font-bold text-gray-800 text-[16px] md:text-[20px] lg:text-[28px]">
                Chat with
              </span>
              <img src={lumi} className="w-16 md:w-20 lg:w-24" />
            </div>
            <p className="text-graytext align-middle sm:w-80 md:w-96 text-center px-8">
              Empowering your academic journey with real-time answers, up-to-date insights, and the future of higher education at your fingertips.
            </p>
          </div>
          <div className="flex flex-col items-center justify-center bg-gray-50 p-4 rounded-lg shadow-md w-fit">
            <p className="text-md font-semibold text-primdark mb-4">Prompt Suggestions</p>
            <ul className="w-full space-y-3">
              {prompts.map((prompt, index) => (
                <li
                  key={index}
                  disabled={loading}
                  onClick={() => handlePromptClick(prompt.title)}
                  className="cursor-pointer flex justify-between items-center bg-white border border-gray-200 rounded-lg shadow-sm px-4 py-2 hover:bg-gray-100 transition-all"
                  >
                  <span className="text-gray-800 font-medium text-sm">{prompt.title}</span>
                </li>
              ))}
            </ul>
          </div>
        </div>
      )}
      
      {chatText.length > 0 && (
          <ul className=" md:pt-8 pt-16">
            {chatText.map((messagePair, index) => (
              <div key={index} className="w-full flex flex-col">
                <div className="m-2 flex justify-end">
                  <li className="text-white text-right px-4 py-2 rounded-lg bg-primdark text-[16px] lg:text-[16px] w-fit">
                    {messagePair.user}
                  </li>
                </div>
                <div className="m-2 flex justify-start">
                  <li className="text-black text-left px-4 py-2 rounded-lg bg-white text-[16px] lg:text-[16px] w-fit">
                    <ReactMarkdown
                      components={{
                        a: ({ href, children }) => (
                          <a
                            href={href}
                            className="text-blue-500 underline hover:text-blue-700 font-bold"
                            target="_blank"
                            rel="noopener noreferrer"
                          >
                            {children}
                          </a>
                        ),
                      }}
                    >
                      {messagePair.assistant}
                    </ReactMarkdown>
                  </li>
                </div>
              </div>
            ))}
            <div ref={messagesEndRef} />
          </ul>
      )}
    </div>
      </div>
  );
};

export default Chat;