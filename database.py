import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = sqlalchemy.create_engine('sqlite:///database.db', echo=False)
Session = sessionmaker(bind=engine)
db = declarative_base()
session = Session()
create = True

class Users(db):
    __tablename__ = "users"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    date = sqlalchemy.Column(sqlalchemy.String)
    name  = sqlalchemy.Column(sqlalchemy.String)
    score = sqlalchemy.Column(sqlalchemy.Integer)

if create == True:
    db.metadata.create_all(engine)

def addEntry(date, name, points):
    user = Users(date=date, name=name, score=points)
    session.add(user)
    session.commit()

def sortByScore():
    qry = session.query(Users).order_by(sqlalchemy.desc(Users.score)).limit(5).all()
    return qry

