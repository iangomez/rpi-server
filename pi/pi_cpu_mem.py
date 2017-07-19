# Function: read_cpu
# This function reads the percent memory used by the CPU.
def read_cpu():
	output = subprocess.check_output(["grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage}'"], shell=True)
	config.cpu = str(output)[:2]

# Function: read_memory
# This function reads the percent memory available on the raspberry pi.
def read_memory():
	output = subprocess.check_output(["df -h | grep /dev/root | cut -d ' ' -f 14-"], shell=True)
	config.memory = str(output)[:2]