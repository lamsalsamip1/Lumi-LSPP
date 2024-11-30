import { github, linkedin, lumi } from "../assets";
import { creators } from "../constants";

const Aboutus = () => {
    return (
        <div className="h-screen flex justify-center ">
            <div className="mt-40 mx-auto px-8 py-4 flex-col flex items-center w-fit rounded-xl h-fit bg-white/50 shadow-lg border-primdark gap-4">
                <p className="text-xl font-bold text-primdark flex gap-2 items-center">
                    <span>Creators of </span>
                    <img className="w-16" src={lumi} />
                </p>
                <ul>
                    {creators.map((creator) => {
                        return (
                            <li
                                key={creator.id}
                                className="text-gray-800 font-medium text-sm rounded-lg shadow-sm px-4 py-2 hover:bg-gray-100 transition-all"
                            >
                                <div className="flex flex-row justify-between gap-12 items-center">
                                    <p>{creator.name}</p>

                                    <div className="gap-2 p-2 flex flex-row ">
                                    <a href={creator.github} target="_blank" rel="noopener noreferrer">
                                        <img src={github} alt="github" className="w-6 h-6" />
                                    </a>
                                    <a href={creator.linkedin} target="_blank" rel="noopener noreferrer">
                                        <img src={linkedin} alt="github" className="w-6 h-6" />
                                    </a>
                                    </div>
                                </div>
                            </li>
                        );
                    })}
                </ul>
            </div>
        </div>
    );
}

export default Aboutus;
