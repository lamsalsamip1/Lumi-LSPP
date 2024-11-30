import { newsItems } from "../constants"


const News = () => {

    return (
        <div className="h-screen overflow-hidden">
            <div className="h-full flex flex-col">
                <h2 className="text-4xl font-bold text-center py-6 bg-gray-100">
                    Latest News Updates
                </h2>
                <div className="flex-grow overflow-y-auto px-4 py-6">
                    <div className="max-w-3xl mx-auto space-y-8">
                        {newsItems.map((news, index) => (
                            <div 
                                key={index} 
                                className="bg-white rounded-xl shadow-lg overflow-hidden transition-all duration-300 transform hover:-translate-y-2 hover:shadow-2xl"
                            >
                                <div className="p-6">
                                    <div className="flex items-center mb-4">
                                        <span className="px-3 py-1 bg-teal text-white text-sm font-medium rounded-full mr-3">
                                            {news.category}
                                        </span>
                                        <span className="text-gray-500 text-sm">
                                            {news.readTime}
                                        </span>
                                    </div>
                                    <h3 className="text-2xl font-bold text-gray-900 mb-3">
                                        {news.title}
                                    </h3>
                                    <p className="text-gray-600 mb-4">
                                        {news.description}
                                    </p>
                                    <div className="flex justify-between items-center">
                                        <span className="text-gray-500 text-sm">
                                            {news.date}
                                        </span>
                                        <a 
                                            href={news.url} 
                                            target="_blank" 
                                            rel="noopener noreferrer"
                                            className="inline-flex items-center text-teal hover:text-blue-800 font-medium"
                                        >
                                            Read More
                                            <svg 
                                                xmlns="http://www.w3.org/2000/svg" 
                                                className="h-5 w-5 ml-2" 
                                                viewBox="0 0 20 20" 
                                                fill="currentColor"
                                            >
                                                <path 
                                                    fillRule="evenodd" 
                                                    d="M10.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L12.586 11H5a1 1 0 110-2h7.586l-2.293-2.293a1 1 0 010-1.414z" 
                                                    clipRule="evenodd" 
                                                />
                                            </svg>
                                        </a>
                                    </div>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            </div>
        </div>
    )
}

export default News
