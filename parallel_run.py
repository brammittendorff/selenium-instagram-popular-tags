from subprocess import Popen

processes = []

for counter in range(30):
    chrome_cmd = 'python3 start.py'
    processes.append(Popen(chrome_cmd, shell=True))

for counter in range(30):
    processes[counter].wait()