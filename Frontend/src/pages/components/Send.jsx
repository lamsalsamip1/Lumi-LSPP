import { send } from "../../assets"
import useSendMessage from "../../hooks/useSendBotMessage";
import useClearHistory from "../../hooks/useClearHistory";
import useChat from "../../zustand/useChat";


import CircularProgress from "@mui/material/CircularProgress";
import Box from "@mui/material/Box";

const Send = () => {
	const { message, setMessage } = useChat();
	const { promptClick } = useChat();
	const { loading, sendMessage } = useSendMessage();
	const { clearHistory, loadingc } = useClearHistory();

	const handleSubmit = async (e) => {
		e.preventDefault();
		if (!message) return;
		await sendMessage(message);
		setMessage("");
	}

	const ClearChat = async (e) => {
		e.preventDefault();
		await clearHistory();
		setMessage("");
		window.scrollTo({ top: 0, behavior: "smooth" });

	}

	return (
		<form className='px-2 sm:px-40 lg:px-64 xl:px-64 my-3 w-screen z-10 ' onSubmit={handleSubmit}>
			<div className='w-full relative flex gap-2 justify-center'>
				<div
					disabled={loadingc}
					onClick={ClearChat}
					className="bg-primary hover:bg-primdark cursor-pointer text-white text-[16px] lg:text-[16px] px-4 py-2 rounded-lg flex items-center justify-center">
					{loadingc ?
						<Box sx={{ display: "flex", justifyContent: "center" }}>
							<CircularProgress size="30px" />
						</Box>
						: <p>Clear</p>
					}

				</div>

				<input
					type='text'
					className='border text-sm rounded-lg block p-5 lg:p-2.5  w-full bg-navbg border-primary text-black outline-blue-500 lg:pr-12 pr-12'
					placeholder='Ask Lumi for the information you need'
					value={message}
					onChange={(e) => setMessage(e.target.value)}
				/>
				<button
					disabled={loading}
					type='submit' className='absolute inset-y-0 end-0 flex items-center pe-3 justify-center '
				>
					{loading || promptClick ?
						<Box sx={{ display: "flex", justifyContent: "center" }}>
							<CircularProgress size="30px" />
						</Box>
						: <img src={send} />}
				</button>
			</div>
		</form>
	)
}

export default Send
