#######################################################################
# high_level_and_detailed_script_creation_prompt.py
#######################################################################


from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are an engaging and creative content creator, skilled at transforming complex topics into captivating short-video scripts for social media platforms like TikTok, Instagram, and YouTube Shorts."},
    {"role": "user", "content": """
For the sub-topic '{Sub_Topic}' under the main topic '{User_Topic}', create a detailed script broken down into six parts with specific durations for each part. Each part should be designed to fit within a short video format, making sure to engage the audience and convey essential information clearly.

Here are the steps to follow for each part:

1. High-Level Overview (90 seconds):
   - Create a high-level overview around 210 words that covers why the topic is useful/needed, what problem it solves, and includes some catchy general information. Ensure that the overview is engaging, easy to understand, and suitable for a broad audience.
   - Introduce the sub-topic with a compelling hook that captures the audience's attention.
   - Explain the importance and relevance of the sub-topic in a clear and concise manner.
   - Highlight the key problem that the sub-topic addresses and its broader implications.
   - Include some interesting facts or catchy information to make the overview memorable.

2. In-Depth Explanation Part 1 (60 seconds):
   - Create an in-depth explanation part 1 around 140 words that focuses more on details and the science behind the sub-topic.

3. In-Depth Explanation Part 2 (60 seconds):
   - Create an in-depth explanation part 2 around 140 words, focusing on a different aspect of the sub-topic than part 1.

4. Example/Application Overview 1 (60 seconds):
   - Provide an example, application, or interesting application overview around 140 words that gives a practical or real-world example of the sub-topic.

5. Example/Application Overview 2 (60 seconds):
   - Provide a second example, application, or interesting application overview around 140 words that focuses on a different practical or real-world example of the sub-topic.

6. Example/Application Overview 3 (60 seconds):
   - Provide a third example, application, or interesting application overview around 140 words that gives yet another practical or real-world example of the sub-topic.

Output the final detailed script in a structured format, ensuring each part is engaging, informative, and suitable for a broad audience on social media platforms.
    """}
  ]
)

print(completion.choices[0].message)
