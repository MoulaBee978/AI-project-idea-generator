import React, { useState } from 'react'
import axios from 'axios'
import InputForm from './components/InputForm'
import ProjectCard from './components/ProjectCard'

type Project = any

export default function App(){
  const [projects, setProjects] = useState<Project[]>([])
  const [loading, setLoading] = useState(false)

  const handleGenerate = async (payload:any) => {
    setLoading(true)
    try{
      const res = await axios.post('http://localhost:8000/api/generate-projects', payload)
      setProjects(res.data.projects || [])
    }catch(err){
      console.error(err)
      alert('Failed to generate ideas. See console for details.')
    }finally{
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen p-6">
      <div className="max-w-5xl mx-auto">
        <header className="mb-6">
          <h1 className="text-4xl font-semibold mb-2">AI Project Idea Generator</h1>
          <p className="text-gray-400">Get tailored software project ideas powered by LangChain + Gemini</p>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="col-span-1 glass p-6 rounded-lg">
            <InputForm onGenerate={handleGenerate} loading={loading} />
          </div>

          <div className="col-span-2">
            {loading && (
              <div className="glass p-6 rounded-lg mb-4">Generating ideas... ⏳</div>
            )}
            <div className="space-y-4">
              {projects.map((p:any, i:number) => (
                <ProjectCard key={i} project={p} />
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
