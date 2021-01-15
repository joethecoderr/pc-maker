#Connection
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://admin:password@pcmakerinstance.c15oncijbytw.us-east-2.rds.amazonaws.com/dbname') # connect to server
#engine.execute(" CREATE TABLE low_req_pcbenchmark (     id int not null primary key,     Game_Name varchar(255),     Descr varchar(255),     OS varchar(255),     Processor varchar(255),  Ram varchar(255),  Graphics varchar(255),  DirectX varchar(255),      size varchar(255),  Notes varchar(255)         )") 

Session = sessionmaker(bind=engine)

Base= declarative_base()
