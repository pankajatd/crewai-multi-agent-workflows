from typing import List
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, DirectoryReadTool, FileWriterTool, FileReadTool
from pydantic import BaseModel, Field
from dotenv import load_dotenv

_ = load_dotenv()

# Define the JSON output schema
class Content(BaseModel):
    title: str = Field(..., description="The title of the content.")
    body: str = Field(..., description="The main text or script of the content.")
    tags: List[str] = Field(..., description="Relevant keywords or hashtags.")

llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.7,
)
class Content(BaseModel):
    content_type: str = Field(...,
                              description="The type of content to be created (e.g., blog post, social media post, video)")
    topic: str = Field(..., description="The topic of the content")
    target_audience: str = Field(..., description="The target audience for the content")
    tags: List[str] = Field(..., description="Tags to be used for the content")
    content: str = Field(..., description="The content itself")
@CrewBase
class TheMarketingCrew():
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def head_of_marketing(self)->Agent:
        return Agent(
            config=self.agents_config['head_of_marketing'],# type: ignore[index]
            tools=[SerperDevTool(), ScrapeWebsiteTool(), DirectoryReadTool('resources/drafts'), FileWriterTool(), FileReadTool()],
            reasoning=True,
            inject_data=True, # Corrected
            llm=llm,
            allow_delegation=True,
            max_rpm=3
        )

    @agent
    def content_creator_social_media(self) -> Agent:
        return Agent(
            config=self.agents_config['content_creator_social_media'],# type: ignore[index]
            tools=[SerperDevTool(), ScrapeWebsiteTool(), DirectoryReadTool('resources/drafts'), FileWriterTool(), FileReadTool()],
            inject_data=True, # Corrected typo from 'date' to 'data'
            llm=llm,
            allow_delegation=True,
            max_iter=30,
            max_rpm=3
        )

    @agent
    def content_writer_blogs(self) -> Agent:
        return Agent(
            config=self.agents_config['content_writer_blogs'],# type: ignore[index]
            tools=[SerperDevTool(), ScrapeWebsiteTool(), DirectoryReadTool('resources/drafts/blogs'), FileWriterTool(), FileReadTool()],
            inject_data=True, # Corrected typo
            llm=llm,
            allow_delegation=True,
            max_iter=5,
            max_rpm=3
        )

    @agent
    def seo_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['seo_specialist'],# type: ignore[index]
            tools=[SerperDevTool(), ScrapeWebsiteTool(), DirectoryReadTool('resources/drafts'), FileWriterTool(), FileReadTool()],
            inject_data=True, # Corrected typo
            llm=llm,
            allow_delegation=True,
            max_iter=3,
            max_rpm=3
        )

    # --- TASKS ---
    @task
    def market_research(self) -> Task:
        return Task(config=self.tasks_config['market_research'], agent=self.head_of_marketing())# type: ignore[index]

    @task
    def prepare_marketing_strategy(self) -> Task:
        return Task(config=self.tasks_config['prepare_marketing_strategy'], agent=self.head_of_marketing())# type: ignore[index]

    @task
    def create_content_calendar(self) -> Task:
        return Task(
            config=self.tasks_config['create_content_calendar'],# type: ignore[index]
            agent=self.content_creator_social_media() # Fixed method name
        )

    @task
    def prepare_post_drafts(self) -> Task:
        return Task(config=self.tasks_config['prepare_post_drafts'], agent=self.content_creator_social_media(), output_json=Content)# type: ignore[index]

    @task
    def prepare_scripts_for_reels(self) -> Task:
        return Task(config=self.tasks_config['prepare_scripts_for_reels'], agent=self.content_creator_social_media(), output_json=Content)# type: ignore[index]

    @task
    def content_research_for_blogs(self) -> Task:
        return Task(config=self.tasks_config['content_research_for_blogs'], agent=self.content_writer_blogs())# type: ignore[index]

    @task
    def draft_blogs(self) -> Task:
        return Task(config=self.tasks_config['draft_blogs'], agent=self.content_writer_blogs(), output_json=Content)# type: ignore[index]

    @task
    def seo_optimization(self) -> Task:
        return Task(config=self.tasks_config['seo_optimization'], agent=self.seo_specialist(), output_json=Content)# type: ignore[index]

    @crew
    def marketingcrew(self) -> Crew:
        """Creates the Marketing crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            planning=True,
            planning_llm=llm
        )

if __name__ == "__main__":
    from datetime import datetime

    inputs = {
        "product_name": "AI Powered Excel Automation Tool",
        "target_audience": "Small and Medium Enterprises (SMEs)",
        "product_description": "A tool that automates repetitive tasks in Excel using AI, saving time and reducing errors.",
        "budget": "Rs. 50,000",
        "current_date": datetime.now().strftime("%Y-%m-%d"),
    }
    crew = TheMarketingCrew()
    crew.marketingcrew().kickoff(inputs=inputs)
    print("Marketing crew has been successfully created and run.")