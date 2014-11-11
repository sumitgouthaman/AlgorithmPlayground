/**
Longest Common Subsequence
==========================

*/

import java.util.*;

public class LCS {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int testCase = 0; testCase < T; testCase++) {
            String s1 = sc.next();
            String s2 = sc.next();
            
            String lcs = getLCS(s1, s2);
            
            System.out.println(lcs);
        }
    }
    
    public static String getLCS(String s1, String s2) {
        int N = s1.length();
        int M = s2.length();
        
        int[][] lcsTable = new int[N + 1][M + 1];
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= M; j++) {
                if(charAt(s1, i) == charAt(s2, j)) {
                    lcsTable[i][j] = 1 + lcsTable[i - 1][j - 1];
                } else {
                    lcsTable[i][j] = Math.max(
                        lcsTable[i][j - 1],
                        lcsTable[i - 1][j]
                    );
                }
            }
        }
        int ptr1 = N;
        int ptr2 = M;
        int ptrLcs = lcsTable[N][M] - 1;
        char[] lcs = new char[lcsTable[N][M]];
        while (ptr1 > 0 && ptr2 > 0) {
            if (charAt(s1, ptr1) == charAt(s2, ptr2)) {
                lcs[ptrLcs--] = charAt(s1, ptr1);
                ptr1--;
                ptr2--;
            } else {
                if (lcsTable[ptr1][ptr2 - 1] > lcsTable[ptr1 - 1][ptr2]) {
                    ptr2--;
                } else {
                    ptr1--;
                }
            }
        }
        return new String(lcs);
    }
    
    // Where index is assumed to start from 1 instead of 0
    public static char charAt(String s, int index) {
        return s.charAt(index - 1);
    }
}