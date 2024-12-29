from phi.model.groq import Groq

try:
    model = Groq(id="llama3-groq-8b-8192-tool-use-preview")
    print("Model is accessible!")
except Exception as e:
    print("Error accessing model:", e)
