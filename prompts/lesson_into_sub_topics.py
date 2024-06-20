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

1. Carefully review the provided lesson plan and identify the main components that make up the overall topic.
2. For each main component, brainstorm the specific sub-topics that need to be addressed to fully explain that component.
3. Ensure that each sub-topic is focused and can be adequately covered within a short video script format.
4. Consider the logical flow of information from one sub-topic to the next, making sure that each builds upon the previous one.
5. Organize the sub-topics in a clear and structured manner under each main component heading.

Output the sub-topics in a structured format under each main component heading.
    """}
  ]
)

print(completion.choices[0].message)
