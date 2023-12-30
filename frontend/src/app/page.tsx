"use client"; 
import React from 'react'
import axios from 'axios'
import { useState } from 'react';


export default function Home() {
  const [response, setResponse] = useState("")
  const [password, setPassword] = useState("")
  const [hasError, setHasError] = useState(false)

  return (
    <div>
      <h1 className="text-center">Sam's Auto Home</h1>
      <div className="h-56 grid grid-cols-3 gap-4 content-start">
        <div className="bg-gray-900 flex flex-col justify-center items-center">
          <h1 className="text-center">Garage Door</h1>
          <form onSubmit={triggerGarageRequest}>
            <input className="password" type="password" placeholder="Password" value={password} onChange={handleChange}></input>
            <input className="ml-1 bg-blue-500 hover:bg-blue-700 text-white font-bold py-0.4 px-4 rounded" type="submit" value="Trigger" />
            {getResponseText()}
          </form>
        </div>
      </div>
    </div>
  )

  async function triggerGarageRequest(event: any) {
    event.preventDefault()
    try{
      setResponse("")
      const res = await axios.post(`http://localhost:8000/garage`, {'password': password})
      setResponse("Garage Door Switch Triggered")
      setHasError(false)
    }
    catch(error: any) {
      if (error.response) {
        if(error.response.status == 401){
          setResponse("Invalid Password")
          setHasError(true)
        }
        else if(error.response.status == 500){
          setResponse("Error triggering the garage switch")
          setHasError(true)
        }
        else{
          setResponse("There was an error")
          setHasError(true)
        }
      }
    }
  }

  function handleChange(event: any){
    setPassword(event.target.value)
  }

  function getResponseText(){
    if (hasError) {
      return (
        <h1 className='response error'>{response}</h1>
      )
    }

    return (
      <h1 className='response success'>{response}</h1>
    )
  }
}
