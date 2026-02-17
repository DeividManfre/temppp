from crewai import Agent, Task, Crew

class Observability:
    def log(self, question: str, answer: str):
        agent = Agent(
            role="Observer",
            goal="Monitorar qualidade das respostas",
            backstory="Audita interações do chatbot"
        )

        task = Task(
            description=f"Pergunta: {question}\nResposta: {answer}",
            expected_output="Registro avaliado",
            agent=agent
        )

        Crew(agents=[agent], tasks=[task]).kickoff()