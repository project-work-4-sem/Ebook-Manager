#! /bin/bash
#memory usage
ps -e -orss=,pcpu=,pid=,args= | sort -b -k1,1nr
exit 0