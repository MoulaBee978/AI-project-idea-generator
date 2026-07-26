from backend.prompts.idea_prompt import get_prompt_template
from backend.utils.output_parser import JSONOutputParser
from backend.services.gemini_client import GeminiClient
from typing import List
import os


class IdeaChain:
    def __init__(self, model_name: str = None):
        # Use Gemini client for remote generation
        api_key = os.environ.get("GEMINI_API_KEY")
        model = model_name or os.environ.get("GEMINI_MODEL", "gemini-1.5-pro")
        self.client = GeminiClient(api_key, model)
        self.prompt = get_prompt_template()
        self.memory = []  # Simple list to store chat history
        self.parser = JSONOutputParser()

    async def run(self, domain: str, language: str, tech_stack: str, difficulty: str) -> List[dict]:
        input_vars = {
            "domain": domain,
            "language": language,
            "tech_stack": tech_stack,
            "difficulty": difficulty,
        }

        # Format prompt using LangChain PromptTemplate
        prompt_text = self.prompt.format(**input_vars)

        # Include conversation history if any
        history_text = ""
        if self.memory:
            parts = []
            for entry in self.memory[-5:]:  # Keep last 5 exchanges
                parts.append(str(entry))
            history_text = "\n".join(parts)

        full_prompt = (history_text + "\n\n" + prompt_text) if history_text else prompt_text

        # Call Gemini client
        result_text = self.client.generate(full_prompt, temperature=0.2, max_tokens=1500)

        # Save to memory
        self.memory.append({"input": prompt_text, "output": result_text})

        parsed = self.parser.parse(result_text)
        return parsed
