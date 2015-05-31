from flask import Flask
from flask import render_template
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello world'

@app.route('/entries')
def entries(entry='May27'):
	entry_loc = 'static/DailyEntries/' + entry
	image = '/static/images/' + entry + '.jpg'
	print "image URL", image
	with open(entry_loc) as f:
		content = f.readlines()
	return render_template('entries.html', entry = content, image = image)

if __name__ == '__main__':
	app.run(debug=True)

