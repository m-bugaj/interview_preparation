// TASK:
// Task
// Given an integer, n, perform the following conditional actions:

// If n is odd, print Weird
// If n is even and in the inclusive range of 2 to 5, print Not Weird
// If n is even and in the inclusive range of 6 to 20, print Weird
// If n is even and greater than 20, print Not Weird
// Complete the stub code provided in your editor to print whether or not  is weird.

// Sample Input 0

// 3
// Sample Output 0

// Weird
// Sample Input 1

// 24
// Sample Output 1

// Not Weird

// SOLUTION:

package Java.HackerRank.Introduction;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class hr_Java_If_Else {
    
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int N = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        scanner.close();
        
        if(N%2 != 0){
            System.out.println("Weird");
        } else {
            if (N>=2 && N<=5) {
                System.out.println("Not Weird");
            }
            if (N>=6 && N<=20) {
                System.out.println("Weird");
            }
            
            if (N>20) {
                System.out.println("Not Weird");
            }
        }
    }
}