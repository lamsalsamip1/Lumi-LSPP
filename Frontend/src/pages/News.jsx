
const News = () => {
    // Sample news data (you can replace this with your actual data source)
    const newsItems = [
        {
            title: "BCA Re-entrance Result 2081 - TU",
            url: "https://edusanjal.com/news/bca-re-entrance-result-tu/",
            description: "Tribhuvan University Faculty of Humanities and Social Sciences (TUFoHSS) has released the Bachelor of Computer Application (BCA) re-entrance examination results for the academic year 2081.",
            date: "November 20, 2024",
            category: "Technology",
            readTime: "5 min read"
        },
        {
            title: "The British College announces Career Fest 2024",
            url: "https://www.educatenepal.com/news/detail/the-british-college-announces-career-fest-2024",
            description: "The British College, in collaboration with Growth Sellers, is hosting Career Fest 2024, connecting job seekers with over 50 leading companies.",
            date: "November 11, 2024",
            category: "Career Event",
            readTime: "7 min read"
        },
        {
            title: "Top 10 IT Colleges in Nepal: IT Courses, Fees, Scholarships",
            url: "https://meroupdate.com/university/top-10-it-colleges-in-nepal/?utm_source=chatgpt.com",
            description: "Discover Nepal’s top 10 IT colleges, featuring course offerings, fee structures, scholarship opportunities, and admission processes for aspiring IT professionals.",
            date: "November 2, 2024",
            category: "Education",
            readTime: "5 min read"
        },
        {
            title: "BE/BArch. Entrance Result 2081",
            url: "https://entrance.ioe.edu.np/notice/download?filename=BEResult2081.pdf&contentType=pdf",
            description: "Tribhuvan University's Institute of Engineering has released the results for the BE/BArch entrance examinations for the year 2081. Read more to check your results.",
            date: "September 7, 2024",
            category: "Technology",
            readTime: "2 min read"
        }
    ];

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
                                        <span className="px-3 py-1 bg-blue-100 text-blue-800 text-sm font-medium rounded-full mr-3">
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
                                            className="inline-flex items-center text-blue-600 hover:text-blue-800 font-medium"
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
