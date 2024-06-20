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

Here are the references for each of the variables (except subject) for creating educational short-form text content for TikTok and Instagram:
{{ACTION}}
Reference: Use action verbs that describe how the subject is teaching or explaining the concept. Examples include:

breaks down
simplifies
illustrates
demonstrates
explains

{{CONCEPT}}
Reference: Specify the educational concept or topic being explained in the text. Examples include:

photosynthesis
the water cycle
the Pythagorean theorem
the American Revolution
the basics of coding

{{WRITING_STYLE}}
Reference: Specify the desired writing style for the educational content. Examples include:

conversational
witty
straightforward
engaging
humorous

{{EDUCATIONAL_TECHNIQUES}}
Reference: Mention specific educational techniques or strategies to be used in the text. Examples include:

analogies
examples
step-by-step instructions
real-world applications
mnemonic devices

{{CONTENT_STYLE}}
Reference: Mention specific content styles or inspirations to be used in the text. Examples include:

storytelling
Informative
comparison and contrast
problem and solution

{{EXCLUSIONS}}
Reference: List elements that should be excluded or avoided in the educational content. Examples include:

complex scientific jargon
lengthy explanations
confusing terminology
irrelevant tangents
controversial opinions

{{VERSION}}
Reference: Specify whether the content is intended for TikTok or Instagram. Examples include:

TikTok
Instagram

These references provide guidance and examples for each variable to help create effective and engaging educational short-form text content tailored for TikTok and Instagram.
    """}
  ]
)

print(completion.choices[0].message)
