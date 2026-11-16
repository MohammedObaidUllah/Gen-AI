# exercise 1 and 2
def create_prompt(topic, audience):
    return f"Explain {topic} to {audience} in simple terms with an example."

prompt = create_prompt("Generative AI", "beginners")
print(prompt)   

# exercise 3
try:
    number = int(input("Enter a number: "))
    print(100 / number)
except ValueError:
    print("Enter a valid number.")
except ZeroDivisionError:
    print("The number cannot be zero.")
finally:
    print("Program completed")