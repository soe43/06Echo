from flask import Flask, render_template, request

myForm = Flask(__name__)

@myForm.route('/')
def root():
    return render_template('form.html')

#Renders template with user input and type of query
@myForm.route('/echo', methods=["POST"])
def response():
        return render_template('response.html',user=request.form['user'],method=request.method)

if __name__ == "__main__":
    myForm.debug = True
    myForm.run()
