from werobot import WeRoBot
import config as cfg

# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
# global chatbot 


myrobot = WeRoBot(token=cfg.token)
myrobot.config["APP_ID"] = cfg.appid
myrobot.config['ENCODING_AES_KEY'] = cfg.aeskey


# chatbot = ChatBot("ChineseChatBot")
# trainer = ChatterBotCorpusTrainer(chatbot)
# trainer.train("chatterbot.corpus.chinese")


@myrobot.image
def image_repeat(message,session):
    return message.img


@myrobot.text
def test_repeat(message,session):
    return message.content


# @myrobot.text
# def text_response(message,session):
#     answer = chatbot.get_response(message.content).text
#     return answer


