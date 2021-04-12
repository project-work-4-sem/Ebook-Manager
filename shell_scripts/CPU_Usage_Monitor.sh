#!/bin/bash
hostname=$(hostname)
critical=90 #SET BY THE USER
warning=75 #SET BY THE USER
WarningMail="sohambhardwaj17@gmail.com" # SET BY THE USER
mkdir -p Log_Files
logfile=Log_Files/cpusage-`date +%h%d%y`.log
touch $logfile

cpu_load=`top -b -n1 | grep "Cpu(s)" | awk '{print $2}' | awk -F . {'print $1'}`

if [ -n $warning -a -n $critical ]; then
	if [ "$cpu_load" -ge "$warning" -a "$cpu_load" -lt "$critical" ]; then
		echo "`date +%H:%M:%S` STATUS = WARNING | CPU LOAD = $cpu_load on HOST $hostname " >> $logfile
		echo "STATUS=WARNING | CPU LOAD = $cpu_load on Host $hostname" | mail -s "CPU LOAD WARNING" $WarningMail
		exit 1
	elif [ "$cpu_load" -ge "$critical" ]; then
		echo "`date +%H:%M:%S` STATUS = CRITICAL | CPU LOAD = $cpu_load on HOST $hostname " >> $logfile
		echo "STATUS=CRITICAL | CPU LOAD = $cpu_load on Host $hostname" | mail -s "CPU LOAD CRITICAL" $WarningMail
		exit 2
	else
		echo "`date +%H:%M:%S` STATUS = OK | CPU LOAD = $cpu_load on HOST $hostname " >> $logfile
		echo "Log File Generated"
		exit 0
	fi
fi

