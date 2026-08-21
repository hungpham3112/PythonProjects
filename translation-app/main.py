import ollama
ollama.chat(
  model='mistral', 
  messages=[{'role': 'user', 'content': 'Why is the sky blue?'}], 
  stream=False
)
