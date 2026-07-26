import React, { useState } from 'react'

const DOMAINS = ["Artificial Intelligence","Machine Learning","Healthcare","Education","Cybersecurity","IoT","Agriculture","Finance","E-Commerce","Web Development"]
const LANGS = ["Python","Java","JavaScript","TypeScript","C++","Go","Kotlin"]
const STACKS = ["MERN","React","FastAPI","Django","Spring Boot","Flutter","LangChain","TensorFlow","Node.js"]
const DIFFICULTIES = ["Beginner","Intermediate","Advanced"]

export default function InputForm({onGenerate, loading}:{onGenerate:any, loading:boolean}){
  const [domain, setDomain] = useState(DOMAINS[0])
  const [language, setLanguage] = useState(LANGS[0])
  const [techStack, setTechStack] = useState(STACKS[0])
  const [difficulty, setDifficulty] = useState(DIFFICULTIES[0])

  const submit = (e:React.FormEvent) =>{
    e.preventDefault()
    onGenerate({domain, language, tech_stack: techStack, difficulty})
  }

  return (
    <form onSubmit={submit} className="space-y-4">
      <div>
        <label className="block text-sm text-gray-300">Domain of Interest</label>
        <select value={domain} onChange={e=>setDomain(e.target.value)} className="w-full mt-1 p-2 rounded bg-transparent border">
          {DOMAINS.map(d=> <option key={d} value={d}>{d}</option>)}
        </select>
      </div>

      <div>
        <label className="block text-sm text-gray-300">Programming Language</label>
        <select value={language} onChange={e=>setLanguage(e.target.value)} className="w-full mt-1 p-2 rounded bg-transparent border">
          {LANGS.map(d=> <option key={d} value={d}>{d}</option>)}
        </select>
      </div>

      <div>
        <label className="block text-sm text-gray-300">Technology Stack</label>
        <select value={techStack} onChange={e=>setTechStack(e.target.value)} className="w-full mt-1 p-2 rounded bg-transparent border">
          {STACKS.map(d=> <option key={d} value={d}>{d}</option>)}
        </select>
      </div>

      <div>
        <label className="block text-sm text-gray-300">Difficulty</label>
        <select value={difficulty} onChange={e=>setDifficulty(e.target.value)} className="w-full mt-1 p-2 rounded bg-transparent border">
          {DIFFICULTIES.map(d=> <option key={d} value={d}>{d}</option>)}
        </select>
      </div>

      <div>
        <button disabled={loading} className="w-full py-2 bg-gradient-to-r from-indigo-600 to-pink-600 rounded text-white">{loading? 'Generating...':'Generate Ideas'}</button>
      </div>
    </form>
  )
}
