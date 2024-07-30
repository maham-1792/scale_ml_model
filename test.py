import cohere

# Initialize the Cohere client with your API key
cohere_api_key = "tqTkOB5IwS69rO8XirIcu0rk6dfzQ0coiZYoxxHa"  # Replace with your actual API key
cohere_client = cohere.Client(cohere_api_key)

# List of models to test
models = ['command-xlarge-nightly', 'command-medium-nightly', 'command-light-nightly']

# Test each model
for model in models:
    try:
        response = cohere_client.generate(
            model=model,
            prompt="I love this service!",
            max_tokens=50
        )
        print(f"Model: {model}, Generated Text: {response.generations[0].text}")
    except Exception as e:
        print(f"Model: {model}, Error: {e}")
