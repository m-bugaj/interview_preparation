// TASK:

// Comparators are used to compare two objects. In this challenge, you'll create a comparator and use it to sort an array.

// The Player class is provided for you in your editor. It has 2 fields: a name String and a score integer.

// Given an array of n Player objects, write a comparator that sorts them in order of decreasing score; if  or more players have the same score, sort those players alphabetically by name. To do this, you must create a Checker class that implements the Comparator interface, then write an int compare(Player a, Player b) method implementing the Comparator.compare(T o1, T o2) method.

// Sample Input

// 5
// amy 100
// david 100
// heraldo 50
// aakansha 75
// aleksa 150
// Sample Output

// aleksa 150
// amy 100
// david 100
// aakansha 75
// heraldo 50

// SOLUTION:

package Java.HackerRank.DataStructures;

import java.util.*;

// Write your Checker class here
class Checker implements Comparator<Player> {
    public int compare(Player p1, Player p2) {
        if (p2.score == p1.score) return p1.name.compareTo(p2.name);
        return p2.score - p1.score;
    }
}

class Player{
    String name;
    int score;
    
    Player(String name, int score){
        this.name = name;
        this.score = score;
    }
}

public class hr_Java_Comparator {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();

        Player[] player = new Player[n];
        Checker checker = new Checker();
        
        for(int i = 0; i < n; i++){
            player[i] = new Player(scan.next(), scan.nextInt());
        }
        scan.close();
     
        Arrays.sort(player, checker);
        for(int i = 0; i < player.length; i++){
            System.out.printf("%s %s\n", player[i].name, player[i].score);
        }
    }
}
