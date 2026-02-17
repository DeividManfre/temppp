import yaml

class ToonLoader:
    def __init__(self, path: str):
        with open(path, "r", encoding="utf-8") as f:
            self.data = yaml.safe_load(f)

    def system_prompt(self) -> str:
        p = self.data["persona"]
        return (
            f"Você é {p['name']}.\n"
            f"Estilo: {p['style']}.\n"
            f"Regras:\n" + "\n".join(f"- {r}" for r in p["rules"])
        )