# Selenium Instagram Tags From Wordlist

You can clone this repository to see the effect of multiple nodes of selenium under a hub. When using 5 nodes it will screenshot google.com 5 times / second the amount of parallel jobs. But when using 10 nodes you will see that it can not handle 10 nodes at the same time so sometimes it will use 8 nodes / second and sometimes less.

# Installation

```bash
pip3 install -r requirements.txt
```

# Usage

Run docker:

```bash
docker-compose up --build
```

To run parallel:

```bash
python3 parallel_run.py  -s wordlist.txt
```

Show latest 100 results sorted by tag amount

```
./show.sh | sort -nr | head -n 100
```

To watch the process happening in a other terminal

```
watch -d -n 1 './show.sh | sort -nr | head -n 100'
```
