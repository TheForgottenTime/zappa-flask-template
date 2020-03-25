from flask import current_app, Blueprint, render_template

bp = Blueprint('bp', __name__, url_prefix='/bp')

#define routes to api endpoints here
#url_prefix optional, reccomended when building out large apps with multiple blueprints

@bp.route('/')
def index():
    pass