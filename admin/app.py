from flask import Flask, request
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_babelex import Babel

from chat_bot.models import *

app = Flask(__name__)
babel = Babel(app)

app.secret_key = 'super secret key'

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'flatly'

admin = Admin(app, name='bot_admin', template_mode='bootstrap3')

@babel.localeselector
def get_locale():
    from flask import session
    if request.args.get('lang'):
        session['lang'] = request.args.get('lang')
    return session.get('lang', 'ru')


class BaseView(ModelView):
    form_args = {
        'name': {'label': 'Название'},
        'user': {'label': 'Пользователь'},
        'timer': {'label': 'Таймер'},
        'event_type': {'label': 'Событие'},
        'send_at': {'label': 'Отправить с'},
        'address': {'label': 'Адрес'},
        'phone': {'label': 'Телефон'},
        'start_time': {'label': 'Начало события'},
        'stop_time': {'label': 'Конец события'},
        'send_time': {'label': 'Время начала отправки'},
    }


class AddressView(BaseView):
    form_excluded_columns = ['users']


class EventTimerView(BaseView):
    form_excluded_columns = ['events']


# Add administrative views here
admin.add_view(BaseView(User, session))
admin.add_view(AddressView(Address, session))
admin.add_view(BaseView(Event, session, category='Event'))
admin.add_view(BaseView(EventType, session, category='Event'))
admin.add_view(BaseView(AdminUser, session, category='Admin'))
admin.add_view(BaseView(Organization, session, category='Admin'))
admin.add_view(BaseView(Rules, session, category='Admin'))
admin.add_view(BaseView(EventStatus, session, category='Event'))
admin.add_view(EventTimerView(EventTimer, session, category='Event'))
admin.add_view(BaseView(EventWeight, session, category='Event'))



app.run(host='0.0.0.0', debug=True)