// Task:

// There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.

// Example
// stringList = ['ab','ab','abc']
// queries = ['ab','abc','bc']


// There are 2 instances of 'ab', 1 of 'abc' and 0 of 'bc'. For each query, add an element to the return array, results = [2,1,0].

// Function Description

// Complete the function matchingStrings in the editor below. The function must return an array of integers representing the frequency of occurrence of each query string in stringList.

// matchingStrings has the following parameters:

// string stringList[n] - an array of strings to search
// string queries[q] - an array of query strings
// Returns

// int[q]: an array of results for each query

// Sample input 1

// stringList = ['aba','baba','aba','xzxb']
// queries = ['aba','xzxb','ab']

// Sample output 1
// 2
// 1
// 0

// SOLUTION:

package Prepare.DataStructures.HackerRank.Arrays;

import java.io.*;
import java.util.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'matchingStrings' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts following parameters:
     *  1. STRING_ARRAY stringList
     *  2. STRING_ARRAY queries
     */

    public static List<Integer> matchingStrings(List<String> stringList, List<String> queries) {
    // Write your code here

    List<Integer> out = new ArrayList<>();
    HashMap<String, Integer> s_dict = new HashMap<>();
    for(int i=0;i<stringList.size();i++)
        s_dict.put(stringList.get(i), s_dict.getOrDefault(stringList.get(i), 0) + 1);
        
    for(int j=0;j<queries.size();j++) {
        int count = s_dict.getOrDefault(queries.get(j), 0);
        out.add(count);
    }
    
    return out;
    }

}

public class hr_Sparse_Arrays {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter("C:/Users/BUGI/Desktop/Learn/Interview/Prepare/DataStructures/HackerRank/Arrays/output/hr_sparse_arrays.txt"));

        int stringListCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<String> stringList = IntStream.range(0, stringListCount).mapToObj(i -> {
            try {
                return bufferedReader.readLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
            .collect(toList());

        int queriesCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<String> queries = IntStream.range(0, queriesCount).mapToObj(i -> {
            try {
                return bufferedReader.readLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
            .collect(toList());

        List<Integer> res = Result.matchingStrings(stringList, queries);

        bufferedWriter.write(
            res.stream()
                .map(Object::toString)
                .collect(joining("\n"))
            + "\n"
        );

        bufferedReader.close();
        bufferedWriter.close();
    }
}

