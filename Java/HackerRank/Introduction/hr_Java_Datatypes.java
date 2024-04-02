// TASK:
// Java has 8 primitive data types; char, boolean, byte, short, int, long, float, and double. For this exercise, we'll work with the primitives used to hold integer values (byte, short, int, and long):

// A byte is an 8-bit signed integer.
// A short is a 16-bit signed integer.
// An int is a 32-bit signed integer.
// A long is a 64-bit signed integer.
// Given an input integer, you must determine which primitive data types are capable of properly storing that input.

// To get you started, a portion of the solution is provided for you in the editor.

// Reference: https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html

// Sample Input

// 5
// -150
// 150000
// 1500000000
// 213333333333333333333333333333333333
// -100000000000000
// Sample Output

// -150 can be fitted in:
// * short
// * int
// * long
// 150000 can be fitted in:
// * int
// * long
// 1500000000 can be fitted in:
// * int
// * long
// 213333333333333333333333333333333333 can't be fitted anywhere.
// -100000000000000 can be fitted in:
// * long

// SOLUTION:

package Java.HackerRank.Introduction;

import java.util.Scanner;

public class hr_Java_Datatypes {
    public static void main(String []argh)
    {



        Scanner sc = new Scanner(System.in);
        int t=sc.nextInt();

        for(int i=0;i<t;i++)
        {

            try
            {
                long x=sc.nextLong();
                System.out.println(x+" can be fitted in:");
                if(x>=-128 && x<=127)System.out.println("* byte");
                //Complete the code
                if(x>=Math.pow(-2, 15) && x<=Math.pow(2, 15)-1)System.out.println("* short");
                if(x>=Math.pow(-2, 31) && x<=Math.pow(2, 31)-1)System.out.println("* int");
                if(x>=Math.pow(-2, 63) && x<=Math.pow(2, 63)-1)System.out.println("* long");
            }
            catch(Exception e)
            {
                System.out.println(sc.next()+" can't be fitted anywhere.");
            }

        }
    }
}
