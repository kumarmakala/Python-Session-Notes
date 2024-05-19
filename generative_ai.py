import openai

def get_recipe(ingredients):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",  # Choose the appropriate model
        prompt=f"What can I cook with {ingredients}?",
        max_tokens=150,
        temperature=0.5
    )
    return response.choices[0].text.strip()

# Example usage
ingredients = "tomatoes, spinach, chicken"
recipe = get_recipe(ingredients)
print("Suggested Recipe:", recipe)
