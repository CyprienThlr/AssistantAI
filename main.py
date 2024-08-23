import openai

api_key = 'Cypth2008*'
openai.api_key = api_key

def ask_jarvis(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Fonction principale pour interagir avec l'Assistant
def main():
    print("Bonjour ! Je suis JARVIS. Comment puis-je vous aider aujpurd'hui ?")
    while True:
        user_input = input("Vous: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("JARVIS: AU revoir !")
            break
        response = ask_jarvis(user_input + "\n")
        print("JARVIS:", response)

if __name__ == "__main__":
    main()