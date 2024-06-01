from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List

class Topic(BaseModel):
  title: str = Field(description="Title of topic")
  points: List[str] = Field(description="Array of bullet points for the topic title")

class VideoInfo(BaseModel):
  main_topic: str = Field(description="Main topic that is being talked about")
  summary: str = Field(description="Summary about this topic in 60 words")
  topics: List[Topic] = Field(description="Array of topics discussed")