

from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
def homepage():

	title = "My First Website"
	paragraph = ["Hello my name is Kai Burkholder","Hello my name is Kai Burkholder","Hello my name is Kai Burkholder"]

	return render_template("Index.html",title = title, paragraph= paragraph )


@app.route('/about')

def aboutpage():

	title = "About this site"
	paragraph = ["mememe", "blablabla"]
	pagetype = 'about'

	return render_template("Index.html", title= title, paragraph= paragraph, pagetype= pagetype)



if __name__ == "__main__":
	app.run()
