# How to write / solve simplest CTF games

## Typical cmdline usage

### testing

By hand:
`./server.py` is OK. You type answer by hand.

However, when program is used, below may be useful:

Server side:
`busybox nc -ll -p 2323 -e ./server.py`

Client side:
`busybox nc 127.0.0.1 2323 -e ./client.py`

It should be equivalent to:

`socat exec:./server.py exec:./client.py`

### deploying

Server side will be equivalent to
`busybox nc -ll -p 2323 -e ./server.py`

and you see your deployment (the effect seen by other players) by
`nc 127.0.0.1 2323`

It may be better to impose some resource limit here, as in normal CTF. But as for toy CTF that is optional.

## Python explanation

Lines in scripts:

```python
#!/usr/bin/python -u
```

This line is for unbuffered python interpreter. So if the scripts are executable, then `./server.py` will be `/usr/bin/python -u ./server.py`. A common practice.

```python
x = int(raw_input())
```

`raw_input()` reads a line as string. Notice that sometimes `raw_input(prompt_string)` is used. Try out yourself by putting a string inside the argument.

```python
print >>sys.stderr, raw_input()
```

Things printed at stderr can not be seen by peer, rather it would be seen by you! Print diagnostic messages or flags here!