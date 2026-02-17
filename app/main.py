from fastapi import FastAPI
from app.schemas import ChatRequest
from app.core.session import SessionManager
from app.rag.vectorstore import VectorStore
from app.rag.retriever import Retriever
from app.rag.context_builder import ContextBuilder
from app.llm.chatgpt import ChatGPT
from app.core.observability import Observability

import yaml

app = FastAPI()

# preciso colocar dentro de um .env
sessions = SessionManager()
store = VectorStore()
retriever = Retriever(store)
context_builder = ContextBuilder()
llm = ChatGPT()
obs = Observability()


#colocar modulo de leitura em um script ceparado dentro de uma classe
with open("/app/data/toon/default.yml", "r", encoding="utf-8") as f:
    TOON = yaml.safe_load(f)

def build_toon_system_prompt() -> str:
    persona = TOON.get("persona", {})
    rules = persona.get("rules", [])
    return (
        f"Você é {persona.get('name', 'Assistente')}.\n"
        f"Estilo: {persona.get('style', 'neutro')}.\n"
        f"Regras:\n" + "\n".join(f"- {r}" for r in rules)
    )

@app.post("/chat")
def chat(req: ChatRequest):
    session_id = req.session_id or sessions.create()

    retrieved = retriever.retrieve(req.message)
    system_prompt = context_builder.build(build_toon_system_prompt(), retrieved)

    history = sessions.get(session_id)
    messages = [{"role": "system", "content": system_prompt}] + history
    messages.append({"role": "user", "content": req.message})

    answer = llm.chat(messages)

    sessions.append(session_id, "user", req.message)
    sessions.append(session_id, "assistant", answer)

    obs.log(req.message, answer)

    return {"session_id": session_id, "answer": answer}
