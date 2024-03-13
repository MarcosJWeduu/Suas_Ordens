from flask import Blueprint, render_template

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
def index():
    return render_template('index.html')

@dashboard_bp.route('/dashboard')
def dashboard():
    # Lógica para exibir o dashboard
    return render_template('dashboard.html')
