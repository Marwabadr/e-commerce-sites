import os

class Config:
    # Clé secrète pour la sécurité de l'application
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'une_cle_secrete_tres_securisee'

    # Configuration de la base de données SQLite
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(BASEDIR, 'mydatabase.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Désactive le suivi des modifications

    # Mode débogage
    DEBUG = True