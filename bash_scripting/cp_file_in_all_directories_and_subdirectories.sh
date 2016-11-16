#!/bin/sh
for i in $1/*
do
     if [ -d "$i" ]
     then
     cp $2 "$i"
     fi
done


OR


#!/bin/sh
v=`ls -FR $1|grep -E '/[^$]'|tr -d :`
for dir in $v
do
cp $2 $dir
done
