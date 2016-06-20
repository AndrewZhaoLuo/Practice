/*
ID: andrew.42
LANG: C
TASK: agrinet
*/

#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#define MAX_FARMS 150
#define MIN_FARMS 3
#define MAX_DISTANCE 100000

void main () {	
	int costMatrix[MAX_FARMS][MAX_FARMS];
	int numFarms;

	FILE *fin  = fopen ("agrinet.in", "r");
	FILE *fout = fopen ("agrinet.out", "w");

	//read information from the file first
	fscanf(fin, "%d", &numFarms);
	for(int a = 0; a < numFarms; a++){
		for(int b = 0; b < numFarms; b++){
			fscanf(fin, "%d", &costMatrix[a][b]);
			//printf("%d\t", costMatrix[a][b]);
		}
		//printf("\n");
	}

	//should store in order of adding, the id (indice) of each added node
	int inTreeID[MAX_FARMS]; 
	for(int i = 0; i < MAX_FARMS; i++){
		inTreeID[i] = -1;
	}

	//this on the other hand uses significant indexing, where 1 = in tree
	int inTree[MAX_FARMS];

	inTreeID[0] = 0;
	inTree[0] = 1;

	int tot = 0;
	for(int i = 1; i < numFarms; i++){
		//go through all nodes in tree, find shortest path of tree to node
		//not yet in tree
		int shortestPath = MAX_DISTANCE + 1;
		int shortestNodeToAdd = -1;
		for(int n = 0; n < i; n++){
			int curN = inTreeID[n];

			for(int c = 0; c < numFarms; c++){
				if(inTree[c] == 0 && costMatrix[curN][c] < shortestPath && costMatrix[curN][c] != 0){
					shortestPath = costMatrix[curN][c];
					shortestNodeToAdd = c;
				}
			}
		}

		tot += shortestPath;
		inTreeID[i] = shortestNodeToAdd;
		inTree[shortestNodeToAdd] = 1;

		//printf("%d\n", shortestPath);	
		//for(int a = 0; a <= i; a++){
		//	printf("\t%d", inTreeID[a]);
		//}	
		//printf("\n");
	}

	fprintf(fout, "%d\n", tot);

	exit (0);
}
