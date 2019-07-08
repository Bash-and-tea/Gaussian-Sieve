import sys
from math import floor, sqrt

class Gint(object):
    def __init__(self, r, i):
        self.real = r
        self.im = i

    def get_real(self):
        return self.real

    def get_im(self):
        return self.im

    def toString(self):
        return (str(self.real) + " + " + str(self.im) + "i", str(self.real) + " - " + str(self.im) + "i")

def integer_sieve(n):
    max_size = n+1
    isprime = [True] * max_size 
    prime = [] 
    SPF = [None] * (max_size)
    
    isprime[0] = isprime[1] = False

    for i in range(2, n): 
        if isprime[i] == True: 
            prime.append(i)  
            SPF[i] = i 
        
        j = 0
        while (j < len(prime) and
            i * prime[j] < n and
                prime[j] <= SPF[i]): 
        
            isprime[i * prime[j]] = False
            SPF[i * prime[j]] = prime[j] 
            
            j += 1
	
    # print(prime)
    return prime

def sqsum(p):
    (a,b) = (0, 0)
    for i in range(1, floor(sqrt(p))):
        diff = p - (i*i)
        if (sqrt(diff) == floor(sqrt(diff))):
            (a, b) = (floor(sqrt(diff)), i)
            return (a, b)

def main(n):
    print("Returning primes up to integer: " + str(n))
    primes = integer_sieve(n)
    
    for i in range(len(primes)):
        if (primes[i] % 4 == 1):
            the_squares = sqsum(primes[i])
            # print(the_squares)
            primes[i] = Gint(the_squares[0], the_squares[1]).toString()
    primes[0] = Gint(1,1).toString()

    print(primes)

def test_gauss():
    test = Gint(2, 3)
    print(test.get_real())
    print(test.get_im())
    print(test.toString())

if __name__ == "__main__":
    action = sys.argv[1]

    if (action == "compute"):
        main(int(sys.argv[2]))
    elif (action == "test"):
        test_gauss()
    else:
        sys.exit(0)
