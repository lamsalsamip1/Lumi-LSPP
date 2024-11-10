
import { Route, Routes } from 'react-router-dom'
import Chatbot from './pages/Chatbot'
import News from './pages/News'

function App() {

  return (
    <div className='bg-bg'>
      <Routes>
        <Route path='/' element={<Chatbot />} />
        <Route path='/news' element={<News />} />
      </Routes>
    </div>
  )
}

export default App
