import os
from backend.chains.idea_chain import IdeaChain
from backend.utils.lcel_wrapper import estimate_time_via_lcel


class LangChainService:
    def __init__(self):
        model = os.environ.get("GEMINI_MODEL", "gemini-3.1-flash-lite")
        self.chain = IdeaChain(model_name=model)

    async def generate_ideas(self, domain: str, language: str, tech_stack: str, difficulty: str):
        # Primary chain run
        raw = await self.chain.run(domain=domain, language=language, tech_stack=tech_stack, difficulty=difficulty)

        # Post-process: ensure estimated_time exists using LCEL wrapper
        processed = []
        for item in raw:
            if not item.get("estimated_time"):
                item["estimated_time"] = estimate_time_via_lcel(difficulty, tech_stack)
            processed.append(item)

        return processed
