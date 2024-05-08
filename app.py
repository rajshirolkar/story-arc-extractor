from anthropic import Anthropic
import json
import re
from pprint import pprint
import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import List

from collections import defaultdict
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer


load_dotenv()
client = Anthropic(
    api_key=os.environ["ANTHROPIC_API_KEY"],
)

class StoryArc(BaseModel):
    label: str
    description: str
    characters: List[str]
    themes: List[str]

class TranscriptAnalysis(BaseModel):
    story_arcs: List[StoryArc] = Field(..., alias='story_arcs')


transcripts_dir = 'transcripts'
files = os.listdir(transcripts_dir)
files.sort()
with open(os.path.join(transcripts_dir, files[0]), 'r') as file:
    EPISODE_TRANSCRIPT = file.read()

message = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=1024,
    temperature=0,
    system="You are good at extracting story arcs from transcript of TV episodes. You will be a given a transcript of an episode. Your task is to extract the main story arcs from this episode. A story arc is a narrative thread that runs through part or all of the episode, involving certain characters and exploring certain themes. An arc has a beginning, middle and end. It will often center around a conflict or challenge that the characters need to overcome. \n\nFor example, in an episode of Friends, one story arc might be:\n- Joey and Chandler centers around a humorous fight over a chair. The conflict begins when Chandler leaves the room for a moment and Joey takes his seat. When Chandler returns and demands the seat back, Joey refuses, leading to a series of tit-for-tat pranks between the two. The situation escalates comically when Joey decides to make a point about not sharing by wearing all of Chandler's clothes at once, declaring, \"Look at me, I'm Chandler. Could I BE wearing any more clothes?\" This is done as a form of exaggerated revenge for Chandler hiding Joey's underwear, and it leads to a memorable and funny moment involving physical comedy and slapstick humor.\n\nPlease carefully read through the transcript and identify the main story arcs. For each one, think about:\n<scratchpad>\n- What is the key conflict or challenge driving this arc? How is it set up and how is it resolved?\n- Which characters are most central to this arc? What role do they each play?\n- What deeper themes, if any, are explored through this storyline? \n</scratchpad>\n\nThen, output the story arcs in the following JSON format:\n\n<example>\n[\n  {\n    \"label\": \"Joey and Chandler's Fight\",\n    \"description\": \"Joey and Chandler bicker over a chair leading to escalating pranks including Joey wearing all of Chandler's clothes as an act of revenge.\",\n    \"characters\": [\"Joey\", \"Chandler\"],\n    \"themes\": [\"Friendship\", \"Conflict\", \"Petty revenge\"]\n  },\n  ...\n]\n</example>\n\n \n\nMake sure the story arc objects are printed in valid JSON format. Only include the valid JSON and do not include any other text. I just want the JSON from you.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"\n\n<episode_transcript>\n{EPISODE_TRANSCRIPT}\n</episode_transcript>\n\n"
                }
            ]
        }
    ]
).content[0].text
print(message)

def extract_json(response):
    json_start = response.index("[")
    json_end = response.rfind("]")
    return json.loads(response[json_start:json_end + 1])

json_output = extract_json(message)
print("JSON Output:")
pprint(json_output)

transcript_analysis = TranscriptAnalysis(story_arcs=json_output)

for arc in transcript_analysis.story_arcs:
    print(arc.label)  