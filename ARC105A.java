import java.util.*;
public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int[] l = new int[4];
    for (int i = 0; i<4; i++) {
      l[i] = sc.nextInt();
    }
    Arrays.sort(l);
    if (((l[0]+l[3])==(l[1]+l[2])) || ((l[0]+l[1]+l[2])==l[3])) {
      System.out.println("Yes");
    }else{
      System.out.println("No");
    }
    }
  }