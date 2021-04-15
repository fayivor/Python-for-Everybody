fib = [ 0, 1]
for index in range(20):
        sum= fib[-1] + fib[-2]
        fib.append(sum)
print(fib)
