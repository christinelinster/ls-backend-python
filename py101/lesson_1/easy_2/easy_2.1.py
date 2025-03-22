# Welcome Stranger

def greetings(name, info):
    full_name = " ".join(name)
    return (f'Hello, {full_name}! Nice to have a {info["title"]} {info["occupation"]} around.')


greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.