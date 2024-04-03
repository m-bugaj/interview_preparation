// TASK:
// "In computing, End Of File (commonly abbreviated EOF) is a condition in a computer operating system where no more data can be read from a data source." — (Wikipedia: End-of-file)

// The challenge here is to read n lines of input until you reach EOF, then number and print all  lines of content.

// Hint: Java's Scanner.hasNext() method is helpful for this problem.

// Input Format

// Read some unknown  lines of input from stdin(System.in) until you reach EOF; each line of input contains a non-empty String.

// Output Format

// For each line, print the line number, followed by a single space, and then the line content received as input.

// Sample Input

// Hello world
// I am a file
// Read me until end-of-file.
// Sample Output

// 1 Hello world
// 2 I am a file
// 3 Read me until end-of-file.

// SOLUTION:

package Java.HackerRank.Introduction;

import java.util.Scanner;

public class hr_Java_End_of_file {
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        int i = 0;
        Scanner sc = new Scanner(System.in);

        while(sc.hasNext()) {
            i++;
            System.out.printf("%d %s\n", i, sc.nextLine());       
        }
        sc.close();
    }
}
