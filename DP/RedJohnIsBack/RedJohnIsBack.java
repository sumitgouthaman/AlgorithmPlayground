/**
Red John is Back
================
 Red John has committed another murder. But this time, he doesn't leave a red smiley behind. What he leaves behind is a puzzle for Patrick Jane to solve. He also texts Teresa Lisbon that if Patrick is successful, he will turn himself in. The puzzle begins as follows.
 
 There is a wall of size 4xN in the victim's house where. The victim also has an infinite supply of bricks of size 4x1 and 1x4 in her house. There is a hidden safe which can only be opened by a particular configuration of bricks in the wall. In every configuration, the wall has to be completely covered using the bricks. There is a phone number written on a note in the safe which is of utmost importance in the murder case. Gale Bertram wants to know the total number of ways in which the bricks can be arranged on the wall so that a new configuration arises every time. He calls it M. Since Red John is back after a long time, he has also gained a masters degree in Mathematics from a reputed university. So, he wants Patrick to calculate the number of prime numbers (say P) up to M (i.e. <= M). If Patrick calculates P, Teresa should call Red John on the phone number from the safe and he will surrender if Patrick tells him the correct answer. Otherwise, Teresa will get another murder call after a week.
 
 You are required to help Patrick correctly solve the puzzle.
 
 Sample Input
 The first line of input will contain an integer T followed by T lines each containing an integer N.
 
 Sample Output
 Print exactly one line of output for each test case. The output should contain the number P.
 
 Constraints
 1<=T<=20
 1<=N<=40
 
 Sample Input
 
 2
 1
 7
 
 Sample Output
 
 0
 3
 
 Explanation
 
 For N = 1, the brick can be laid in 1 format only
 
 The number of primes <= 1 is 0 and hence the answer.
 
 For N = 7, one of the ways in which we can lay the bricks is
 
 There are 5 ways of arranging the bricks for N = 7 and there are 3 primes <= 5 and hence the answer 3.
*/

import java.util.Scanner;

class Solution{
    private static int solve(int N) {
        int[] possibilities = new int[N];
        possibilities[0] = 1;
        for(int pos = 1; pos < N; pos++){
            possibilities[pos] = possibilities[pos - 1];
            if(pos == 3) {
                possibilities[pos]++;
                continue;
            }
            if(pos > 3) {
                possibilities[pos] += possibilities[pos - 4];
            }
        }
        int ways = possibilities[N - 1];
        if (ways < 2) {
            return 0;
        }
        boolean[] sieve = new boolean[ways + 1];
        sieve[0] = true; // Not primes
        sieve[1] = true;
        for(int num = 2; num <= Math.sqrt(ways); num++) {
            int i = 2;
            while (num * i <= ways) {
                sieve[num * i] = true;
                i++;
            }
        }
        int numPrimes = 0;
        for(boolean isNotPrime: sieve) {
            if (!isNotPrime) {
                numPrimes++;
            }
        }
        return numPrimes;
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for(int testCase = 0; testCase < T; testCase++) {
            int N = sc.nextInt();
            int P = solve(N);
            System.out.println(P);
        }
    }
}