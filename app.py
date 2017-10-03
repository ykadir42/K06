#Jawadul Kadir
#SoftDev1 pd7
#HW6 -- Echo Echo Echo
#2017-10-03

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def link():
    return '<a href="/TextInput"">Click here to Login</a>'

@app.route("/TextInput")
def text_input():
	return render_template('TextInput.html')

@app.route("/Greeting")
def greeting():
	print "***APP***"
	print app

	print "\n"
	print "\n"
	print "\n"

	print "***REQUEST***"
	print request

	print "\n"
	print "\n"
	print "\n"


	print "***REQUEST.ARGS***"
	print(request.args)

	print "\n"
	print "\n"
	print "\n"


	print "***REQUEST.HEADERS***"
	print(request.headers)

	print "\n"
	print "\n"
	print "\n"


	print "***REQUEST.METHOD***"
	print(request.method)

	print "\n"
	print "\n"
	print "\n"


	print "***REQUEST.FORM***"
	print(request.form)

	print "\n"
	print "\n"
	print "\n"

	print "***END***"
	print "\n"
	print "\n"
	print "\n"



	return render_template('Greeting.html', input = request.args['text_input'], method = request.method)


if __name__ == "__main__":
    app.debug = True
    app.run()
