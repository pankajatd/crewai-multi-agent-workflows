import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

# 1. Load your API keys
load_dotenv()

@CrewBase
class BlogCrew():
    # These must be indented inside the class
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['research_agent'], # type: ignore[index]
            tools=[SerperDevTool()],
            verbose=True
        )

    @agent # Added missing decorator
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config['writer_agent'], # type: ignore[index]
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],# type: ignore[index]
            agent=self.researcher()
        )

    @task # Added missing decorator
    def blog_task(self) -> Task:
        return Task(
            config=self.tasks_config['blog_task'],# type: ignore[index]
            agent=self.writer() # Fixed: Writer agent should do the blog task
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents, # CrewBase automatically provides this list
            tasks=self.tasks,   # CrewBase automatically provides this list
            process=Process.sequential,
            verbose=True
        )

# This must be at the very far left (no spaces)
if __name__ == '__main__':
    blog_crew = BlogCrew()
    # Note: Ensure your topic matches what your YAML expects
    result = blog_crew.crew().kickoff(inputs={"topic": "The Future of Electric Vehicles"})
    print(result)