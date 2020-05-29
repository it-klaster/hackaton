import codecs
import json
import logging

from aoiklivereload import LiveReloader
from settings import Config, DEBUG
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import MessageHandler, Filters
from telegram.ext import Updater, CallbackQueryHandler

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger()

REQUEST_KWARGS = {
    'proxy_url': Config.PROXY
}

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


class DialogBot:
    def __init__(self, token):
        self.updater = Updater(token, request_kwargs=REQUEST_KWARGS, use_context=True)
        handler = MessageHandler(Filters.text | Filters.command, self.handle_message)
        self.updater.dispatcher.add_handler(handler)
        self.updater.dispatcher.add_handler(CallbackQueryHandler(self.handle_button))
        self.states = ['ASKING_ADRESS', 'GET_ADRESS']
        self.state = {}

    def start(self):
        self.updater.start_polling()

    def build_menu(self,
                   buttons,
                   n_cols,
                   header_buttons=None,
                   footer_buttons=None):
        menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
        if header_buttons:
            menu.insert(0, [header_buttons])
        if footer_buttons:
            menu.append([footer_buttons])
        return menu

    def handle_button(self, update, context):
        _from = update.callback_query.from_user
        adr = update.callback_query.data
        user = {'first_name': _from.first_name,
                'last_name': _from.last_name,
                'username': _from.username,
                'telegramm_id': _from.id,
                'address': adr
                }

        registered = register_user(user)
        if registered:
            # delete menu
            address = registered["address"]
            reply_markup = ReplyKeyboardRemove()
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=f'Ok, запишем: Что будет нового по адресу: {address} сообщить {registered["first_name"]}',
                                     reply_markup=reply_markup)


    def handle_message(self, update, context):
        chat_id = update.message.chat_id
        msg = update.message.text
        normal_msg = ' '.join(msg.split()).lower()
        _from = update.message.from_user

        if chat_id not in self.state or update.message.text == "/start":
            self.state[chat_id] = 'ASKING_ADRESS'
            answer = f"Здравствуйте, {_from.first_name}! \nЧтобы получать уведомления сервиса 'Умный город',  укажите адрес дома"
            return context.bot.send_message(chat_id=update.effective_chat.id, text=answer)

        if self.state[chat_id] == 'ASKING_ADRESS':
            adresses = search_address(normal_msg)
            if not adresses:
                return context.bot.send_message(chat_id=update.effective_chat.id,
                                                text=f'Не знаю в городе адреса похожего на "{msg}".Может опечатка?\nУточните адрес.')

            if len(adresses) > 20:
                return context.bot.send_message(chat_id=update.effective_chat.id,
                                         text=f'Я знаю слишком много ({len(adresses)}) адресов, похожих на "{msg}".\nУточните адрес.')

            if len(adresses) == 1:
                return register_user(adresses[0])

            if len(adresses) <= 20:
                button_list = [InlineKeyboardButton(adr['address'], callback_data=adr['address'])
                                for adr in adresses]
                reply_markup = InlineKeyboardMarkup(self.build_menu(button_list, n_cols=2))
                return context.bot.send_message(chat_id=update.effective_chat.id, text='Один из этих?', reply_markup=reply_markup)


if __name__ == '__main__':

    if DEBUG:
        reloader = LiveReloader()
        reloader.start_watcher_thread()

    dialog_bot = DialogBot(Config.BOT_TOKEN)
    dialog_bot.start()



