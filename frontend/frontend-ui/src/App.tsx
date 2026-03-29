import { useState } from 'react'
import './App.css'
import AppFlow from './pages/AppFlow'
import BurnMapLanding from './pages/BurnMapLanding'

function App() {
  const [view, setView] = useState<'landing' | 'app'>('landing')

  if (view === 'landing') {
    return <BurnMapLanding onLaunch={() => setView('app')} />
  }

  return <AppFlow onExit={() => setView('landing')} />
}

export default App
