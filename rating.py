from flask import Flask, render_template, flash, url_for, redirect , g
from busroutes import busRoutes

app = Flask(__name__)
app.config['SECRET_KEY'] = '4f6c484fa2d098ccb271bf1f07173423'

@app.route("/")
@app.route('/busroutes', methods=['GET', 'POST'])
def destination():
    form = busRoutes()
    if form.validate_on_submit():
        flash(f'{form.comment1.data}!')
        return redirect("busroutenotes.html")
    return render_template("busroutes.html", title="Bus Routes", form=form)



if __name__ == "__main__":
    app.run(debug=True)
