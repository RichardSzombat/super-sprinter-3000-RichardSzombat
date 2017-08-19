from flask import Flask, render_template, redirect, request, session
import csv

app = Flask(__name__)


@app.route('/create', methods=['POST', 'GET'])
def route_create():
    if request.method == 'POST':
        print("This was a POST")
        form=request.form
        title = request.form['title']
        story=request.form['story']
        criteria=request.form['criteria']
        business_value=request.form['business_value']
        estimation = request.form['estimation']
        with open ("lists.csv","w") as lists:
            for value in form.items():
                print(value)
                row=value[1]+";"
                lists.write(row)
        return redirect('/')


@app.route('/story')
def create_story():
    return render_template('form.html', estimation="2.5", business_value="1000", button="Create")  # , note=note_text)

@app.route('/')
@app.route('/list')
def show_list():
    return render_template('list.html')

if __name__ == "__main__":
    # app.secret_key = 'Content changed'  # Change the content of this string
    app.run(
        debug=True,  # Allow verbose error reports
        port=5000  # Set custom port
    )
