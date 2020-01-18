# leakyleaks.ctf

Your new trustworthy Leaking Platform

## What is this?

Whistle blowing is an important basis to conquer corruption and consipiracies!

*leakyleaks* is the new trustworthy platform which supports anonymous whistle blowing. 

It is completly anonymous and completely secure. And even better: you can run your own copy of it on your machine, as it is 100% open source.

# Install and run Instructions

- Install git, python3, python3-virtualenv

    apt install git python3 python3-virtualenv

- Clone this repo

    git clone https://github.com/leakyleaks-ctf/leakyleaks.ctf

- Change into newly created directory and create python virtualenv

    cd leakyleaks.ctf
    python3 -m virtualenv venv

- Activate virtualenv

    source venv/bin/activate

- install python dependencies

    pip install -r requirements.txt

- Set environment variable

    FLASK_APP=leakyapp flask run
