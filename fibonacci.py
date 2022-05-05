# n=5-> 0 1 1 2 3
# n=10-> 0 1 1 2 3 5 8 13 21 34

def fibonacii(n):
    l = []
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n > 2:
        start = 0
        next = 1
        current = 0
        l.append(start)
        l.append(next)
        while n-2 != 0:
            current = start + next
            start = next
            next = current
            l.append(current)
            n -= 1
        return l

if __name__ == '__main__':
    print(fibonacii(10))