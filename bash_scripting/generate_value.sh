#Create the program that will look for “Message-ID” header in the external file. 
#When found change its value to some unique value. Generate unique value without random functions usage. 
#Please do not use any counters saved outside the program.


#!/bin/sh
#===========================works for frebsd10.3===============================================
#!/bin/sh
while IFS= read -r line
do
echo $line|sed -e "s/^Message-I[dD]: <.*>$/Message-Id: <`echo $line | sha256|tr -cd 0-9`>/" >>tmp.txt
done < "$1"
cp tmp.txt $1
rm tmp.txt





#===========================works for centos7===============================================

while IFS= read -r line
do
echo $line|sed -e "s/^Message-I[dD]: <.*>$/Message-Id: <`echo $line|sha256sum|tr -cd 0-9 | head -c 30`>/" >>tmp.txt
done < "$1"
cp tmp.txt $1
rm tmp.txt
