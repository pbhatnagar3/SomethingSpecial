from flask import Flask, render_template, request, redirect, url_for
import os, json

app = Flask(__name__)

@app.route('/pick-a-date', methods=['GET', 'POST'])
def happy_birthday():
	if request.method == 'GET':
		return render_template('index.html')
	elif request.method == 'POST':
		f = request.form
		print "selected date : ", f['date']
		return entries(f['date'])
	else:
		return 'wtf'

@app.route('/entries')
def entries(entry='May26'):
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

