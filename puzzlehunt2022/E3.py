# Fibonacci Redifined

# iterative string fibonacci
"""
    fib(1) ->        '0'
    fib(2) ->        '1'
    fib(3) ->       '01'
    fib(4) ->      '101'
    fib(5) ->    '01101'
    fib(6) -> '10101101'
    
    Observation: after fib(2), digits are added to prefix while suffix remains constant.
    Hence, can stop well before 1000th string to get last 20 digits
"""

def fibonacci(digits):
    # base cases
    last = '1'
    secondLast = '0'
    
    curr = '01'
    
    # stop when length is sufficient
    while len(curr) < digits:
        curr = secondLast + last 
        secondLast = last 
        last = curr 
    return curr[-digits:]

    
def main():
    # only need last 20 digits so can stop fairly early
    print(fibonacci(20))
    
if __name__ == "__main__":
    main()