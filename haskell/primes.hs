sieve' primes (n:numbers) | any (\x -> n `mod` x == 0) primes = sieve' primes numbers
                          | otherwise = n:(sieve' (n:primes) numbers)

sieve = sieve' [] (2:[3,5..])