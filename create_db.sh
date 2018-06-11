if psql -lqt | cut -d \| -f 1 | grep -qw TestDB; then
    echo 'db exists'
    # database exists
    # $? is 0
else
    psql -a -f create_db.sql
    # ruh-roh
    # $? is 1
fi
