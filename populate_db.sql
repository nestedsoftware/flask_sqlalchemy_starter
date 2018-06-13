\set dbname `echo "$SQLALCHEMY_DBNAME"`

\c :"dbname"

TRUNCATE TABLE "messages";

INSERT INTO "messages" (message) VALUES ('Hello, friend! Welcome!');
INSERT INTO "messages" (message) VALUES ('How are you doing today?');
INSERT INTO "messages" (message) VALUES ('I hope this message finds you well!');
