#!/bin/bash

source db_config.env
mysql -u"$MYSQL_ROOT_USER" -p"$MYSQL_ROOT_PASS" <<EOF
CREATE DATABASE IF NOT EXISTS \`$NEW_DB\`;
CREATE USER IF NOT EXISTS '$NEW_USER'@'localhost' IDENTIFIED BY '$NEW_PASS';
GRANT ALL PRIVILEGES on \`$NEW_DB\`.* TO '$NEW_USER'@'localhost';
FLUSH PRIVILEGES;
EOF

echo "User '$NEW_USER' and database '$NEW_DB' created with privileges."

