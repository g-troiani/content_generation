# generate_content_script.py

import subprocess

# Function to run a script and get its output
def run_script(script_name):
    result = subprocess.run(["python", script_name], capture_output=True, text=True)
    return result.stdout

# List of script names to run
scripts = [
    "create_lesson_plan.py",
    "lesson_into_sub_topics.py",
    "sub_topics_content_creation.py",
]

# Collect the outputs from each script
content_results = []
for script in scripts:
    output = run_script(script)
    content_results.append(output)

# Save results to a file
with open("content_generation_script.txt", "w") as file:
    for result in content_results:
        file.write(result + "\n\n")

print("Content generation script saved to 'content_generation_script.txt'.")
