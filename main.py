import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if api_key is None:
    raise RuntimeError("OPENROUTER_API_KEY is not set in the environment variables.")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

def main():
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "user",
                "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
            }
        ],
    )
    #check usage
    if response.usage is not None:
        print(f"Prompt tokens: {response.usage.prompt_tokens}, Completion tokens: {response.usage.completion_tokens}\nResponse tokens: {response.usage.total_tokens}")
    else:
        raise RuntimeError("Response usage is None. Unable to retrieve token usage information.")
    print(f"Response: \n{response.choices[0].message.content}")


if __name__ == "__main__":
    main()
