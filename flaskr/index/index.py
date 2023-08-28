from flask import Blueprint, render_template


class Index:
    blueprint = Blueprint("index", __name__, template_folder='templates')

    def __init__(self):
        pass

    @blueprint.route("/")
    def index():
        """Index...
        :return:
        """
        return render_template('index.html', page_title='Hello World')
