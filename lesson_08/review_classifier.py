import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import errors
from google.genai import types
import time

env_path = Path(__file__).resolve().parent.parent / ".env"

load_dotenv(env_path)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini key not found!!")

client = genai.Client(api_key = api_key)
print("Gemini client initialized successfully")

test_data = [
    {
        "review": "The product quality is excellent!",
        "label": "POSITIVE"
    },
    {
        "review": "I am satisfied with the product quality!",
        "label": "POSITIVE"
    },
    {
        "review": "The service was excellent",
        "label": "POSITIVE"
    },
    {
        "review": "The product stopped working after two days.",
        "label": "NEGATIVE"
    },
    {
        "review": "I received a defective product.",
        "label": "NEGATIVE"
    },
    {
        "review": "The product was expired.",
        "label": "NEGATIVE"
    },
    {
        "review": "The package contains three items.",
        "label": "NEUTRAL"
    },
    {
        "review": "The package contains electrical appliances.",
        "label": "NEUTRAL"
    },
    {
        "review": "The package contains cooking essentials.",
        "label": "NEUTRAL"
    },
    
]

new_reviews = [
    {
        "review": "Great, another product that broke within a week.",
        "label": "NEGATIVE"
    },
    {
        "review": "The product is not bad at all.",
        "label": "POSITIVE"
    },
    {
        "review": "Excellent packaging, but the product doesn't work.",
        "label": "NEGATIVE"
    },
    {
        "review": "It does what it is supposed to do. Nothing special.",
        "label": "NEUTRAL"
    },
    {
        "review": "I expected worse, but it turned out quite good.",
        "label": "POSITIVE"
    },
    {
        "review": "I've seen better products at half the price.",
        "label": "NEGATIVE"
    }
]
test_data.extend(new_reviews)

def zero_shot_prompt(review):
    prompt = f"""
    Classify the following customer review
    as POSITIVE, NEGATIVE, or NEUTRAL.

    Return exactly one sentiment label:
    POSITIVE, NEGATIVE, or NEUTRAL.
    Do not include explanations.

    Review: {review}
    Label:
    """

    return prompt

# print(zero_shot_prompt(test_data[0]["review"]))

def few_shot_prompt(review):
    prompt = f"""
    Classify the following customer review
    as POSITIVE, NEGATIVE, or NEUTRAL.    

    Examples:

    Review: The cake was excellent!
    Label: POSITIVE

    Review: The delivery service was poor.
    Label: NEGATIVE

    Review: I bought 10 erasers.
    Label: NEUTRAL  

    Return exactly one sentiment label:
    POSITIVE, NEGATIVE, or NEUTRAL.
    Do not include explanations.

    Review: {review}
    Label: 
    """
    return prompt

# print(few_shot_prompt(test_data[0]["review"]))


def classify_review(prompt):
    valid_labels = {"POSITIVE", "NEGATIVE", "NEUTRAL"}

    try:
        response = client.models.generate_content(
            model = "gemini-3.5-flash-lite",
            contents = prompt,
            config=types.GenerateContentConfig(
                temperature=0.0
            )
        )

        output_txt = (response.text or "").strip().upper()

        if output_txt in valid_labels:
            # print("Gemini: ", output_txt)
            return output_txt
        return "INVALID"
    except errors.APIError as e:
        print(f"Gemini API error: {e}")
        return "API_ERROR"


# prompt = zero_shot_prompt(test_data[0]["review"])
# # print(prompt)

# prediction = classify_review(prompt)

# print(prediction)


def evaluate(prompt_function):
    correct = 0
    api_errors = 0
    invalid_outputs = 0

    for item in test_data:
        # Extract the review
        review = item["review"]

        # Extract the actual label
        label = item["label"]

        # Generate the prompt
        user_prompt = prompt_function(review)

        # Get the prediction
        model_prediction = classify_review(user_prompt)

        print(f"Review: {review}")
        print(f"Expected: {label}")
        print(f"Predicted: {model_prediction}")
        print(f"Match: {model_prediction == label}")
        print("-" * 50)

        if model_prediction == "API_ERROR":
            api_errors += 1

        elif model_prediction == "INVALID":
            invalid_outputs += 1

        elif model_prediction == label:
            correct += 1
        time.sleep(5)

    total = len(test_data)

    evaluated = total - api_errors

    incorrect = evaluated - correct - invalid_outputs

    accuracy = (correct / evaluated) * 100 if evaluated > 0 else None

    coverage = (evaluated / total) * 100 if total > 0 else None

    return {
        "total": total,
        "evaluated": evaluated,
        "correct": correct,
        "incorrect": incorrect,
        "invalid_outputs": invalid_outputs,
        "api_errors": api_errors,
        "accuracy": accuracy,
        "coverage": coverage
    }

print("\n===== RUNNING ZERO-SHOT EVALUATION =====\n")
zero_shot_results = evaluate(zero_shot_prompt)

print("\n===== RUNNING FEW-SHOT EVALUATION =====\n")
few_shot_results = evaluate(few_shot_prompt)

def display_results(title, results):
    print(f"===== {title} =====")
    for key, value in results.items():
        key = key.replace("_", " ").title()
        print(f"{key} : {value}")
        

display_results("ZERO-SHOT RESULTS", zero_shot_results)

print()

display_results("FEW-SHOT RESULTS", few_shot_results)