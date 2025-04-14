import os

messages = []

name = input("Name: ")

while True:

    #cleaning terminal
    os.system('cls')

    if len(messages) > 0:
        for m in messages:
            print(m['name'], "-", m['text'])

    print("__________________")
    
    #getting text
    text = input("message: ")
    if text == "end":
        break

    #adding messages in the list
    messages.append( {
        "name": name,
        "text": text
    })