import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime
import time
import random

session = vk_api.VkApi(token='8a38ef4dbb2486b716f6254ca77c5071cc340c41a2ee26e9231e2a750f29e4d494665373700e37ae27112')

session_api = session.get_api()
longpoll = VkLongPoll(session)
door = 1 #закрыта

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

                elif response.find('открой дверь') and door == 1:
                    door = 0
                    time.sleep(random.uniform(0.5, 1.5))
                    session.method('messages.send', {'user_id': event.user_id, 'message': 'Дверь закрыта.', 'random_id': 0})
                    print(door)

                elif response.find('открой дверь') and door == 0:
                    time.sleep(random.uniform(0.5, 1.5))
                    session.method('messages.send',
                                   {'user_id': event.user_id, 'message': 'Уже закрыта!', 'random_id': 0})
                    print(door)

                elif response.find('закрой дверь') and door == 0:
                    door = 1
                    time.sleep(random.uniform(0.5, 1.5))
                    session.method('messages.send', {'user_id': event.user_id, 'message': 'Дверь открыта.', 'random_id': 0})
                    print(door)

                elif response.find('закрой дверь') and door == 1:
                    time.sleep(random.uniform(0.5, 1.5))
                    session.method('messages.send',
                                   {'user_id': event.user_id, 'message': 'Уже открыта!', 'random_id': 0})
                    print(door)
