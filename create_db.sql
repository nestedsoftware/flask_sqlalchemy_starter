\set username `echo "$SQLALCHEMY_USERNAME"`
\set dbname `echo "$SQLALCHEMY_DBNAME"`

CREATE DATABASE :"dbname"
    WITH 
    OWNER = :'username'
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;

    
