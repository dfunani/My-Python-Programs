from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import yaml


def Main():
    chatbot = ChatBot("Codeeee")
    trainer = ChatterBotCorpusTrainer(chatbot)
    listener = ListTrainer(chatbot)

    listener.train(Get_TrainingData())
    trainer.train(
        "chatterbot_corpus.data.english"
    )

    exit_conditions = (":q", "quit", "exit")
    while True:
        query = input("> ")
        if query in exit_conditions:
            break
        else:
            print(f"🪴 {chatbot.get_response(query)}")


def Get_TrainingData():
    res = Get_WhatsAppData("./WhatsApp Chat with Sexy MONKEY.txt")
    return res


def Get_WhatsAppData(filename):
    with open(filename, "r", encoding="utf_8") as file:
        data = file.read()
    res = data. split('\n')
    data = list(map(lambda x: x[x.find(": ") + 1:], res))
    return list(filter(lambda x: x != "<Media omitted>", data))


if __name__ == "__main__":
    Main()
