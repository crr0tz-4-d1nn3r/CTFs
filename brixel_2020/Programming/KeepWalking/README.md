#  Keep walking...
10

This is a challenge to test your basic programming skills.

Pseudo code:

Set X = 1

Set Y = 1

Set previous answer = 1

answer = X * Y + previous answer + 3

After that => X + 1 and Y + 1 ('answer' becomes 'previous answer') and repeat this till you have X = 525.

The final answer is the value of 'answer' when X = 525. Fill it in below.

Example:

5 = 1 * 1 + 1 + 3

12 = 2 * 2 + 5 + 3

24 = 3 * 3 + 12 + 3

........................

........................

This flag is not in the usual format, you can enter it with or without the brixelCTF{flag} format


## Flag
```
48373851
```

## Solution

Python example of described algorithm.

```python
x = 1
y = 1
prev_ans = 1

while x < 526:
    ans = x * y + prev_ans + 3
    x += 1
    y += 1
    prev_ans = ans

print('x = ' + str(x))
print('ans = ' + str(ans))
```