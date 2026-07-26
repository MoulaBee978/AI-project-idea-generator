import React from 'react'

export default function ProjectCard({project}:{project:any}){
  return (
    <div className="glass p-6 rounded-lg">
      <div className="flex items-center justify-between mb-3">
        <h3 className="text-2xl font-semibold">{project.title}</h3>
        <span className="text-sm text-gray-300">{project.estimated_time}</span>
      </div>

      <p className="text-gray-300 mb-3"><strong>Problem:</strong> {project.problem_statement}</p>
      <p className="text-gray-300 mb-3"><strong>Objective:</strong> {project.objective}</p>

      <div className="grid grid-cols-2 gap-4">
        <div>
          <h4 className="font-medium">Key Features</h4>
          <ul className="list-disc list-inside text-gray-300">
            {project.key_features?.map((k:string,i:number)=> <li key={i}>{k}</li>)}
          </ul>
        </div>
        <div>
          <h4 className="font-medium">Required Technologies</h4>
          <ul className="list-disc list-inside text-gray-300">
            {project.required_technologies?.map((k:string,i:number)=> <li key={i}>{k}</li>)}
          </ul>
        </div>
      </div>

      <div className="mt-4 text-sm text-gray-400">
        <p><strong>Why useful:</strong> {project.why_useful}</p>
        <p><strong>Recommended Stack:</strong> {project.recommended_stack}</p>
        <p><strong>Best For:</strong> {project.best_suitable_for}</p>
      </div>
    </div>
  )
}
