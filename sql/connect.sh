#!/bin/bash

user=$1

echo "Connecting user ${user}"

psql -h id-hdb-psgr-cp76.ethz.ch -U $user -d puv -p 5432 --password