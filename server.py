from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)


@app.route('/create', methods=['POST'])
def route_create():
    print('POST request received! Created !')
    session['note'] = request.form['note']
    return redirect('/')


@app.route('/')
def route_index():
    # note_text = None
    # if 'note' in session:
    #     note_text = session['note']
    return render_template('form.html',estimation="2.5",business_value="1000",button="Create")  # , note=note_text)


if __name__ == "__main__":
    # app.secret_key = 'Content changed'  # Change the content of this string
    app.run(
        debug=True,  # Allow verbose error reports
        port=5000  # Set custom port
    )
