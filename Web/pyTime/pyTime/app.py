"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, render_template, url_for
app = Flask(__name__)

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
    """Renders a sample page."""
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
	return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(
		host = '0.0.0.0',
		port = 5000,
		debug = True
	)
