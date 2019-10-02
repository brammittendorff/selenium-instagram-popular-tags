from subprocess import Popen

processes = []

for counter in range(20):
    chrome_cmd = 'python3 start.py'
    processes.append(Popen(chrome_cmd, shell=True))

for counter in range(20):
    processes[counter].wait()