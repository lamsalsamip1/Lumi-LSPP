
import { Route, Routes } from 'react-router-dom'
import Chatbot from './pages/Chatbot'
import News from './pages/News'
import Navbar from './pages/components/Navbar'

function App() {

  return (
    <div className='bg-bg h-screen overflow-hidden flex flex-col'>
      <Navbar />
      <Routes>
        <Route path='/' element={<Chatbot />} />
        <Route path='/news' element={<News />} />
      </Routes>
    </div>
  )
}

export default App
