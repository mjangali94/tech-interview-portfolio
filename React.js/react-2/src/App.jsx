import { useState } from 'react'
import viteLogo from '/vite.svg'
import './App.css'
import { Fragment } from "react"
import Header from "./components/Header"
import Entry from "./components/Entry"
import data from "./data"

function App() {
    const travelItems= data.map(entry => {
        return (
            <Entry entry={entry} />
            )})
       return (
           <>
               <Header />
               {travelItems}
           </>
           )
       }
export default App
