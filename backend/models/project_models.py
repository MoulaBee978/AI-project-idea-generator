from pydantic import BaseModel
from typing import List


class ProjectIdea(BaseModel):
    title: str
    problem_statement: str
    objective: str
    why_useful: str
    required_technologies: List[str]
    recommended_stack: str
    key_features: List[str]
    learning_outcomes: List[str]
    future_enhancements: List[str]
    estimated_time: str
    best_suitable_for: str
