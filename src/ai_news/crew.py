from crewai import Agent, Crew, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

@CrewBase
class AiNews():
    """AiNews crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    llm = LLM(
        base_url='http://localhost:11434',
        model='ollama/llama3.2'
    )

    @agent
    def retrieve_news(self) -> Agent:
        return Agent(
            config=self.agents_config['retrieve_news'],
	        tools=[SerperDevTool()],
            llm=self.llm
        )

    @agent
    def review_curator(self) -> Agent:
        return Agent(
            config=self.agents_config['review_curator'],
            llm=self.llm
        )
        
    @agent
    def insight_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['insight_generator'],
            llm=self.llm
        )
    

    @task
    def retrieve_news_task(self) -> Task:
        return Task(config=self.tasks_config['retrieve_news_task'])

    @task
    def review_curator_task(self) -> Task:
        return Task(config=self.tasks_config['review_curator_task'])
    
    @task
    def insight_generator_task(self) -> Task:
        return Task(
            config=self.tasks_config['insight_generator_task'],
            output_file='articles/{dt}_feedback.md'.format(dt=datetime.now().strftime('%Y-%m-%d_%H-%M-%S')),
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AiNews crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            verbose=True,
        )
