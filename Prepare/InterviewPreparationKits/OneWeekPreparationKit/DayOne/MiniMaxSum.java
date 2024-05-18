// TASK:
// Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

// Example
// arr=[1,3,5,7,9]

// The minimum sum is 1+3+5+7=16 and the maximum sum is 3+5+7+9=24. The function prints

// 16 24

// Sample Input

// 1 2 3 4 5
// Sample Output

// 10 14

// SOLUTION:


package Prepare.InterviewPreparationKits.OneWeekPreparationKit.DayOne;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class IntegerComparator implements Comparator<Integer> {
    @Override
    public int compare(Integer a, Integer b) {
        return a - b;
    }
}

class Result {

    /*
     * Complete the 'miniMaxSum' function below.
     *
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static void miniMaxSum(List<Integer> arr) {
    // Write your code here
        
        //SOLUTION FOR HUGE LIST WITH SORTING USING COMPARATOR
        Collections.sort(arr, new IntegerComparator());
        
        int len = arr.size();
        long min = (long) arr.get(0) + (long) arr.get(1) + (long) arr.get(2) + (long) arr.get(3);
        long max = (long) arr.get(len-1) + 
                    (long) arr.get(len-2) + 
                    (long) arr.get(len-3) + 
                    (long) arr.get(len-4);
        
        //SOLUTION FOR SMALL LIST
        // long sum = 0;
        
        // for (int i=0; i<arr.size(); i++) {
        //     sum += arr.get(i);
        // }
        
        // long min = sum - Collections.max(arr);
        // long max = sum - Collections.min(arr);
        
        System.out.println(min + " " + max);
    }

}

public class MiniMaxSum {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        String[] arrTemp = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        List<Integer> arr = new ArrayList<>();

        for (int i = 0; i < 5; i++) {
            int arrItem = Integer.parseInt(arrTemp[i]);
            arr.add(arrItem);
        }

        Result.miniMaxSum(arr);

        bufferedReader.close();
    }
}
