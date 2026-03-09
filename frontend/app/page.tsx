"use client"

import { useState } from "react"

export default function Home() {

  const [topic, setTopic] = useState("")
  const [results, setResults] = useState<any[]>([])

  const search = async () => {

    const response = await fetch("http://127.0.0.1:8000/recommend", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ topic })
    })

    const data = await response.json()

    setResults(data.recommendations)
  }

  return (
    <div className="min-h-screen flex flex-col items-center bg-gray-100 p-10">

      <h1 className="text-4xl font-bold text-blue-600 mb-8">
        AI Study Resource Recommender
      </h1>

      <div className="flex gap-4 mb-10">

        <input
          type="text"
          placeholder="Enter topic..."
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
          className="border rounded-lg px-4 py-2 w-80 focus:ring-2 focus:ring-blue-400 outline-none"
        />

        <button
          onClick={search}
          className="bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition"
        >
          Search
        </button>

      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 w-full max-w-4xl">

        {results.map((item, index) => (

          <div
            key={index}
            className="bg-white shadow-md rounded-xl p-5 hover:shadow-xl transition"
          >

            <h2 className="text-xl font-semibold mb-2">
              {item.title}
            </h2>

            <p className="text-sm text-gray-500 mb-3">
              Type: {item.resource_type}
            </p>

            <a
              href={item.resource_link}
              target="_blank"
              className="text-blue-500 hover:underline"
            >
              Open Resource →
            </a>

          </div>

        ))}

      </div>

    </div>
  )
}