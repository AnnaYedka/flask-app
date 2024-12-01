from flask import redirect, url_for, flash, render_template, request
from . import bp
from flask_login import current_user, login_user, logout_user
import sqlalchemy as sa
from models import User
from .form import LoginForm
from app import login, db
from urllib.parse import urlsplit
from functools import wraps


@login.user_loader
def load_user(id):
	return db.session.get(User, int(id))


@bp.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('ingredient.index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = db.session.scalar(
			sa.select(User).where(User.username == form.username.data))
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')
			return redirect(url_for('login'))
		login_user(user, remember=form.remember_me.data)
		next_page = request.args.get('next')
		if not next_page or urlsplit(next_page).netloc != '':
			next_page = url_for('ingredient.index')
		return redirect(next_page)
	return render_template('auth/login.html', title='Sign In', form=form)


@bp.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('ingredient.index'))


def admin_required(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		if not current_user.role.name == 'admin':
			print('user is not admin')
			return redirect(url_for('auth.login'))
		return func(*args, **kwargs)
	return wrapper
