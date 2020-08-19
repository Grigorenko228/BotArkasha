import random
import time
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

ANSWERS = [['открыть дверь', 'закрыть дверь'], ['открыть окно', 'закрыть окно'], ['включить свет', 'выключить свет']]


def errorCatcher(x):
    count = 0
    for i in ANSWERS:
        for j in i:
            if j in x:
                count += 1
            if count > 1:
                return 'error'
    return 'ok'


session = vk_api.VkApi(token='8a38ef4dbb2486b716f6254ca77c5071cc340c41a2ee26e9231e2a750f29e4d494665373700e37ae27112')

session_api = session.get_api()
longpoll = VkLongPoll(session)
door = 1

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:

            print('Сообщение пришло в: ' + str(event.datetime))
            print('Текст сообщенимя: ' + str(event.text))

            response = event.text.lower()
            if event.from_user and not event.from_me:

                if response.find('привет') >= 0 or response.find('здравствуй') >= 0:
                    time.sleep(random.uniform(0.5, 1.5))
                    session.method('messages.send',
                                   {'user_id': event.user_id, 'message': 'И тебе привет!', 'random_id': 0})

                elif response.find('пока') >= 0 or response.find('досвидания') >= 0:
                    time.sleep(random.uniform(0.5, 1.5))
                    session.method('messages.send',
                                   {'user_id': event.user_id, 'message': 'До скорой встречи!', 'random_id': 0})

                elif response.find('открой дверь') and door == 1:
                    door = 0
                    time.sleep(random.uniform(0.5, 1.5))
                    session.method('messages.send',
                                   {'user_id': event.user_id, 'message': 'Дверь закрыта.', 'random_id': 0})

                elif response.find('открой дверь') and door == 0:
                    time.sleep(random.uniform(0.5, 1.5))
                    session.method('messages.send',
                                   {'user_id': event.user_id, 'message': 'Уже закрыта!', 'random_id': 0})

                elif response.find('закрой дверь') and door == 0:
                    door = 1
                    time.sleep(random.uniform(0.5, 1.5))
                    session.method('messages.send',
                                   {'user_id': event.user_id, 'message': 'Дверь открыта.', 'random_id': 0})

                elif response.find('закрой дверь') and door == 1:
                    time.sleep(random.uniform(0.5, 1.5))
                    session.method('messages.send',
                                   {'user_id': event.user_id, 'message': 'Уже открыта!', 'random_id': 0})
