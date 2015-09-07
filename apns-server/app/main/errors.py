from flask import render_template, jsonify, make_response
from . import main

@main.app_errorhandler(404)
def page_not_found(e):
    return make_response(jsonify({'status': 'not_found'}), 404)

@main.app_errorhandler(500)
def internal_server_error(e):
    return make_response(jsonify({'status': 'server_error'}), 500)
