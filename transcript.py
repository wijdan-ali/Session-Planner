from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from pyscript import window, document

import datetime



def getYoutubeId(link):
    arr = link.split("=")
    return arr[1]

def getTranscript(id):
    yt_api = YouTubeTranscriptApi()
    formatter = TextFormatter()
    raw = yt_api.fetch(id, languages=["en-US"])
    timestamped_output = ""
  
    
    for item in raw:
        start_seconds = item.start
        text = item.text
        
        # 1. Convert seconds to a human-readable HH:MM:SS format
        # This uses the datetime library's timedelta to format the seconds.
        time_format = str(datetime.timedelta(seconds=int(start_seconds)))
        
        # 2. Append the formatted time and text to the output string
        timestamped_output += f"[{time_format}] {text}\n"
        

   

getTranscript(getYoutubeId("https://www.youtube.com/watch?v=iwWcZ3rT1ig"))



