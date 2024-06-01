from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from .models import VideoInfo

import os


SYSTEM_TEMPLATE = """Analyze following text. Extract the main topic that it is talking about and create a 60 word summary about this topic from the text. Also get the main topics and list 3-4 bullet points about what is being mentioned about these topics

Format the response in {format_instructions}

Text: {text}"""


class VideoAnalyzerGPT():
  def __init__(self):
    parser = PydanticOutputParser(pydantic_object=VideoInfo)
    prompt_template = PromptTemplate(
        template=SYSTEM_TEMPLATE,
        input_variables=["text"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )
    model = ChatOpenAI(model="gpt-4o-2024-05-13", openai_api_key=os.environ['OPENAI_API'])

    self.__chain = prompt_template | model | parser
  
  def run(self, text):
    self.__output = self.__chain.invoke({ "text": text })
    return self
  
  def prettyprint(self):
    print("Main Topic:")
    print(self.__output.main_topic)
    print()

    print("Summary:")
    print(self.__output.summary)
    print()

    print("Topics discussed:")
    for topic in self.__output.topics:
      print(f"\tTopic: {topic.title}")
      print(f"\tPoints:")
      for point in topic.points:
        print(f"\t\t- {point}")
      print()