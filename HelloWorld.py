from flask import Flask
from flask import render_template
import os
import json
from pprint import pprint


app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello world'

@app.route('/entries')
def entries(entry='May27'):
	entry_loc = 'static/DailyEntries/' + entry + '.json'
	image = '/static/images/' + entry + '.jpg'
	print "image URL", image
	with open(entry_loc) as f:
		content = f.readlines()
	with open(entry_loc) as data_file:    
	    json_content = json.load(data_file)
	print json_content
	specific_title = "Specific Title"
	return render_template('entries.html', 
		date=json_content['date'],
	 	title = json_content['title'],
	 	highlight = json_content['highlight'],
	 	image = image,
	 	specific_title = specific_title,
	 	specific_content = json_content['family']
	 	)

if __name__ == '__main__':
	app.run(debug=True)

