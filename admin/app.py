from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from chat_bot.models import *

app = Flask(__name__)

app.secret_key = 'super secret key'

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'flatly'

admin = Admin(app, name='bot_admin', template_mode='bootstrap3')
# Add administrative views here
admin.add_view(ModelView(User, session))
admin.add_view(ModelView(Address, session))
admin.add_view(ModelView(Event, session))
admin.add_view(ModelView(EventType, session))
admin.add_view(ModelView(AdminUser, session))
admin.add_view(ModelView(Organization, session))
admin.add_view(ModelView(Rules, session))
admin.add_view(ModelView(EventStatus, session))
admin.add_view(ModelView(EventTimer, session))
admin.add_view(ModelView(EventWeight, session))



app.run(host='0.0.0.0', debug=True)