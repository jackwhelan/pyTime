from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '7a81d54bcbe122a84e2f1c100e2a67db'

posts = [
	{
		'author': 'Jack Whelan',
		'title': 'Update 1',
		'content': 'First post content',
		'date_posted': 'April 20, 2018'
	},

	{
		'author': 'John Doe',
		'title': 'Update 2',
		'content': 'Second post content',
		'date_posted': 'April 21, 2018'
	}
]

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
@app.route('/home')
@app.route('/changelog')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
	return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return  redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(
		host = '0.0.0.0',
		port = 5000,
		debug = True
	)
