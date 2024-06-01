import sys
import platform
from constants import WORKDIR

class WhisperWrapper:
  # video file to transcribe 
  __filename: str

  def __init__(self, filename):
    self.__filename = filename

  def transcribe(self):
    platform_name = sys.platform
    arch = platform.processor()
    if platform_name == 'darwin' and 'arm' in arch:
      import mlx_whisper
      return mlx_whisper.transcribe(self.__filename)["text"]
    else:
      print(f"{platform} / {arch} not supported")