import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {
    public static int getGameNum(String str) {
        String num = str.substring(str.indexOf(" ") + 1);
        return Integer.parseInt(num);
    }
    public static String[] getLst(String str) {
        String[] strLst = str.split("[:,;]");
        for (int i = 0; i < strLst.length; ++i) {
            strLst[i] = strLst[i].trim();
        }
        return strLst;
    }
    public static void main(String[] args) throws FileNotFoundException {
        Scanner scnr = new Scanner(new File("games"));
        int sum = 0;
        int powerSum = 0;
        while (scnr.hasNextLine()) {
            String ln = scnr.nextLine();
            String[] singleGame = getLst(ln);
            int green = 0;
            int red = 0;
            int blue = 0;
            for (int i = 1; i < singleGame.length; ++i) {
                int max = Integer.parseInt(singleGame[i].substring(0,
                        singleGame[i].indexOf(" ")));
                if (singleGame[i].contains("n") && max > green) {
                    green = max;
                }
                if (singleGame[i].contains("l") && max > blue) {
                    blue = max;
                }
                if (singleGame[i].contains("d") && max > red) {
                    red = max;
                }
            }
            if (green <= 13 && red <= 12 && blue <= 14) {
                sum += getGameNum(singleGame[0]);
            }
            powerSum += green * blue * red;
        }
        System.out.println(sum);
        System.out.println(powerSum);
    }
}
