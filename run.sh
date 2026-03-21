#!/bin/bash
source venv/bin/activate
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
chmod +x run.sh
venv\Scripts\activate
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
