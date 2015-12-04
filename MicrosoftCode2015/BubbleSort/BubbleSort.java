import java.util.*;
import java.io.*;

public class BubbleSort{
   public static void main(String[] args) throws FileNotFoundException{
      //problem: implement bubble sort and tell the number of swaps we got
   
      //read input
      ArrayList<Integer> array = new ArrayList<Integer>();
      Scanner s = new Scanner(new File("input.txt"));
      while(s.hasNext()){
         array.add(s.nextInt());
      }
      
      int swaps = 0;
      boolean cont = true;
      while(cont){
         cont = false; //set to true when we do a swap
         for(int i = 0; i < array.size() - 1; i++){
            if(array.get(i) > array.get(i + 1)){
               int temp = array.get(i);
               array.set(i, array.get(i + 1));
               array.set(i + 1, temp);
               swaps++;
               cont = true;//stop early if no swaps
            }
         }
      }
      
      PrintStream p = new PrintStream(new File("output.txt"));
      p.println(swaps);
      for(int i = 0; i < array.size(); i++){
         p.print(array.get(i) + " ");
      }
      p.close();
      
   }

}