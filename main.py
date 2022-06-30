import re

# Read CSS file
with open("sample.css", "r") as style:
    contents = style.read()
contents_lines = contents.split("\n")

# Parse CSS into dictionary
parse = {}
for line in contents_lines:
    line = line.strip()

    if "}" in line:
        continue

    elif "{" in line:
        css_property = line[0 : line.index("{") - 1]
        parse[css_property] = {}
        continue

    match = re.search(r"([\w-]*):\s?(.*);", line)
    if match is not None and not line.startswith("/*"):
        css_key = match.group(1)
        css_value = match.group(2)
        parse[css_property][css_key] = css_value

# Output CSS dictionary into file
output = ""
for css_property in parse.keys():
    output += f"{css_property} {{\n"

    children: dict = parse[css_property]
    for key in children.keys():
        output += f"    {key}: {children[key]};\n"

    output += "}\n\n"

with open("test.css", "w") as test:
    test.write(output)
