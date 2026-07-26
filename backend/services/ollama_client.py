import os
from ollama import Ollama


class OllamaClient:
    def __init__(self, host: str = None, model: str = None):
        self.host = host or os.environ.get("OLLAMA_HOST", "http://localhost:11434")
        self.model = model or os.environ.get("OLLAMA_MODEL", "llama3")
        self.client = Ollama(host=self.host)

    def generate(self, messages, temperature: float = 0.2, max_tokens: int = 800):
        # messages: list of dicts {role: 'system'|'user', 'content': '...'}
        prompt = "\n".join([m["content"] for m in messages])
        resp = self.client.chat(model=self.model, messages=[{"role": "user", "content": prompt}], temperature=temperature)
        # Ollama client returns generator-like object or dict; normalize
        if isinstance(resp, dict) and "choices" in resp:
            return resp["choices"][0]["message"]["content"]
        return str(resp)
