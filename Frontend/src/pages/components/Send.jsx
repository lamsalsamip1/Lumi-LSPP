import {  useState } from "react";
import { send } from "../../assets"
import useSendMessage from "../../hooks/useSendBotMessage";

const Send = () => {
  const [message,setMessage]=useState("")
  
  const {loading,sendMessage}= useSendMessage();

	const handleSubmit=async(e)=>{
		e.preventDefault();
		if(!message) return;
		await sendMessage(message);
		setMessage("");
	}


  return (
    <form className='px-2 sm:px-40 lg:px-64 xl:px-72 my-3 w-screen z-10 ' onSubmit={handleSubmit}>
			<div className='w-full relative'>
				<input
					type='text'
					className='border text-sm rounded-lg block  p-5 lg:p-2.5  w-full bg-navbg border-primary text-black outline-blue-500'
					placeholder='Ask Lumi for the imformation you need'
					value={message}
					onChange={(e)=>setMessage(e.target.value)}
				/>
				<button 
					disabled={loading}
					type='submit' className='absolute inset-y-0 end-0 flex items-center pe-3'
				>
					{loading?<span>Loading</span>:<img src={send} />}
				</button>
			</div>
		</form>
  )
}

export default Send
