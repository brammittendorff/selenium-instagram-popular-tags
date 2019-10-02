import sys
import time
import argparse
from subprocess import Popen

parser = argparse.ArgumentParser(description='Instagram Popular Tags')
parser.add_argument('-s', '--source', help='location of the wordlist file')

args = parser.parse_args()

nodeTotal = 5
batchTotal = 10

if args.source:
    words = []
    with open(args.source, "r") as ins:
        for line in ins:
            words.append(line)

    processes = []

    for i in range(len(words)):
        chrome_cmd = "python3 start.py -w {}".format(words[i])
        processes.append(Popen(chrome_cmd, shell=True))
        if (i % batchTotal) == 0:
            time.sleep((batchTotal/nodeTotal)+1)

    for i in range(len(words)):
        processes[i].wait()