from openai import OpenAI

# Initialize OpenAI client to interact with TinyLlama API
client = OpenAI(
    base_url="http://localhost:8080/v1",  # TinyLlama API endpoint
    api_key="sk-no-key-required",        # No API key needed for local TinyLlama
)

def process_user_input(user_input):
    """
    Process user input and return a chatbot response from TinyLlama.
    """
    response = client.chat.completions.create(
        model="LLaMA_CPP",  # Adjust the model name based on TinyLlama's requirements
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant designed to help students find "
                    "nearby food resources, such as food banks and pantries, and suggest recipes "
                    "based on the ingredients they have."
                ),
            },
            {"role": "user", "content": user_input},
        ]
    )
    return response.choices[0].message["content"]
