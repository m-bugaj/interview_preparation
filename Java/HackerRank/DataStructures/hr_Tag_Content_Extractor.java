// TASK:

// In a tag-based language like XML or HTML, contents are enclosed between a start tag and an end tag like <tag>contents</tag>. Note that the corresponding end tag starts with a /.

// Given a string of text in a tag-based language, parse this text and retrieve the contents enclosed within sequences of well-organized tags meeting the following criterion:

// 1. The name of the start and end tags must be same. The HTML code <h1>Hello World</h2> is not valid, because the text starts with an h1 tag and ends with a non-matching h2 tag.

// 2. Tags can be nested, but content between nested tags is considered not valid. For example, in <h1><a>contents</a>invalid</h1>, contents is valid but invalid is not valid.

// 3. Tags can consist of any printable characters.

// Sample Input

// 4
// <h1>Nayeem loves counseling</h1>
// <h1><h1>Sanjay has no watch</h1></h1><par>So wait for a while</par>
// <Amee>safat codes like a ninja</amee>
// <SA premium>Imtiaz has a secret crush</SA premium>
// Sample Output

// Nayeem loves counseling
// Sanjay has no watch
// So wait for a while
// None
// Imtiaz has a secret crush

// SOLUTION:

package Java.HackerRank.DataStructures;

import java.util.regex.*;
import java.util.*;

public class hr_Tag_Content_Extractor {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int testCases = Integer.parseInt(in.nextLine());
        while(testCases>0){
            String line = in.nextLine();
            
            //Write your code here
            String regex = "<(.+)>([^<]+)<\\/\\1>";
            Pattern p = Pattern.compile(regex);
            Matcher m = p.matcher(line);
            if (!m.find()) {
                System.out.println("None");
            } else {
                m.reset(); 
                while (m.find()) {
                    System.out.println(m.group(2));
                }
            }
            
            testCases--;
        }
        in.close();
    }
}
