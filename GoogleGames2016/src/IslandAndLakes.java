import java.io.*;
import java.util.*;

public class IslandAndLakes {
	
	public static int LAND = 1;
	public static int WATER = 0;
	
	public static void main(String[] args) throws FileNotFoundException{
		Scanner s = new Scanner(new File("islands.txt"));
		
		int rows = s.nextInt();
		int cols = s.nextInt();
		s.nextLine();
		
		int[][] input = new int[rows][cols];
		for(int r = 0; r < rows; r++){
			String line = (s.nextLine());
			for(int c = 0; c < cols; c++){
				input[r][c] = Integer.parseInt("" + line.charAt(c));
			}
		}
		//print archi
		for(int r = 0; r < rows; r++){
			for(int c = 0; c < cols; c++){
				System.out.print(input[r][c]);
			}
			System.out.println();
		}
		
		int shore = 0;
		//get total shoreline! = same as lake + beach
		for(int r = 0; r < rows; r++){
			for(int c = 0; c < cols; c++){
				if(input[r][c] == LAND){
					if(input[Math.min(r + 1, rows - 1)][c] == WATER) shore++;
					if(input[Math.max(r - 1, 0)][c] == WATER ) shore++;
					if(input[r][Math.min(c + 1, cols - 1)] == WATER) shore++;
					if(input[r][Math.max(c - 1, 0)] == WATER)shore++;
				}
			}
		}
		//get islands
		System.out.println("Islands = " + islandCount(input));
		System.out.println("Islands = " + (lakeCount(input) - 1));
		System.out.println(shore);
		
	}
	
	public static int islandCount(int[][] input){
		//false
		boolean[][] visited = new boolean[input.length][input[0].length];
		int count = 0;
		
		for(int r = 0; r < visited.length; r++){
			for(int c = 0; c < visited[0].length; c++){
				//fhaven't visited
				if(!visited[r][c] && input[r][c] == LAND){
					count++;
					floodFill(input, visited, r, c, LAND);
				}
				
				visited[r][c] = true;
			}
		}
		
		
		return count;
	}
	
	public static int lakeCount(int[][] input){
		//false
		boolean[][] visited = new boolean[input.length][input[0].length];
		int count = 0;
		
		for(int r = 0; r < visited.length; r++){
			for(int c = 0; c < visited[0].length; c++){
				//fhaven't visited
				if(!visited[r][c] && input[r][c] == WATER){
					count++;
					floodFill(input, visited, r, c, WATER);
				}
				
				visited[r][c] = true;
			}
		}
		
		
		return count;
	}
	
	public static void floodFill(int[][] input, boolean[][] visited, int r, int c, int search){
		if(r >= input.length || r < 0 || c >= input[0].length || c < 0 || visited[r][c]){
			return;
		}
		
		visited[r][c] = true;
		if(input[r][c] == search){
			floodFill(input, visited, r + 1, c, search);
			floodFill(input, visited, r - 1, c, search);
			floodFill(input, visited, r, c + 1, search);
			floodFill(input, visited, r, c - 1, search);
		}
	}
}
