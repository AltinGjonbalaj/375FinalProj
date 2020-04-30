#include <stdio.h>
#include <stdlib.h>
#include <ctime>
#include <iostream>
#include <fstream>

using namespace std;

int main() {
	ofstream output("sparse_input.txt");
	srand((unsigned)time(0));
	for (int i = 0; i < 500000; i++) {
		const int num_nodes = (rand() % ((50 - 3) + 1)) + 3; //pick a number of nodes between 3 and 100
		int adj_matrix[num_nodes][num_nodes];
		for (int row = 0; row < num_nodes; row++) {
			for (int col = 0; col <= row; col++) {
				int rand_weight = (rand() % 1002) + (-1);
				if (rand_weight < 800 || row == col) {
					rand_weight = -1; //make all numbers on the diagonal -1 and remove 0 as a possibility
				}
				adj_matrix[row][col] = rand_weight;
				adj_matrix[col][row] = rand_weight;
			}
		}
		

		//write out matrices to file
		for (int r = 0; r < num_nodes; r++) {
			for (int c = 0; c < num_nodes; c++) {
				output << adj_matrix[r][c];
				if (c != num_nodes - 1) {
					output << ",";
				}
				
			}
			if (r != num_nodes - 1) {
				output << "|";
			}
		}
		output << endl;
	}
	output.close();
	return 0;
}
