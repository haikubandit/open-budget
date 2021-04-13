"""SQLAlchemy models for budget data and users."""

from datetime import datetime

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class Department(db.Model):
    """Departments in the city."""

    __tablename__ = 'departments'

    dept_code = db.Column(db.Text, primary_key=True,)
    dept_name = db.Column(db.Text, nullable=False, unique=True,)
    description = db.Column(db.Text,)

    general_funds = db.relationship('GeneralFund', backref='department')

    def serialize(self):
        """Returns a dict representation of departments which we can turn into JSON"""
        return {
            'dept_code': self.dept_code,
            'dept_name': self.dept_name,
            'description': self.description
            # 'general_funds': self.general_funds
        }

    def __repr__(self):
        return f"<Department {self.dept_code} {self.dept_name} >"


class Division(db.Model):
    """Departments in the city."""

    __tablename__ = 'divisions'

    division_id = db.Column(db.Integer, primary_key=True,)
    division_name = db.Column(db.Text, nullable=False, unique=True,)
    description = db.Column(db.Text, )
    dept_code = db.Column(db.Text, db.ForeignKey('departments.dept_code'))

    department = db.relationship('Department', backref='division')

    def __repr__(self):
        return f"<Division {self.dept_id} {self.division_name} >"


class GeneralFund(db.Model):
    """User in the system."""

    __tablename__ = 'generalfunds'

    id = db.Column(db.Integer, primary_key=True,)

    dept_code = db.Column(db.Text, db.ForeignKey('departments.dept_code'))

    allocation = db.Column(db.Float, nullable=False,)

    year = db.Column(db.Integer,)

    def serialize(self):
        """Returns a dict representation of departments which we can turn into JSON"""
        return {
            'dept_code': self.dept_code,
            'allocation': self.allocation,
            'year': self.year
            # 'department': self.department
        }


    def __repr__(self):
        return f"<GeneralFund {self.id} {self.dept_code} {self.allocation} {self.year} >"
