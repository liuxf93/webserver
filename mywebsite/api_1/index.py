from flask import render_template
from . import api


@api.route('/index')
def index():
    return render_template('api_v1/index.html')