/*Prob 1:
Write a program which takes two values x and y. Prints x for y number of times.
Input:
2 
3
Expected Output
2
2
2*/
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int i = scan.nextInt();
        int j = scan.nextInt();
        for (int k =1;k<=j;k++){
            System.out.println(i);
        }
    
    }
}

//Prob 2:
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int x = scan.nextInt();
        for (int i = 1; x * i <= 1000; i++) {
            System.out.println(x * i);
        }
    
    }
}

//Prob 3:
//Write a program to get firstName and lastName and n as input and print fullName that is firstName+lastName for n times.

import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String a  = scan.nextLine();
        String b  = scan.nextLine();
        int count = scan.nextInt();
        for (int i = 1;  i <= count; i++) {
            System.out.println(a+" "+b);
        }
    
    }
  /*O/p:
Anisha
Rag
5
Anisha Rag
Anisha Rag
Anisha Rag
Anisha Rag
Anisha Rag*/
