# question-place-django
## Prerequisites
* Python3
* pip
* npm
## Creation virtual environment
```bash
$ python3 -m venv venv  
$ cd venv              
$ . bin/activate  
```
## Start Django back-end
In home folder of the repository
```bash
$ pip install -r requirements.txt
$ cd QuestionPlace                    
$ python manage.py runserver
```
## Start Vue front-end
```bash
$ cd QuestionPlace/frontend                   
$ npm i -s
$ npm run serve --fix
```
## Visualize Project
Open chrome on "http://127.0.0.1:8000"
