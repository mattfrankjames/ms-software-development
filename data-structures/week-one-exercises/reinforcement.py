# get the dividend and coerce to integer
dividend = int(input('Give me a number to divide '))

# get the divisor and coerce to integer
divisor = int(input('Give me a number to divide by '))


def get_multiple(n, m):
    # check if we have no remainder when dividing the dividend by the divisor, meaning the dividend is a multiple of the divisor return true

    if(n % m == 0):
        print('{0} is a multiple of {1}'.format(n, m))
        return True
    # if not divisible by the divisor, return false
    else:
        print('{0} is NOT a multiple of {1}'.format(n, m))
        return False

# call the function with our input numbers


get_multiple(dividend, divisor)
