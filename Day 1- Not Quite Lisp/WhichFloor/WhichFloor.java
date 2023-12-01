import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class WhichFloor {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner scnr = new Scanner(new File("floorInstruction"));
        String instrcution = scnr.nextLine();
        int num = 0;
        int op = 1;
        for (int i = 0; i < instrcution.length(); ++i) {
            if (instrcution.charAt(i) == '(') {
                num += 1;
            }
            if (instrcution.charAt(i) == ')') {
                num -= 1;
            }
            if (num == -1) {
                op += i;
                break;
            }
        }
        System.out.println("num: " + num + ", op: " + op);
    }
}
