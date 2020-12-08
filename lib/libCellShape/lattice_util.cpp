#include <iostream>
#include <map>

int ** make_lattice(int size_x, int size_y){
	int *  content = new int  [size_x * size_y]{0};
	int ** lattice = new int* [size_x];
	for (int index = 0; index < size_x; index ++){
		lattice[index] = content + index * size_y;
	}
	return lattice;
}

void denoise_lattice(int ** lattice_in, int ** lattice_out, int size_x, int size_y){
	for (int y = 0; y < size_y; y++){
		for (int x = 0; x < size_x; x++){
			int most = 0;
			std::map<int, int> count;
			for (int y_eye = y-1; y_eye <= y+1; y_eye++){
				for (int x_eye = x-1; x_eye <= x+1; x_eye++){
					int val = -1;
					if (x_eye < size_x && x_eye > 0 && y_eye < size_y && x_eye > 0)
						val = lattice_in[x_eye][y_eye];
					if (count.find(val) == count.end()) count[val] = 0;
					else count[val] += 1;
					if (count[val] >= count[most]){most = val;}
				}
			}
			if(most != -1 && most != lattice_in[x][y] && count[most] > 5){
				lattice_out[x][y] = most;
			}
			else{
				lattice_out[x][y] = lattice_in[x][y];
			}
		}
	}
}

