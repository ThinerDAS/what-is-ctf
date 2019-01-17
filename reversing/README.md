# reversing

## Crackme nature

Crackmes compose most of the reversing challenges. Writing a crackme is easy, it is like writing a verifier of input.

Notice that your verifier should react as correct on your designated input and incorrect on all other inputs.

And also rarely noticed is that, your algorithm should be theoretically solvable. Hash algorithm like SHA256 on a long enough flag is UNSOLVABLE, and so do public-key cryptography and current symmetric encryption with the key to be solved as flag. Briefly it is common practice that you write the solution script before submitting the challenge if you are a challenge writer.

Also, if you are not a CTF player, chances are that you have made things wrong by misunderstanding what CTF players are doing. Gary, my friend, has made things wrong by composing a group theory exercise while writing the crackme checking the answer barely. CTF players have access of the binary and they are only reversing the binary, and as a result, a mathematical crackme should write only relevant math inside the checker logic.

## Export

You need to provide CTF players (usually) a binary, rather than your source code.

```shell
gcc crackme.c -o crackme -s
```

`-s` indicate that you want to strip all symbols (function names, variable names, etc) off the binary. If you feel that your binary is too complex, you may want to keep the function names.

Other flags useful for deployment include:
* `-O`, `-O3`, `-Os`: Optimization. `-O3` is commonly used highest optimization level, `-Os` is optimize for size (so the compiler will refrain to use too many inlines and unrollings).
* `-march=native`: Normally including this flag will make compiler generate more state-of-the-art instructions for your binary, depending on your computer CPU.

Also you may use `clang` instead of `gcc`, as `clang` compiles certain codes better and is generally faster.

It is commo practice to see in IDA the resulting binary.

## Solving

One need to find out the algorithm and do the inverse.

For the given challenge, knowing that it is simple xor and comparing, we find the data and xor it back.

In brief, this line print out the flag:

```python
print ''.join(chr(i^ord(j)) for i,j in zip(range(64),open('crackme').read()[0x6e0:0x720]))
```

## Other types of reversing challenges

CTF is about achieving. So reversing can be related to many aspects of CTF, not limited to crackmes. Be imaginative!