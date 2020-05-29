import codecs
import json

from telegram.ext import Updater, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from settings import Config
from telegram.ext import MessageHandler, Filters

from aoiklivereload import LiveReloader

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger()

REQUEST_KWARGS = {
    'proxy_url': Config.PROXY
}

def get_address(msg):
    with codecs.open('adresses.json', encoding='utf-16') as json_file:
        data = json.loads(json_file.read())
        if not msg:
            return data
        find_add = [addr for addr in data if msg in addr['address'].lower()]
        return find_add


def register_user(adr):
    pass

def is_valid(adress):
    return True

def get_user(telegramm_user_id):
    with codecs.open('users.json', 'r', encoding='utf-16') as json_file:
        users = json.loads(json_file.read())

        return { user for user in users.values if user.get('telegramm_user_id') == telegramm_user_id} or None

def register_user(user):
    existing_user = get_user(user['telegramm_id'])
    if not existing_user:
        existing_user = {user}

    existing_user.update(user)

    with codecs.open('users.json', 'wr', encoding='utf-16') as json_file:
        users = json.loads(json_file.read())
        if not users:
            users = []
        users.append(existing_user)
        json_file.write(users)



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
        chat_id = update.message.chat_id


        # delete menu
        reply_markup = ReplyKeyboardRemove()
        context.bot.send_message(chat_id=update.effective_chat.id, text='Один из этих?', reply_markup=reply_markup)





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
            adresses = get_address(normal_msg)

            logger.error(adresses)
            if not adresses:
                return context.bot.send_message(chat_id=update.effective_chat.id,
                                                text=f'Не знаю в городе адреса похожего на "{msg}".Может опечатка?\nУточните адрес.')


            if len(adresses) > 10:
                return context.bot.send_message(chat_id=update.effective_chat.id,
                                         text=f'Я знаю слишком много ({len(adresses)}) адресов, похожих на "{msg}".\nУточните адрес.')


            if len(adresses) == 1:
                return register_user(adresses[0])


            if len(adresses) <= 10:
                user = {
                    'first_name': _from.first_name,
                    'last_name': _from.last_name,
                    'username': _from.username,
                    'telegramm_id': _from.id
                }

                button_list = [InlineKeyboardButton(adr['address'], callback_data={**user, 'address': adr['address']})
                                for adr in adresses]

                reply_markup = InlineKeyboardMarkup(self.build_menu(button_list, n_cols=2))

                context.bot.send_message(chat_id=update.effective_chat.id, text='Один из этих?', reply_markup=reply_markup)


if __name__ == '__main__':
    reloader = LiveReloader()
    reloader.start_watcher_thread()

    dialog_bot = DialogBot(Config.BOT_TOKEN)
    dialog_bot.start()



