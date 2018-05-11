# coding: utf-8
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route("/get_essay")
def get_essay():

	# based on 100 words per paragraph
	sample_paragraph = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, hjyyj. \n\n"
	
	# take in word count from form and convert to int
	word_count = int(request.args.get("word_count"))

	# calculate a paragraph count
	paragraph_count = word_count/100

	return render_template('get_essay.html', get_essay = sample_paragraph, paras=paragraph_count)


if __name__ == "__main__":
		app.run(debug=True, use_reloader=True)