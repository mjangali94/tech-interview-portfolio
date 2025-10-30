import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Header from "./components/Header"
import Main from "./components/Main"
import {createRoot} from "react-dom/client"
createRoot(document.getElementById('root')).render(
      <>
        <Header />
        <Main />
    </>
)

// export default App

