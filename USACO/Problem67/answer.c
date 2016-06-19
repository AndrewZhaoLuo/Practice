/*
ID: andrew.42
LANG: C
TASK: cowtour
*/

#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int pathThere(char c);
double max(double a, double b);

double max(double a, double b){
	if(a > b){
		return a;
	}
	return b;
}

int pathThere(char c){
	return c == '1';
}

void main () {
	double CANT_REACH = -1;
	int MAX_PASTURES = 150;

	//uses significant indexing, ie the 0th pasture's info will be in the 0th index of these arrays
	int numPastures;
	int pasturesX [MAX_PASTURES];
	int pasturesY [MAX_PASTURES];

	char adjacencyMatrix [MAX_PASTURES][MAX_PASTURES];

	FILE *fin  = fopen ("cowtour.in", "r");
	FILE *fout = fopen ("cowtour.out", "w");

	//read information from the file first
	fscanf(fin, "%d", &numPastures);
	for(int i = 0; i < numPastures; i++){
		fscanf(fin, "%d %d", &(pasturesX[i]), &(pasturesY[i]));
	}
	for(int a = 0; a < numPastures; a++){
		char line[numPastures];
		fscanf(fin, "%s", line);
		
		for(int b = 0; b < numPastures; b++){
			adjacencyMatrix[a][b] = line[b];
		}
	}

	//run flloyd marshall - note this will also tell us the two pastures
	//pastures with non-valid reach
	double weightMatrix [MAX_PASTURES][MAX_PASTURES];
	for(int a = 0; a < numPastures; a++){
		for(int b = 0; b < numPastures; b++){
			if(pathThere(adjacencyMatrix[a][b])){
				double dx = pasturesX[a] - pasturesX[b];
				double dy = pasturesY[a] - pasturesY[b];
				double tot = dx * dx + dy * dy;
				weightMatrix[a][b] = sqrt(tot);
			}
			else{
				weightMatrix[a][b] = CANT_REACH;
			}
		}
	}
	for(int k = 0; k < numPastures; k++){
		for(int i = 0; i < numPastures; i++){
			for(int j = 0; j < numPastures; j++){
				double ik = weightMatrix[i][k];
				double kj = weightMatrix[k][j];	

				if(ik != CANT_REACH && kj != CANT_REACH && i != k && k != j && i != j
				&& (ik + kj < weightMatrix[i][j] || weightMatrix[i][j] == CANT_REACH)){
					weightMatrix[i][j] = ik + kj;
				}
			}
		}
	}
	
	//we then want to know the maximum minimum-spanning edge for each vertex
	double diameterTo[MAX_PASTURES];
	for(int a = 0; a < numPastures; a++){
		for(int b = 0; b < numPastures; b++){
			if(weightMatrix[a][b] != CANT_REACH && weightMatrix[a][b] > diameterTo[a]){
				diameterTo[a] = weightMatrix[a][b];
			}
		}
	}

	//we then want to know the diameter of the field each pasture is in
	double pasturesDiameter[MAX_PASTURES];
	for(int a = 0; a < numPastures; a++){
		double top = 0;
		for(int b = 0; b < numPastures; b++){
			if(weightMatrix[a][b] != CANT_REACH){
				double localTop = max(diameterTo[a], diameterTo[b]);
				top = max(top, localTop);
			}
		}
		pasturesDiameter[a] = top;
	}

	//we then try the combinations of every possible edge between two disconnected vertexes
	//and pick the one with the smallest minimum spanning edge
	double smallestDiameter = -1;
	for(int a = 0; a < numPastures; a++){
		for(int b = 0; b < numPastures; b++){
			if(weightMatrix[a][b] == CANT_REACH && a != b){
				double diameterA = diameterTo[a];
				double diameterB = diameterTo[b];

				int dx = pasturesX[a] - pasturesX[b];
				int dy = pasturesY[a] - pasturesY[b];

				double dist = sqrt(dx * dx + dy * dy);
				double newDiameter = dist + diameterA + diameterB;
				//if the new drawn diameter is less than the original diameter
				//the daimeter of the new field be not really change man
				double bestDiameter = max(newDiameter, pasturesDiameter[a]);
				bestDiameter = max(bestDiameter, pasturesDiameter[b]);

				if(bestDiameter < smallestDiameter || smallestDiameter == -1){
					smallestDiameter = bestDiameter;
				}
			}
		}
	}
	
	fprintf(fout, "%f\n", smallestDiameter);

	exit (0);
}
