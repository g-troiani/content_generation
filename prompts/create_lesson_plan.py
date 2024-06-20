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

1. Analyze the main topic and consider its broad applications and relevance. Write your analysis in this section.
2. Identify the key components and sub-topics that are essential for a comprehensive understanding of the main topic. List these components, with each component on a new line.
3. Create a structured lesson plan that logically progresses through the key components you identified. For each component, provide the following:
   a. A brief explanation of the component.
   b. Ideas for making the explanation engaging and accessible to a non-expert audience.
4. Review your lesson plan and ensure that each component is explained in a way that is informative, interesting, and suitable for a broad audience. Write your review in this section.

Output the final lesson plan in a structured format with clear headings for each main component.

Remember, your goal is to create a lesson plan that effectively educates an audience unfamiliar with the subject, so prioritize clarity, engagement, and logical progression throughout the lesson.
    """}
  ]
)

print(completion.choices[0].message)
