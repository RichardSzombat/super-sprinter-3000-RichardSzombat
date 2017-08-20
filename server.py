from flask import Flask, render_template, redirect, request, session
import csv
import functions

app = Flask(__name__)


@app.route('/create', methods=['POST', 'GET'])
def route_create():
    print("1")
    new_story = request.form
    print("2")
    functions.save_story(new_story)
    print("3")
    #form_to_file = functions.write_to_file2(form)
    return redirect('/')


@app.route('/story', methods=['POST', 'GET'])
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
