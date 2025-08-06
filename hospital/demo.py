from openai import OpenAI

# URL = 'https://api.openai.com/v1'
client = OpenAI(api_key = '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')

response = client.responses.create(
  model="gpt-4.1",
  input="Tell me a three sentence bedtime story about a unicorn."
)

print(response)
