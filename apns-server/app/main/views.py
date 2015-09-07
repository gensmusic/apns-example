from flask import render_template, jsonify, request
from . import main
from .forms import RegistrationForm, PushForm
from ..models import Identity

@main.route('/')
def index():
    return 'Hello'

@main.route('/query')
def query():
    ids = Identity.query.all()
    return render_template('query.html', ids=ids)

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    # if not form.validate():
    #     return jsonify({'register' : 'failed', 'reason' : 'bad format'})
    ids = Identity.query.filter_by(email=form.identity.data)
    if ids is None:
        identity = Identity(identity=form.identity.data,
                            device=form.device.data,
                            token=form.token.data)
        db.session.add(identity)
        db.session.commit()
    return jsonify({'register': 'ok'})

@main.route('/register-web', methods=['GET', 'POST'])
def registerweb():
    if request.method == 'GET':
        return render_template('register-web.html')

    form = RegistrationForm()
    print form
    if not form.validate():
        return jsonify({'register' : 'failed', 'reason' : 'bad format'})

    ids = Identity.query.filter_by(email=form.identity.data)
    if ids is None:
        identity = Identity(identity=form.identity.data,
                            device=form.device.data,
                            token=form.token.data)
        db.session.add(identity)
        db.session.commit()
    return jsonify({'register': 'ok'})

@main.route('/push', methods=['GET', 'POST'])
def push():
    return jsonify({'push': 'ok'})