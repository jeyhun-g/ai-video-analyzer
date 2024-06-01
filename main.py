from dotenv import load_dotenv
load_dotenv()

from input import get_input
from whisperwrapper import WhisperWrapper
from analyzer import VideoAnalyzerGPT

welcome_message = """
Welcome to video summarizer
    - Get main topic the video is about
    - Get a summary
    - Get few subtopics mentioned in the video
"""

print(welcome_message)

# Get the video link
video_path = get_input()

# Transcribe
transcript = WhisperWrapper(filename=video_path).transcribe()

# Analyze
analyzer = VideoAnalyzerGPT()
analyzer.run(transcript).prettyprint()
