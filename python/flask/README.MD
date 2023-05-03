https://rest-apis-flask.teclado.com/docs/course_intro/
create models 
>>> from app import app, db
>>> app.app_context().push()
>>> db.create_all()