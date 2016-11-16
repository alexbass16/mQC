#!/bin/sh

username=root
password=root
host=localhost

template="mysql -u $username -p$password -h $host -e"

$template "select current_timestamp()" |sed -e "/current_timestamp()/d" | tr '\n' ',' >>$1
$template "show status like 'threads_connected';" |sed -e "/Variable_name/d" |awk '{print $2}' |tr '\n' ',' >> $1
$template "show global status like 'questions';" |sed -e "/Variable_name/d" | awk '{print $2}' | tr '\n' ',' >> $1
$template "show status like 'slow_queries';" | sed -e "/Variable_name/d" | awk '{print $2}' | tr '\n' ',' >> $1
$template "show status like 'open_tables';" | sed -e "/Variable_name/d" | awk '{print $2}' | tr '\n' ','  >> $1
#$template "show engine innodb status" | tr "\\" "\n" | cut -c 2- | awk '/Buffer pool size/{print $4}' | tr '\n' ','>> $1
$template "show engine innodb status" | tr "\\" "\n" | cut -c 2- | awk '/Total memory allocated/{print $4}'| sed -e 's/;//g' >> $1



#format:
#date, thread_connected, questions, slow_queries, open_tables, total_memory_allocated

