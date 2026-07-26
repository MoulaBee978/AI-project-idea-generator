import os
import httpx
from typing import Optional


class GeminiClient:
    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY is required in environment")
        # model name; user can set GEMINI_MODEL in env
        self.model = model or os.environ.get("GEMINI_MODEL", "gemini-3.1-flash-lite")
        # base url for generative API
        self.base_url = os.environ.get("GEMINI_BASE_URL", "https://generative.googleapis.com")

    def generate(self, prompt: str, temperature: float = 0.2, max_tokens: int = 800) -> str:
        """Call the Gemini API via REST using an API key.

        Uses the Google AI Studio / v1beta models endpoint.
        Model name can be configured via GEMINI_MODEL.
        """
        # Use the correct Gemini API endpoint (v1)
        url = f"https://generativelanguage.googleapis.com/v1/models/{self.model}:generateContent"
        params = {"key": self.api_key}
        payload = {
            "contents": [{
                "parts": [{"text": prompt}]
            }],
            "generationConfig": {
                "temperature": temperature,
                "maxOutputTokens": max_tokens,
                "topP": 0.95,
                "topK": 40,
            }
        }

        with httpx.Client(timeout=60.0) as client:
            resp = client.post(url, json=payload, params=params)
            resp.raise_for_status()
            data = resp.json()

        # Extract text from the Gemini API response format
        if isinstance(data, dict):
            candidates = data.get("candidates", [])
            if candidates:
                content = candidates[0].get("content", {})
                parts = content.get("parts", [])
                if parts:
                    texts = [p.get("text", "") for p in parts if isinstance(p, dict)]
                    return "".join(texts)

        # Fallback: return raw JSON string
        return str(data)
