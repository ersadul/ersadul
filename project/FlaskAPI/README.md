# Python Flask 
## Description
I'm trying to build first API project, using [Flask] web framework for Python.
I use two learning source: [freeCodeCamp][fcc] and [Caleb Curry][cc]. In this case, we make a To-do list app. We can do create, read, update, and delete task.
![image](https://user-images.githubusercontent.com/13926075/194043888-d8f2a425-dccb-44e9-8893-e15d6f3a5a2a.png)

## Run App
main library that used in this app are flask, flask_sqlalchemy, and datetime.
we may run this app anyway by 
```sh
py app.py
```
but if there is not available dependencies, you must install it first. list of dependency in requirement.txt file. You can create virtual environment to isolate dependency between your app and main OS. 

```sh
py -m venv .venv
.venv/Scripts/activate
```
> Note: `.venv/Scripts/activate` (windows), `source .venv/bin/activate` (mac) to enter virtual env

after you inside venv, install dependenies. then run the file
```sh
pip install -r requirements.txt
```

   [flask]: <https://flask.palletsprojects.com/en/2.2.x/>
   [fcc]: <https://www.youtube.com/watch?v=Z1RJmh_OqeA>
   [cc]: <https://www.youtube.com/watch?v=qbLc5a9jdXo>
