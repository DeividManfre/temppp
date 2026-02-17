import redis
import uuid
import json
from app.core.config import settings

r = redis.from_url(settings.redis_url, decode_responses=True)

class SessionManager:
    def create(self) -> str:
        session_id = str(uuid.uuid4())
        r.set(session_id, json.dumps([]))
        return session_id

    def append(self, session_id: str, role: str, content: str):
        data = r.get(session_id)
        if data is None:
            history = []
        else:
            history = json.loads(data)

        history.append({"role": role, "content": content})
        r.set(session_id, json.dumps(history))

    def get(self, session_id: str):
        data = r.get(session_id)
        if data is None:
            r.set(session_id, json.dumps([]))
            return []
        return json.loads(data)
