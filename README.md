# leakyleaks.ctf

Your new trustworthy Leaking Platform

## What is this?

Whistle blowing is an important basis to conquer corruption and consipiracies!

*leakyleaks* is the new trustworthy platform which supports anonymous whistle blowing. 

It is completly anonymous and completely secure. And even better: you can run
your own copy of it on your machine, as it is 100% open source.

# Install and run Instructions 

- Create and run a postgres container **according to the instructions of the postgres
  docker image** (assume --name leakdb) use the -v option to pass on persitant storage

- Create docker container and attach to it (debian based)

    docker image pull debian
    docker container run --name leakapp -p 8000:80 -it debian

- Create a private network for the apps

    docker network create leaknet
    docker network connect leaknet leakdb
    docker network connect leaknet leakapp

- Attach to app container

    docker container attach leakyapp

- Install git, python3, python3-virtualenv, libpq-dev

    apt install git python3 python3-virtualenv libpq-dev

- Clone this repo

    git clone https://github.com/leakyleaks-ctf/leakyleaks.ctf

- Change into newly created directory and create python virtualenv

    cd leakyleaks.ctf
    python3 -m virtualenv venv

- Activate virtualenv

    source venv/bin/activate

- install python dependencies

    pip install -r requirements.txt

- Set environment variable and run the app

    DATABASE_URL="postgresl://leakydb:<your_database_password_here>@leakdb/leakydb
    FLASK_APP=leakyapp flask run

# User creation

- Start the flask shell

    FLASK_APP=leakyapp flask shell

- Within the shell, instanciate a user object, add it to the database and commit the session

    u = User(username="yourusername", email="youremail")
    u.set_password("yourpassword")
    db.session.add(u)
    db.session.commit()
