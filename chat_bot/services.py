import codecs
import json


def search_address(msg):
    with codecs.open('resources/adresses.json', encoding='utf-16') as json_file:
        data = json.loads(json_file.read())
        if not msg:
            return data
        find_add = [addr for addr in data if msg in addr['address'].lower()]
        return find_add


def get_user(telegramm_user_id):
    with codecs.open('resources/users.json', 'r+', encoding='utf-16') as json_file:
        users = json.loads(json_file.read())
        users = [user for user in users if user.get('telegramm_id') == telegramm_user_id]
        return users[0] if len(users) > 0 else None


def register_user(user):
    existing_user = get_user(user['telegramm_id'])
    if not existing_user:
        existing_user = user
    existing_user['address'] = user['address']

    with codecs.open('resources/users.json', 'r', encoding='utf-16') as json_file:
        users = json.loads(json_file.read())
        if not users:
            users = []
        users.append(existing_user)

    with codecs.open('resources/users.json', 'w', encoding='utf-16') as json_file:
        json_file.write(json.dumps(users))

    return existing_user
