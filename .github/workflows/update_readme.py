import requests
import re

# Fetch a random cat fact from the Cat Facts API
response = requests.get("https://catfact.ninja/fact")
fact_data = response.json()
random_fun_fact = fact_data["fact"]

# Read the existing README.md file
with open("README.md", "r") as readme_file:
    readme_content = readme_file.read()

# Replace the FUN_FACT_PLACEHOLDER with the new fun fact
readme_content = re.sub(r"<!-- FUN_FACT_PLACEHOLDER -->", f"**Fun Fact:** {random_fun_fact}", readme_content)

# Write the updated content back to README.md
with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)
