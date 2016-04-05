from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from tornado.options import options, define


define("db_host", default="localhost", help="DB host", type=str)
define("db_port", default=5432, help="DB port", type=int)
define("db_user", default=None, help="DB username", type=str)
define("db_pass", default=None, help="DB password", type=str)
define("db_name", default=None, help="DB database name", type=str)
define("db_echo", default=False, help="DB debug", type=bool)

engine = None
Base = None


def connect_db():
    return create_engine('postgresql://%s:%s@%s:%s/%s' % (
        options.db_user, options.db_pass, 
        options.db_host, options.db_port, 
        options.db_name
    ), convert_unicode=True, echo=options.db_echo)


def create_session_factory():
    global engine, Base
    
    engine = connect_db()
    session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

    Base = declarative_base()
    Base.query = session.query_property()
    Base.metadata.create_all(engine)

    return session
