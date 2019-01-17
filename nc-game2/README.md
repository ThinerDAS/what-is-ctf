# How to solve simplest CTF games with pwntools

## Typical cmdline usage

### deploying

Server side is same as the [last game](../nc-game).

`busybox nc -ll -p 2323 -e ./server.py`

For client side, simply

`./exp.py`

## Python explanation

Lines in scripts:

```python
#!/usr/bin/python -i
```

After `exp.py` you may be interested in certain variable, `-i` provide an interactive shell after the script.

```python
from pwn import *

context.arch = 'amd64'
context.log_level = 'debug'
```

By convention scriptors use `from pwn import *` only in pwntools.
`log_level` is for IO dump on terminal, so if you comment the last line, the world will be in peace and no noisy output. Use this line when you want.

```python
r = remote(host, port)
```

Instead of providing host / port in `nc` args, in pwntools you provide them directly to the function, and use `send` / `recv` for IO.

```python
r.interactive()
```

You can switch to `nc` mode anytime with this line.

