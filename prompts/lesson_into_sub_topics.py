#######################################################################
# break_down_lessons_into_sub_topics_prompt.py
#######################################################################

from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are an engaging and creative content creator, skilled at transforming complex topics into captivating short-video scripts for social media platforms like TikTok, Instagram, and YouTube Shorts."},
    {"role": "user", "content": """
Based on the lesson plan for {User_Topic}, break down each main component into specific sub-topics that need to be covered to explain the topic thoroughly. Each sub-topic should be designed to fit within a short video format, making sure to capture the audience's attention and convey essential information clearly and engagingly.

Here are the steps to follow:

1. Review the lesson plan and identify the main components.
2. For each component, list the sub-topics that need to be explained to provide a complete understanding.
3. Ensure that each sub-topic is manageable in size and suitable for a short video script.
4. Maintain a logical flow from one sub-topic to the next, building upon the previous information.

Output the sub-topics in a structured format under each main component heading.
    """}
  ]
)

print(completion.choices[0].message)
