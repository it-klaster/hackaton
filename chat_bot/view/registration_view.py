import textwrap

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

from chat_bot.constants import Buttons
from chat_bot.utils import get_logging
from chat_bot.view.main_view import MainView

ask_adr_msg = "Здравствуйте, {}! \nЧтобы получать уведомления сервиса 'Умный город',  укажите адрес дома"

logger = get_logging()

class RegistrationView(MainView):

    def __init__(self, bot):
        super().__init__(bot)
        self.bot = bot

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

    def ask_adress(self, chat_id, user):
        answer = ask_adr_msg.format(user.first_name)
        keyboard = [
            [KeyboardButton(text=Buttons.cancel)]
        ]
        markup = ReplyKeyboardMarkup(keyboard=keyboard)
        return self.bot.send_message(chat_id=chat_id, text=answer, reply_markup=markup)


    def not_found(self, chat_id, adr):
        return self.bot.send_message(chat_id=chat_id,
                                        text=f'Не знаю в городе адреса похожего на "{adr}".Может опечатка?\nУточните адрес.')

    def too_many_found(self, chat_id, msg, count):
        return self.bot.send_message(chat_id=chat_id,
                                        text=f'Я знаю слишком много ({count}) адресов, похожих на "{msg}".\nУточните адрес.')

    def choose_address(self, chat_id, addresses):
        button_list = [
            InlineKeyboardButton(
                adr.name,
                # Ограничение на длину символов в callback_data?
                # При большем количестве символов вызывается telegram.error.BadRequest: Button_data_invalid
                # TODO: Возможно стоит передавать Address.id
                callback_data=adr.name[:37]
            )
            for adr in addresses]
        reply_markup = InlineKeyboardMarkup(self.build_menu(button_list, n_cols=2))
        logger.debug(reply_markup)
        return self.bot.send_message(chat_id=chat_id, text='Один из этих адресов?',
                                        reply_markup=reply_markup)

    def reply_success(self, chat_id, user):
        # delete menu
        reply_markup = ReplyKeyboardRemove()
        self.bot.send_message(chat_id=chat_id,
                                 text=f'Ok, запишем: Что будет нового по адресу: {user.address.name} сообщить {user.name}',
                                 reply_markup=reply_markup)


    def not_found_user(self, chat_id):
        return self.bot.send_message(chat_id=chat_id, text='Мы знакомы?')

    def change_adress(self, chat_id, user):
        return self.bot.send_message(chat_id=chat_id,
                                     text=f"""Вы подписаны на оповещения по адресу {user["address"]}. 
                                     Для изменения адреса напишите /register """)