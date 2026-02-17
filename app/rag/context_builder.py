class ContextBuilder:
    def build(self, toon_prompt: str, retrieved: str) -> str:
        return f"""
{toon_prompt}

CONTEXTO RECUPERADO:
{retrieved}
"""