from app import create_app
from flask_login import LoginManager
from app.models.user import User
app = create_app()


# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'  # Specify the login view

# User loader function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
if __name__ == '__main__':
    app.run(debug=True)