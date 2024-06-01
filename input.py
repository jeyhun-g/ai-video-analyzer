import os.path

def get_input():
  print("Input path to the video file")
  video_path = input("Path: ")
  if not os.path.isfile(video_path):
    print('Not a valid path')
    exit(1)
  return video_path