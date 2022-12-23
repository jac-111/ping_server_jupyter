from flask import Flask, render_template

# Create a flask instance
app = Flask(__name__)


# create route decoratior
# route is the part that comes after www.mysite.com/....
# this goes to the home page
@app.route('/')


# Jinja filters
#safe
#capitalize
#lower
#upper
#title
#trim
#striptags

#def index():
#	# Header tag - like markdown #
#	return "<h1>Hello World!</h1>"

# flask knows to look at the templates directory
def index():
	my_list=[1,2,3]
	return render_template("index.html",my_list=my_list)

# This will get the final part of the route as input
# localhost:5000/user/pog
 # This decorator passes "name"
@app.route('/user/<name>')
def user(name):
	# Header tag - like markdown #
	stuff = "some <strong>HTML<strong> script"
	return render_template("user.html", 
		username=name, 
		stuff = stuff)


# Create custom error page

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

# Internal server error
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500

