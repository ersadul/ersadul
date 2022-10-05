from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# Flask             : web framework for python
# render_template   : formatting template
# request           : to handle request 
# redirect          : to redirect into a path
# SQLAlchemy        : py SQL toolkit and ORM
# datetime          : get a date time


# instantiate object of Flask class, used to know where to look for resource: template, static
app = Flask(__name__)
# set database config for app 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# initialize our db object and pass to our app
db = SQLAlchemy(app)

# create model for our database
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

# this route decorator tell what URL should trigger our function
# add method when we in that route
@app.route("/", methods = ['POST', 'GET'])
def index():

    # check if there is a request from interface
    if request.method == 'POST':
        # get data from form request
        task_content = request.form['content']

        # check if the content that requested empty or not
        # if empty, do:
        if task_content == '':
            # query to check is there any data inside database, and show all
            tasks = Todo.query.order_by(Todo.date_created).all()
            
            # additional return value: warning True, to give a warn that we can't leave the task box empty
            return render_template('index.html', warning=True, tasks=tasks)

        # create a model
        new_task = Todo(content=task_content)
        # try to add and commit change into database
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'you have an issue when you add task'
    else:
        # show tasks
        tasks = Todo.query.order_by(Todo.date_created).all()

        # return index.html and show_tasks value(from db), if there is no request 
        return render_template('index.html', tasks=tasks)

# make a route for delete model
@app.route('/delete/<int:id>')
def delete(id):
    # query to get id, and pass 404 if not available
    task = Todo.query.get_or_404(id)

    try:
        db.session.delete(task)
        db.session.commit()
        return redirect('/')
    except:
        return 'you have an issue when you delete task'

# make a route for update model
@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    task = Todo.query.get_or_404(id)

    # if catch POST request, do:
    if request.method == 'POST':

        # get data from form request and assign its value to task.content
        task.content = request.form['content']

        # commit change into database
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'you have an issue when you update task'

    else:
        return render_template('update.html', task=task)

# check if this app execute direcly, not imported
if __name__ == '__main__':
    app.run(debug=True)