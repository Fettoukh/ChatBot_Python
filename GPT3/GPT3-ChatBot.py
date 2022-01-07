#GPT-3 est Generative Pre-trained Transformer 3, 
#C'est un modèle de langage formé sur un grand nombre d'ensembles de données d'Internet et développé par une société appelée OpenAI. 
#GPT-3 est proposé via l'API, actuellement, l'API est dans une version bêta contrôlée et il y a une liste d'attente pour accéder à cette incroyable API.

#vous devez avoir accès à l'API bêta GPT-3. Il est actuellement disponible uniquement sur invitation, vous pouvez demander l'accès en utilisant le lien "beta.openai.com". 
#Il vous mènera à un formulaire où quelques questions seront posées sur votre organisation et le projet que vous envisagez de mettre en œuvre.

#Ici, nous n'allons pas passer d'exemples de formation mais simplement accéder directement à l'API et l'utiliser comme un chatbot.
#On commence par importer les packages requis
#Nous allons passer trois arguments au modèle : 
#    Engine - Nous avons le choix entre quatre options, à savoir Davinci, ADA, Babbage et Curie. Nous utiliserons Davinci car c'est le moteur le plus puissant entraîné avec 175 milliards de paramètres
#    Temperature — Elle est généralement comprise entre 0 et 1, elle est utilisée pour contrôler le caractère aléatoire de la sortie générée. Une valeur de 0 rend le modèle déterministe, c'est-à-dire que la sortie sera la même à chaque fois que nous exécuterons, tandis que d'un autre côté, avec 1 il y aura un fort caractère aléatoire dans la sortie générée.
#    max_tokens — longueur d'achèvement maximale
#Dans le script ci-dessous, la question qui doit être posée est transmise à la variable « prompt », puis transmise au modèle à l'aide de la fonction submit_request. Le résultat est stocké dans la variable 'response' comme indiqué ci-dessous,

#Dans l'exemple ci-dessus, comme vous le voyez, le modèle peut fournir une très bonne réponse à la question posée sans ajustement ni réglage. 
#Étant donné que nous ne fournissons ici aucun exemple de formation, la sortie du modèle n'a pas toujours besoin d'être une réponse, elle pourrait proposer un ensemble de questions similaire ou un contenu lié à l'entrée transmise. 
#La performance peut être améliorée en fournissant quelques exemples de formation

import openai as ai

def chat(question,chat_log = None) -> str:
    if(chat_log == None):
        chat_log = start_chat_log
    prompt = f"{chat_log}Human: {question}\nAI:"
    response = completion.create(prompt = prompt, engine =  "davinci", temperature = 0.85,top_p=1, frequency_penalty=0, 
    presence_penalty=0.7, best_of=2,max_tokens=100,stop = "\nHuman: ")
    return response.choices[0].text

def modify_start_message(chat_log,question,answer) -> str:
    if chat_log == None:
        chat_log = start_chat_log
    chat_log += f"Human: {question}\nAI: {answer}\n"
    return chat_log

if __name__ == "__main__":
    ai.api_key = "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"

    completion = ai.Completion()

    start_chat_log = """Human: Hello, I am Human.
    AI: Hello, human I am openai gpt3.
    Human: How are you?
    AI: I am fine, thanks for asking. 
    """

    train = input("\nDo you want to train the openai chatbot (True/False): ")
    if(train == "True"):
        print("\n(To stop the training enter stop in the qestion)\n")
        while(True):
            question = input("Question: ")
            if question == "stop":
                break
            answer = input("Answer: ")
            start_chat_log = modify_start_message(start_chat_log,question,answer)
            print("\n")

    question = ""
    print("\nEnter the questions to openai (to quit type \"stop\")")
    while True:
        question = input("Question: ")
        if question == "stop":
            break
        print("AI: ",chat(question,start_chat_log))
        
        
 
