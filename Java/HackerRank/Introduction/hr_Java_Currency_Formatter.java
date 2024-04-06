// TASK:

// Given a double-precision number, payment, denoting an amount of money, use the NumberFormat class' getCurrencyInstance method to convert payment into the US, Indian, Chinese, and French currency formats. Then print the formatted values as follows:

// US: formattedPayment
// India: formattedPayment
// China: formattedPayment
// France: formattedPayment
// where formattedPayment is payment formatted according to the appropriate Locale's currency.

// Note: India does not have a built-in Locale, so you must construct one where the language is en (i.e., English).

// Sample Input

// 12324.134
// Sample Output

// US: $12,324.13
// India: Rs.12,324.13
// China: ￥12,324.13
// France: 12 324,13 €

// SOLUTION:

package Java.HackerRank.Introduction;

import java.text.NumberFormat;
import java.util.Locale;
import java.util.Scanner;

public class hr_Java_Currency_Formatter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double payment = scanner.nextDouble();
        scanner.close();
        
        // Write your code here.
        String us = NumberFormat.getCurrencyInstance(Locale.US).format(payment);
        Locale indiaLocale = new Locale.Builder().setLanguage("en").setRegion("IN").build();
        String india = NumberFormat.getCurrencyInstance(indiaLocale).format(payment);
        String china = NumberFormat.getCurrencyInstance(Locale.CHINA).format(payment);
        String france = NumberFormat.getCurrencyInstance(Locale.FRANCE).format(payment);
        
        System.out.println("US: " + us);
        System.out.println("India: " + india);
        System.out.println("China: " + china);
        System.out.println("France: " + france);
    }
}
