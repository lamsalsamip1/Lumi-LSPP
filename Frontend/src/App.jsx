
import { Route, Routes } from 'react-router-dom'
import Chatbot from './pages/Chatbot'
import News from './pages/News'
import Navbar from './pages/components/Navbar'
import Aboutus from './pages/Aboutus'

function App() {

  return (
    <div className='bg-bg h-screen overflow-hidden flex flex-col'>
      <Navbar />
      <Routes>
        <Route path='/' element={<Chatbot />} />
        <Route path='/news' element={<News />} />
        <Route path='/aboutus' element={<Aboutus />} />

      </Routes>
    </div>
  )
}

export default App
