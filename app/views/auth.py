from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models.models import db, User
from flask import jsonify

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email, password=password).first()

        if user:
            session['user_id'] = user.id
            return redirect(url_for('dashboard.dashboard'))
        else:
            
            return redirect(url_for('auth.login'))

    return render_template('login.html')

@auth_bp.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')
        password_confirm = request.form.get('password_confirm')

        if first_name and last_name and email and password and password_confirm:
            new_user = User(first_name=first_name, last_name=last_name, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()

            # Retorna uma resposta JSON indicando sucesso
            return jsonify({"success": True})

        else:
            # Retorna uma resposta JSON indicando falha e as mensagens de erro
            return jsonify({"success": False, "errors": ["Por favor, preencha todos os campos do formulário."]}), 400

    return render_template('register.html')