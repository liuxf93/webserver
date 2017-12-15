from . import api
from flask import render_template


@api.route('/gallery')
def gallery():
    return render_template('api_v1/gallery.html')