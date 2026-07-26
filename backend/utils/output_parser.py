import json
from typing import List
from backend.models.project_models import ProjectIdea


def _find_json_array(text: str) -> str:
    text = text.strip()
    bracket_stack = []
    start = None
    for idx, ch in enumerate(text):
        if ch == '[' and start is None:
            start = idx
            bracket_stack.append(ch)
            continue
        if start is not None:
            if ch == '[':
                bracket_stack.append(ch)
            elif ch == ']':
                bracket_stack.pop()
                if not bracket_stack:
                    return text[start: idx + 1]
    return text


class JSONOutputParser:
    """Parse JSON produced by the LLM and validate into ProjectIdea models.

    This parser will extract an array from wrapped model output and validate entries.
    """

    def parse(self, text: str) -> List[dict]:
        candidate = _find_json_array(text)
        try:
            data = json.loads(candidate)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON from model: {e} | raw: {text}")

        if not isinstance(data, list):
            raise ValueError("Expected a JSON array of project objects")

        parsed = []
        for idx, item in enumerate(data):
            if not isinstance(item, dict):
                raise ValueError(f"Project at index {idx} is not an object")
            try:
                proj = ProjectIdea.parse_obj({
                    "title": item.get("title", "Untitled Project"),
                    "problem_statement": item.get("problem_statement", ""),
                    "objective": item.get("objective", ""),
                    "why_useful": item.get("why_useful", ""),
                    "required_technologies": item.get("required_technologies", []),
                    "recommended_stack": item.get("recommended_stack", ""),
                    "key_features": item.get("key_features", []),
                    "learning_outcomes": item.get("learning_outcomes", []),
                    "future_enhancements": item.get("future_enhancements", []),
                    "estimated_time": item.get("estimated_time", "2-6 weeks"),
                    "best_suitable_for": item.get("best_suitable_for", "Portfolio"),
                })
                parsed.append(proj.dict())
            except Exception as e:
                raise ValueError(f"Invalid project object at index {idx}: {e}")

        return parsed
