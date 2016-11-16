#!/bin/bash
read -a array -p "enter elements of array:"
for i in "${array[@]}"
do
test $i -lt ${min:=$i} && min=$i
done

for g in "${array[@]}"
do
test $g -gt ${max:=$g} && max=$g
done

echo "min value= $min"
echo "max value= $max" 
