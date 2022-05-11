# DispuutStropdas

Home page
https://github.com/gmadurov/DispuutStropdas

Issues:
https://github.com/gmadurov/DispuutStropdas/issues

1. Work on an issue then upload your code to that issue number and do a merge request
   a. if there isnt an issue make one with what you are trying to solve and then upload to that issue number

I recomend not mixing the modules you need for webdev and the modules you normally use. For this I use a virtual enviroment(pipenv)

to install it just do

```
pip install pipenv
```

then to initialize it

```
pipenv install
```

if you want to install a module or modules from a file "requirements.txt"

```
pipenv install module
pipenv install -r requirements.txt
```

you can also add modules to that file by doing within the environement

```
pip freeze > requirements.txt
```

To use get a shell within the environement use

```
pipenv shell
```

to run something within the environement from outside
³²¡¤€¼½¾‘’¥äå
```
pipenv run [command]
```

To deactivate the environement and remove it

```
deactivate

pipenv --rm
```


```
/usr/local/bin/heroku login
/usr/local/bin/heroku git:remote -a stropdas
/usr/local/bin/heroku git push heroku main

```