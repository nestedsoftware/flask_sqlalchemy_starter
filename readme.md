<h1>Flask app boilerplate with SQLAlchemy and Alembic</h1>

<h2>Overview</h2>

This project includes the basic boilerplate required to integrate SQLAlchemy with Flask. Alembic database upgrading is included. _Flask-SQLAlchemy extension is not used_: Among other things, a custom base class for SQLAlchemy declarative models is therefore not required. 

<h2>Installation</h2>

These instructions may be Ubuntu linux-specific in some places. Python 3.6+ and pipenv are required.

 * create `env.sh` file and add the following environment variables (substitute `~/dev/flask_sqlalchemy_starter `, `username`, `userpassword`, `server`, and `dbname` accordingly): 

 ```bash
 export PYTHONPATH=~/dev/flask_sqlalchemy_starter 
 export SQLALCHEMY_USERNAME=username
 export SQLALCHEMY_PASSWORD=userpassword
 export SQLALCHEMY_SERVER=server
 export SQLALCHEMY_DBNAME=dbname
export SQLALCHEMY_URL="postgresql://$SQLALCHEMY_USERNAME:$SQLALCHEMY_PASSWORD@$SQLALCHEMY_SERVER/$SQLALCHEMY_DBNAME"
```
> You don't have to use postgresql as the db of course. 
> * If you wish to use slite in memory, set SQLALCHEMY_URL to `"sqlite:///:memory:"` (see env_test.sh) 
> * If you want to use postgresql and it's not installed on your system yet, I've included instructions for postgresql installation on Ubuntu linux at the end of this file.

* install: `$ pipenv install`
* install with dev dependencies (unit testing): `$ pipenv install --dev`
* start python virtual environment: `$ pipenv shell`
* run: `$ source env.sh && FLASK_ENV=development flask run` 
  * `http://localhost:5000/` should show json greeting
  * `http://localhost:5000/messages` should show json list of messages
* run tests: `$ source env_test.sh` followed by `$ pytest -v`

<h2>Database setup and migration</h2>

* `$ source env.sh`
* `$ ./create_db.sh`
* `cd flask_sqlalchemy_starter && alembic upgrade head && cd ..`
* `$ psql -a -f populate_db.sql` (pre-populates db with a few rows of data)

<h2>Install postgresql on Ubuntu</h2>

* `$ echo "deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main" | sudo tee /etc/apt/sources.list.d/pgdg.list`

>'bionic' in the above command refers to the codename for ubuntu linux 18.04. Update as required for appropriate linux version

* `$ wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -`
* `$ sudo apt-get install postgresql-10 pgadmin4`

> You can omit pgadmin4 if you don't want to use it. 

Create a db user corresponding to your linux username and give that user a db password (not the same as your linux password):

* `$ sudo -u postgres createuser -s "$SQLALCHEMY_USERNAME"`
* `$ psql -a -f update_user_password.sql`

