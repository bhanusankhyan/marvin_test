from flask import Flask, render_template
from database_setup import Users, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:////home/bhanu/Documents/final_build/flask4/marvin1.db')
Base.metadata.bind = engine

app = Flask(__name__)

DBsession = sessionmaker(bind=engine)
session = DBsession()
DBsession.autoflush = True


@app.context_processor
def Dashboard_details():
    navbar_items = {'Home':'/','Components':[{'name':'title1','link':'#'},{'name':'title2','link':'#'}], 'Dropdown':[{'name':'title1', 'link':'#'},{'name':'title2','link':'#'}]}
    user_menu_items = [{'name':'Profile','link':'#','class':'fe fe-user'},{'name':'Settings','link':'#','class':'fe-settings'},
    {'name':'Inbox','link':'#','class':'fe fe-mail'},{'name':'Message','link':'#','class':'fe-send'},
    {'name':'Need Help?','link':'#','class':'fe-help-circle'},{'name':'SignOut','link':'#','class':'fe-log-out'}]
    return dict(navbar_items = navbar_items,user_menu_items = user_menu_items,type = type, str = str)



@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host = '0.0.0.0',port= 8000, debug = True)
