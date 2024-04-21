// TASK:

// Java's BitSet class implements a vector of bit values (i.e.:  false(0) or  true(1)) that grows as needed, allowing us to easily manipulate bits while optimizing space (when compared to other collections). Any element having a bit value of 1 is called a set bit.

// Given 2 BitSets, B1 and B2, of size N where all bits in both BitSets are initialized to 0, perform a series of M operations. After each operation, print the number of set bits in the respective BitSets as two space-separated integers on a new line.

// Sample Input

// 5 4
// AND 1 2
// SET 1 4
// FLIP 2 2
// OR 2 1
// Sample Output

// 0 0
// 1 0
// 1 1
// 1 2

// SOLUTION:

package Java.HackerRank.DataStructures;

import java.util.*;

public class hr_Java_BitSet {
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        int bsSize = in.nextInt();
        BitSet b1 = new BitSet(bsSize);
        BitSet b2 = new BitSet(bsSize);
        
        int m = in.nextInt();
        in.nextLine();
        
        for (int i=0;i<m;i++) {
            String operation = in.next();
            int p1 = in.nextInt();
            int p2 = in.nextInt();
            
            if (operation.equals("AND")) {
                if (p1 == 1) b1.and(b2);
                if (p1 == 2) b2.and(b1);
                System.out.println(b1.cardinality() + " " + b2.cardinality());
            }
            
            if (operation.equals("OR")) {
                if (p1 == 1) b1.or(b2);
                if (p1 == 2) b2.or(b1);
                System.out.println(b1.cardinality() + " " + b2.cardinality());
            }
            
            if (operation.equals("FLIP")) {
                if (p1 == 1) b1.flip(p2);
                if (p1 == 2) b2.flip(p2);
                System.out.println(b1.cardinality() + " " + b2.cardinality());
            }
            
            if (operation.equals("SET")) {
                if (p1 == 1) b1.set(p2);
                if (p1 == 2) b2.set(p2);
                System.out.println(b1.cardinality() + " " + b2.cardinality());
            }
            
            if (operation.equals("XOR")) {
                if (p1 == 1) b1.xor(b2);
                if (p1 == 2) b2.xor(b1);
                System.out.println(b1.cardinality() + " " + b2.cardinality());
            }
        }
        in.close();
    }
}
