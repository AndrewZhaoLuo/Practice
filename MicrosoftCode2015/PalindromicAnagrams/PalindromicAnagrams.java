import java.util.*;
import java.io.*;

public class PalindromicAnagrams{


   public static void main(String[] args) throws FileNotFoundException{
      
      
      //read input
      ArrayList<String> array = new ArrayList<String>();
      Scanner s = new Scanner(new File("input.txt"));
      while(s.hasNext()){
         array.add(s.next());
      }

      //output
      PrintStream p = new PrintStream(new File("output.txt"));
      
      for(int i = 0; i < array.size(); i++){
         int[] count = getCharCount(array.get(i));
         p.print(howManyToRemove(count) + ",");
         p.println(permutations(count));
      }

      p.close();
      
   }
   
   public static int factorial(int n){
      int prod = 1;
      while(n >= 1){
         prod *= n;
         n--;
      }
      
      return prod;
   }
   
   public static int permutations(int[] count){
      int[] pairs = new int[count.length];
      
      for(int i = 0; i < count.length; i++){
         while(count[i] >= 2){
            pairs[i] += 1;
            count[i] -= 2;
         }
      }
      
      int totalPairs = 0;
      for(int i = 0; i < pairs.length; i++){
         totalPairs += pairs[i];
      }
      
      int totalPermutations = factorial(totalPairs);
      
      for(int i = 0; i < pairs.length; i++){
         totalPermutations /= factorial(pairs[i]);
      }
      
      return totalPermutations;
      
   }
   
   public static int[] getCharCount(String s){
      int[] count = new int[26];//for each of the 26 letters
      for(int i = 0; i < s.length(); i++){
         count[s.charAt(i) - 'a']++;
      }
      
      return count;
   }
   
   public static int getOddCount(int[] array){
      int oddCount = 0;
      //get an odd count
      for(int i = 0; i < array.length; i++){
         if(array[i] % 2 == 1){
            oddCount++;
         }
      }
      
      return oddCount;
   }
   
   //gets count, and removes count
   public static int howManyToRemove(int[] array){
      int totalRemove = 0;
      while(getOddCount(array) > 1){
         //find lowest odd number and remove them
         int lowestOddIndex = 0;
         int lowestOdd = 21;//max size of string is 21
         for(int i = 0; i < array.length; i++){
            if(array[i] % 2 == 1 && array[i] < lowestOdd){
               lowestOdd = array[i];
               lowestOddIndex = i;
            }
         }
         
         totalRemove += 1;
         array[lowestOddIndex]--;
      }
      
      return totalRemove;
   }

}