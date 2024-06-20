#######################################################################
# create_lesson_plan_prompt.py
#######################################################################

from openai import OpenAI
client = OpenAI()

User_Topic = input("Enter the main topic: ")

completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are an engaging and creative content creator, skilled at transforming complex topics into captivating short-video scripts for social media platforms like TikTok, Instagram, and YouTube Shorts."},
    {"role": "user", "content": f"""
The user has specified the topic: {User_Topic}. Your task is to identify the most important components of this topic and create a lesson plan that can educate an audience unfamiliar with the subject. The lesson plan should break down the topic into specific, manageable aspects, each designed to fit within a short video format. Ensure that each component is engaging, informative, and suitable for a broad audience.

Here are the steps to follow:

1. Understand the main topic and its broad applications.
2. Identify the key components and sub-topics that are essential for a comprehensive understanding.
3. Create a structured lesson plan that logically progresses through these components.
4. Ensure that each component is explained in a way that is accessible and interesting to a non-expert audience.

Output the final lesson plan in a structured format with clear headings for each main component.
    """}
  ]
)

print(completion.choices[0].message)
