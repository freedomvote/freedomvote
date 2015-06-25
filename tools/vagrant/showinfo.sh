#!/bin/bash

PUBLICIP=$(
	ip addr show dev eth2 \
	| awk ' /inet/ { sub(/\/.*/, "", $2); print $2; exit }'
)

PRIVATEIP=$( \
	ip addr show dev eth1 \
	| awk ' /inet/ { sub(/\/.*/, "", $2); print $2; exit }'
)

PRIVATEIP=`printf '%-15s'  $PRIVATEIP`
PUBLICIP=`printf  '%-15s'  $PUBLICIP`

echo ""
echo "+------------------------------------------------------------------------+"
echo "|                                                                        |"
echo "| Welcome to the Freedom Vote environment. You can now access the        |"
echo "| application and several tools as follows:                              |"
echo "|                                                                        |"
echo "|   * Application:          Browse to http://127.0.0.1                   |"
echo "|   * Application (alt):    Browse to http://$PRIVATEIP             |"
echo "|   * Application (public): Browse to http://$PUBLICIP             |"
echo "|   * PHPMyAdmin   Browse to http://127.0.0.1/phppgadmin                 |"
echo "|   * SSH access:  Commandline: vagrant ssh                              |"
echo "|                                                                        |"
echo "| User accounts to work with:                                            |"
echo "|     Application:     admin             / 123qwe                        |"
echo "|     phpPgAdmin:      freedomvote       / vagrant                       |"
echo "|     Shell:           vagrant           / vagrant                       |"
echo "+------------------------------------------------------------------------+"
echo ""
