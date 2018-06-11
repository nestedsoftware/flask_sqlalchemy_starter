\set dbusername `echo "$SQLALCHEMY_USERNAME"`
\set dbpassword `echo "$SQLALCHEMY_PASSWORD"`

ALTER USER :dbusername PASSWORD :'dbpassword';    
