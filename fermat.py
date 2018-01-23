import random


def get_random(s):
    p = random.sample(s, 1)[0] # time: O(n)
    s.remove(p) #time: O(n)
    return p


def prime_test(N, k):
    # You will need to implements this function and change the return value.

    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.

    # Should return one of three values: 'prime', 'composite', or 'carmichael'
    k = check_k(k,N) # time O(n) were n is the number of bits in N

    a_vals = set(range(2,N))
    for a in range(0,k):
        a = get_random(a_vals)
        modded = mod_exp(a,N-1,N)
        if modded != 1:
            return 'composite'
        if is_carmichael(N,a):
            return 'composite'


    return 'prime' #test


def check_k(k,N): # time O(n) were n is the number of bits in N
    if k > (N - 2): # time O(n) were n is the number of bits in N which will almost certainly be larger that 2
        k = N - 2 # time O(n) were n is the number of bits in N which will almost certainly be larger that 2
    return k


def mod_exp(x, y, N): #O(n^2)
    # You will need to implements this function and change the return value.
    if y == 0: #O(n)
        return 1
    z = mod_exp(x,y//2,N) #O(n^2*log(n))
    if y % 2 == 0: #O(n^2)
        return (z**2) % N #O(n^2)
    else:
        return (x * (z**2)) % N #O(n^2)


def probability(N,k):
    # You will need to implements this function and change the return value.
    k = check_k(k,N)

    return 1 - ((1/2)**k)


def is_carmichael(N,a):
    ctr = 0
    u = N - 1
    while (u % 2) == 0: # time: O(n^2*log(n))
        u = u/2 # time: O(n^2)
        ctr += 1 # time: O(n)

    modded = mod_exp(a,u,N) # time: O(n^2)

    if modded == 1:
        return False

    prev = modded
    for x in range(0,ctr+1):
        modded = mod_exp(modded,2,N)
        if modded == 1:
            if prev != N - 1:
                return True
            else:
                return False
        else:
            prev = modded
    # You will need to implements this function and change the return value.
    return True


print(is_carmichael(561,67))