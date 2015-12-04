import java.util.*;
import java.io.*;

public class HappyNumbers{

   //the index represents the number
   //the number represents the answer
   //a negative indicates an unhappy number
   static boolean[] visited = new boolean[500001];
   
   public static void main(String[] args) throws FileNotFoundException{
      //problem: happy numbers!
      int[] question = new int[10];
   
      //read input
      ArrayList<Integer> array = new ArrayList<Integer>();
      Scanner s = new Scanner(new File("input.txt"));
      for(int i = 0; i < question.length; i++){
         question[i] = s.nextInt();
      }

      //output
      PrintStream p = new PrintStream(new File("output.txt"));
      //calculate all happy numbers and their cycles
      for(int i = 0; i < question.length; i++){
         int result = cycle(question[i]);
         visited = new boolean[500001];
         
         if(result < 0){
            p.print("unhappy ");
            result *= -1;
         }
         else{
            p.print("happy ");
         }
         
         p.println((result - 1));
      }
      p.close();
      
   }

   public static int squareDigits(int n){
      int sum = 0;
      while (n > 0){
         sum += (n % 10) * (n % 10);
         n /=10;
      }
      
      return sum;
   }

   //cycle numbers
   public static int cycle(int n){
      if(n == 1){
         return 1;
      }
      if(visited[n]){
         return -1;
      }
      
      visited[n] = true;
      int result = cycle(squareDigits(n));
      
      if(result > 0){
         result += 1;
      }
      else{
         result -= 1;
      }
      
      return result;
   }

}