from flask import Flask
from flask import render_template
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello world'

@app.route('/entries')
def entries():
	file_name = 'templates/DailyEntries/May27'
	with open(file_name) as f:
		content = f.readlines()
	return render_template('entries.html', entry=content)
	# return 'entries'

if __name__ == '__main__':
	app.run(debug=True)

