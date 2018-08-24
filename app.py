from flask import Flask, render_template
from database_setup import Users, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:////home/bhanu/Documents/final_build/flask2/marvin1.db')
Base.metadata(bind = engine)

app = Flask(__name__)

DBsession = sessionmaker(bind=engine)
session = DBsession()
DBsession.autoflush = True

@app.route('/')
def index():
    return render_template('dashboard.html')
if __name__ == '__main__':
    app.run(port= 8000, host ='0.0.0.0', debug = True)
