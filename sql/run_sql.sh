#!/bin/bash

user=$1
file=$2

psql -h id-hdb-psgr-cp76.ethz.ch -U $user -d ivtdata -p 5432 -f $file --password