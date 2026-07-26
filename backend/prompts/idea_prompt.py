class PromptTemplate:
    """Lightweight wrapper for prompt templates."""
    def __init__(self, template: str):
        self.template = template
    
    def format(self, **kwargs):
        """Format template with variables."""
        return self.template.format(**kwargs)


IDEA_PROMPT_TEMPLATE = """You are an experienced software architect and mentor. Based on the user inputs, generate exactly THREE unique, practical, and non-generic software project ideas tailored to the user's preferences.

User Inputs:
- Domain: {domain}
- Programming Language: {language}
- Technology Stack: {tech_stack}
- Difficulty: {difficulty}

For each project, output a JSON object with these fields:
- title: Project title
- problem_statement: The problem it solves
- objective: What the project aims to achieve
- why_useful: Why this project is valuable
- required_technologies: Array of required tech
- recommended_stack: Stack recommendation
- key_features: Array of key features
- learning_outcomes: Array of what will be learned
- future_enhancements: Array of future ideas
- estimated_time: Estimated development time
- best_suitable_for: Best use case (Academic/Hackathon/Portfolio/Personal Learning)

CRITICAL: Return ONLY a valid JSON array with exactly 3 project objects. No markdown, no code blocks, no extra text. Start with [ and end with ]."""


def get_prompt_template() -> PromptTemplate:
    return PromptTemplate(IDEA_PROMPT_TEMPLATE)
