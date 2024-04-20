// TASK:

// In computer science, a double-ended queue (dequeue, often abbreviated to deque, pronounced deck) is an abstract data type that generalizes a queue, for which elements can be added to or removed from either the front (head) or back (tail).

// Deque interfaces can be implemented using various types of collections such as LinkedList or ArrayDeque classes. For example, deque can be declared as:

// Deque deque = new LinkedList<>();
// or
// Deque deque = new ArrayDeque<>();
// You can find more details about Deque here.

// In this problem, you are given N integers. You need to find the maximum number of unique integers among all the possible contiguous subarrays of size M.

// Note: Time limit is  second for this problem.

// Sample Input

// 6 3
// 5 3 5 2 3 2
// Sample Output

// 3

// SOLUTION:

package Java.HackerRank.DataStructures;

import java.util.*;

public class hr_Java_Dequeue {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Deque<Integer> deque = new ArrayDeque<>();
        Set<Integer> uniqueElements = new HashSet<>();
        int n = in.nextInt();
        int m = in.nextInt();
         int maxUnique = 0;

        for (int i = 0; i < n; i++) {
        int num = in.nextInt();
        deque.addLast(num);
        uniqueElements.add(num);

        if (deque.size() == m + 1) {
            int removed = deque.removeFirst();
            if (!deque.contains(removed)) {
                uniqueElements.remove(removed);
            }
        }

        maxUnique = Math.max(maxUnique, uniqueElements.size());
        }

        System.out.println(maxUnique);

        in.close();
    }
}
