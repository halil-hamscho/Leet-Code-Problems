package arrays_and_hashing.count_primes;

public class Solution {
    public boolean isPrime (int num) {
        // here we will check if a number is prime
        int counter = 0;
        for (int i = 1; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                counter++;
                if ((num / i) != i) {
                    counter++;
                }
            }
        }
        if (counter == 2) {
            return true;
        }
        else {
            return false;
        }
    }
    public int countPrimes(int n) {
        // Sieve of Erathosthenes
        // Will need to do some optimized precomputation, where we utilize an array
        // Mark 1 if it is prime, then mark 0 for its multiples

        if (n <= 2) {
            // 0 and 1 are not primes
            return 0;
        }

        boolean []isprime = new boolean[n];
        // Populate the array
        for(int i = 0; i < n; i++) {
            isprime[i] = true;
        }
        // Precomputation
        for (int i = 2; i < Math.sqrt(n); i++) {
            if (isprime[i]) {
                // Mark multiples are not true
                // Example i = 2, j = 2 x 2 = 4, j += 2 (6)
                for (int j = i*i; j < n; j+=i) {
                    isprime[j] = false;
                }
            }
        }
        int count = 0;
        for(int i = 2; i < n; i++) {
            if(isprime[i]) {
                count++;
            }
        }
        return count;
    }
    public static void main(String[] args) {
        Solution sol = new Solution();
        int num = 10;
        System.out.println(sol.countPrimes(10));
    }
}
