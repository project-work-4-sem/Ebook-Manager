cat /proc/cpuinfo | grep 'model name' | uniq
cpu_load=`top -b -n1 | grep "Cpu(s)" | awk '{print $2}' | awk -F . {'print $1'}`
echo "Utilisation : \n" $cpu_load "%"
lscpu | grep 'CPU MHz'
processes=`ps aux | wc -l`
echo "Processes: " $processes
threads=`ps -eo nlwp | tail -n +2 | awk '{ num_threads += $1 } END { print num_threads }'`
echo "Threads: " $threads
lscpu | grep -E '^Thread|^Core|^Socket|^CPU\('
uptime | awk '{print $1}'
exit 0