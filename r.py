import re

# Sample text containing the image references
text = """
Here is some text with an image reference:
!![Image Description](/images/Pasted%20image%2020241210145647.png).
Here’s another one:
!![Image Description](/images/Pasted%20image%2020241210150000.png).
"""

# Regular expression to match and capture image paths
pattern = r"!!\[Image Description\]\((/images/[^\)]+)\)"

# Find all matches and extract image paths
matches = re.findall(pattern, text)
cleaned_paths = [match.replace("%20", " ") for match in matches]

# Print the extracted image paths
print("Extracted image paths:")
for match in cleaned_paths:
    if '%20' in match:
        print('yes')
    print(match.replace('%20',' '))
