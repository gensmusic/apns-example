from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Length

class PushForm(Form):
    identity = StringField('identity', validators=[Required(), Length(1, 64)])
    device = StringField('device', validators=[Required()])
    token = StringField('token', validators=[Required()])
    submit = SubmitField('push')

    def __repr__(self):
        return '<identity:%s, device:%s, token:%s>' % (self.identity, self.device, self.token)

class RegistrationForm(Form):
    identity = StringField('identity', validators=[Required(), Length(1, 64)])
    device = StringField('device', validators=[Required()])
    token = StringField('token', validators=[Required()])
    submit = SubmitField('register')

    def __repr__(self):
        return '<identity:%s, device:%s, token:%s>' % (self.identity, self.device, self.token)
