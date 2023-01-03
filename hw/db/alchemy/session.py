from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

engine = create_engine('postgresql://postgres:123@localhost/store')

session: Session = sessionmaker(engine)()
