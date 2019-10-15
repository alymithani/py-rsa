import time
import random

def lcm(a,b):
    # Returns the least common multiple of ints a and b
    i = 1
    c = a * b
    while i <= c:
        if i % a == 0 and i % b == 0:
            return i
        i += 1

def gdc(a,b):
    # Returns the greatest common denominator between ints a and b
    if b == 0:
        return a
    return gdc(b,a%b)

def is_prime(a):
    # Returns boolean based on if int input is prime
    if a % 2 == 0 or a == 1:
        return False
    sqrt = a**(1/2)
    i = 3
    while i <= sqrt:
        if gdc(a,i) != 1:
            return False
        i += 2
    return True

def random_prime(min,max):
    # Returns random prime number within a given range
    val = random.randrange(min,max)
    while not is_prime(val):
        val = random.randrange(min,max)
    return val

def generate_key(p,q):
    # Generates a public and private key using two prime integers as inputs
    if not is_prime(p):
        raise Exception('input value {} is not prime.'.format(p))
    if not is_prime(q):
        raise Exception('input value {} is not prime.'.format(q))
    n = p * q
    public_key = [n]
    private_key = [n]
    λ = lcm(p - 1,q - 1)
    e = 2
    while e < λ:
        if gdc(e,λ) == 1:
            break
        e += 1
    d = 2
    while (e*d) % λ != 1:
        d += 1
    public_key.append(e)
    private_key.append(d)
    return public_key, private_key

def encrypt(m,public_key):
    # Encrypts int m using list public_key containing n and e
    n = public_key[0]
    if m >= n:
        raise Exception('message m must be less than n, {}, in public key.'.format(n))
    e = public_key[1]
    return (m**e) % n

def decrypt(c,private_key):
    # Decrypts int c using list private_key containing n and d
    n = private_key[0]
    if c >= n:
        raise Exception('cipher c must be less than n, {}, in private key.'.format(n))
    d = private_key[1]
    return (c**d) % n

def factor_time(n):
    # Returns string representing time taken to factor integer input n
    start_time = time.time()
    factors = []
    i = 2
    while n > 1:
        if n % i == 0:
            n = n // i
            factors.append(i)
        else:
            i += 1
    total_time = time.time() - start_time
    if total_time < (10 ** -3):
        total_time = total_time * (10 ** 6)
        time_string = str(total_time)[0:4] + ' microseconds'
    elif total_time < 1:
        total_time = total_time * (10 ** 3)
        time_string = str(total_time)[0:4] + ' milliseconds'
    else:
        time_string = str(total_time)[0:4] + ' seconds'
    if time_string[3] == '.':
        time_string = time_string[0:3] + time_string[4:]
    return factors,time_string
