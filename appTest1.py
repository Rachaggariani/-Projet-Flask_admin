from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_babel import Babel
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length
from werkzeug.security import generate_password_hash
import pymysql
import os

# Installer MySQLdb pour la compatibilité avec pymysql
pymysql.install_as_MySQLdb()

# Clé secrète pour l'application Flask
secret_key = os.urandom(24)

# Initialisation de l'application Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/testapplicationone'
app.config['SECRET_KEY'] = secret_key  # Ajout de la clé secrète

# Initialisation de SQLAlchemy
db1 = SQLAlchemy(app)

# Initialisation de Flask-Babel
babel = Babel(app)

# Modèle User pour SQLAlchemy
class User(db1.Model):
    __tablename__ = 'user'
    id = db1.Column(db1.Integer, primary_key=True)
    username = db1.Column(db1.String(80), unique=True, nullable=False)
    email = db1.Column(db1.String(200), unique=True, nullable=False)
    password = db1.Column(db1.String(200), nullable=False)

    # Relation avec le modèle Order
    orders = db1.relationship("Order", back_populates="user")

# Modèle Order pour SQLAlchemy
class Order(db1.Model):
    __tablename__ = "order"
    id = db1.Column(db1.Integer, primary_key=True, nullable=False)
    order_date = db1.Column(db1.DateTime, unique=False, nullable=False)
    user_id = db1.Column(db1.Integer, db1.ForeignKey('user.id', onupdate="CASCADE", ondelete='CASCADE'), nullable=False)
    user = db1.relationship("User", back_populates="orders")

# Formulaire pour le modèle User
class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])

# ModelView pour Flask-Admin avec des configurations personnalisées
class UserAdmin(ModelView):
    column_exclude_list = ['password']  # Exclure le champ mot de passe de la vue

    def on_model_change(self, form, model, is_created):
        # Chiffrer le mot de passe lors de la création ou de la modification d'un utilisateur
        if form.password.data:
            model.password = generate_password_hash(form.password.data)

class OrdersAdmin(ModelView):
    form_columns = ["order_date", "user"]
    column_list = ["order_date", "user"]

# Initialisation de Flask-Admin
admin = Admin(app, template_mode='bootstrap3', index_view=AdminIndexView(name='Admin Panel'))

# Ajouter la vue UserAdmin à Flask-Admin
admin.add_view(UserAdmin(User, db1.session)) 
admin.add_view(OrdersAdmin(Order, db1.session))  # Ajouter la vue OrdersAdmin

@app.route('/')
def index():
    users = User.query.all()  # Récupérer tous les utilisateurs de la base de données
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
