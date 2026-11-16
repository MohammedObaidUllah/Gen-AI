# Exercise 1

my_profile = {
    "Name": "Obaid",
    "Age": 22,
    "College": "KMIT",
    "Programming Languages": ["Python"],
    "Current Learning Goal": "Complete Exercise 1"
}

# method 1
for key, value in my_profile.items():
    print(f"{key}: {value}")

# method 2 : print each value individually
print(my_profile["Name"])
print(my_profile["Age"])
print(my_profile["College"])
print(my_profile["Programming Languages"])
print(my_profile["Current Learning Goal"])

# Exercise 2
my_profile["current_project"] = "GenAI Learning Journey"
my_profile["Current Learning Goal"] = "Become a GenAI Developer"

for key, value in my_profile.items():
    print(f"{key}: {value}")

# Exercise 3
import json
json_string = json.dumps(my_profile, indent=4)
print(json_string)
convert_dict = json.loads(json_string)
print(convert_dict["Name"])
print(convert_dict["current_project"])

# Exercise 4
json_res = """
{
    "question": "What is Python?",
    "answer": "Python is a programming language.",
    "confidence": 0.95,
    "topics": ["Programming", "Automation", "AI"]
}
"""

data = json.loads(json_res)

print(data["question"])
print(data["answer"])
print(data["confidence"])
print(data["topics"][1])