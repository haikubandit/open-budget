import os

from flask import Flask, render_template, request, flash, redirect, jsonify, session, g, abort
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError

from models import db, connect_db, Department, Division, GeneralFund
# from forms import NewSongForPlaylistForm, SongForm, PlaylistForm

import pdb

app = Flask(__name__)

# Get DB_URI from environ variable (useful for production/testing) or,
# if not set there, use development local db.
app.config['SQLALCHEMY_DATABASE_URI'] = (
os.environ.get('DATABASE_URL', 'postgresql:///omaha_budget'))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)



##############################################################################
# Homepage and error pages


@app.route('/')
def homepage():
    """Show homepage:

    """

    return render_template('base.html')


# @app.errorhandler(404)
# def page_not_found(e):
#     """404 NOT FOUND page."""

#     return render_template('404.html'), 404


##############################################################################
# API routes

@app.route('/api/<int:year>')
def budget_api(year):
    """Get budget data by year

    """
    json_gf = []
    # all_depts = [dept.serialize() for dept in Department.query.all()]
    all_gf = [gf.serialize() for gf in GeneralFund.query.all()]
    GFunds = GeneralFund.query.filter(GeneralFund.year==year)
    for fund in GFunds:

        json_gf.append({
            "id": fund.id,
            "dept": fund.department.dept_name,
            "allocation": fund.allocation,
            "year": fund.year})

    # pdb.set_trace()


    return jsonify(depts=json_gf)