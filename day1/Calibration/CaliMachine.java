import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class CaliMachine {
    public static String firstNum(String str) {
        int i = 0;
        String num = "";
        while (!Character.isDigit(str.charAt(i))){
            if (str.startsWith("one", i) || str.startsWith(reverseStr("one"), i)) {
                num = "1";
                break;
            }
            if (str.startsWith("two", i) || str.startsWith(reverseStr("two"), i)) {
                num = "2";
                break;
            }
            if (str.startsWith("three", i) || str.startsWith(reverseStr("three"), i)) {
                num = "3";
                break;
            }
            if (str.startsWith("four", i) || str.startsWith(reverseStr("four"), i)) {
                num = "4";
                break;
            }
            if (str.startsWith("five", i) || str.startsWith(reverseStr("five"), i)) {
                num = "5";
                break;
            }
            if (str.startsWith("six", i) || str.startsWith(reverseStr("six"), i)) {
                num = "6";
                break;
            }
            if (str.startsWith("seven", i) || str.startsWith(reverseStr("seven"), i)) {
                num = "7";
                break;
            }
            if (str.startsWith("eight", i) || str.startsWith(reverseStr("eight"), i)) {
                num = "8";
                break;
            }
            if (str.startsWith("nine", i) || str.startsWith(reverseStr("nine"), i)) {
                num = "9";
                break;
            }
            ++i;
        }
        if (num.isEmpty()) {
            for (int j = 0; j < str.length(); ++j) {
                if (Character.isDigit(str.charAt(j))) {
                    num = Character.toString(str.charAt(j));
                    break;
                }
            }
        }
        return num;
    }
    public static String reverseStr(String str) {
        String newStr = "";
        for (int i = 0; i < str.length(); ++i) {
            newStr = Character.toString(str.charAt(i)) + newStr;
        }
        return newStr;
    }
    public static void main(String[] args) throws FileNotFoundException {
        long num = 0;
        Scanner scnr = new Scanner(new File("string"));
        while (scnr.hasNext()) {
            String ln = scnr.nextLine();
            String value = (firstNum(ln).isEmpty()) ? "0" :
                    firstNum(ln) + firstNum(reverseStr(ln));
            num += Integer.parseInt(value);
        }
        System.out.println(firstNum("4nineeightseven2"));
        System.out.println(firstNum(reverseStr("4nineeightseven2")));
        System.out.println(num);
    }
}
