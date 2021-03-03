from flask import Blueprint
main = Blueprint('main',__name__)
from . import views

import os
from flask import send_from_directory

@main.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')
