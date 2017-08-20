from flask import Flask, render_template, redirect, request, session
import functions

app = Flask(__name__)


@app.route('/create', methods=['POST', 'GET'])
def route_create():
    new_story = request.form
    functions.save_story(new_story)
    return redirect('/')


@app.route('/story', methods=['POST', 'GET'])
@app.route('/story/<int:id_>', methods=['GET'])
def create_story(id_=None):
    print(id_)
    if id_:
        all_story = functions.get_story()
        try:
            index = functions.find_index_by_id(id_, all_story)
        except ValueError:
            return "No such story"
        current_story = all_story[index]
        title = current_story[1]
        story = current_story[2]
        criteria = current_story[3]
        business_value = current_story[4]
        estimation = current_story[5]
        status = current_story[6]
        return render_template('form.html', title=title,
                               id_=id_,
                               story=story,
                               criteria=criteria,
                               estimation=estimation,
                               business_value=business_value,
                               status=status)
    else:
        return render_template('form.html', id_=id_)


@app.route("/story/<int:id_>", methods=['POST'])
def save_edited_story(id_):
    edited_story = request.form
    functions.save_edited(id_, edited_story)
    return redirect("/")


@app.route("/delete_story/<int:id_>", methods=['POST','GET'])
def delete_story(id_):
    all_story=functions.get_story()
    new_all_story=functions.delete_story(id_,all_story)
    functions.write_to_file(new_all_story)
    return redirect("/")


@app.route('/')
@app.route('/list')
def show_list():
    all_story = functions.get_story()
    return render_template('list.html', all_story=all_story)


if __name__ == "__main__":
    # app.secret_key = 'Content changed'  # Change the content of this string
    app.run(
        debug=True,  # Allow verbose error reports
        port=5000  # Set custom port
    )
