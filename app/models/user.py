from . import db

class User(db.Model):
    def __init__(self, first, last, email, password):
        from . import db  # Import local dentro da classe para evitar importação circular
        self.id = db.Column(db.Integer, primary_key=True)
        self.first = db.Column(db.String(64), unique=False, nullable=False)
        self.last = db.Column(db.String(64), unique=False, nullable=False)
        self.email = db.Column(db.String(120), unique=True, nullable=False)
        self.password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'