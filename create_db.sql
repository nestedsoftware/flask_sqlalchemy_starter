\set username `echo "$SQLALCHEMY_USERNAME"`

CREATE DATABASE "TestDB"
    WITH 
    OWNER = :'username'
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;

    
