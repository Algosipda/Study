#include <iostream>

using namespace std;

int height, width;
char map[20][20];
int tetris[4][2][2] = {
	{{0, 1}, {1, 0}},
	{{0, 1}, {1, 1}},
	{{1, 0}, {1, 1}},
	{{1, -1}, {1, 0}}
};

bool valid(int y, int x, int k) {
	int nextY, nextX;

	for(int i=0; i<2; i++) {
		nextY = y + tetris[k][i][0];
		nextX = x + tetris[k][i][1];

		if(nextX < 0 || nextX >= width || nextY < 0 || nextY >= height)
			return false;
		if(map[nextY][nextX] != '.')
			return false;
	}
	return true;
}

void printBoard() {
	cout<<endl<<"-------------------------"<<endl;
	for(int i=0; i < height; i++) {
		for(int j=0; j<width; j++) {
			cout<<map[i][j];
		}
		cout<<endl;
	}
}

int cover() {
	int y, x;
	int count = 0, start = 0;
	bool finish = true;

	for(int i=0; i<height && finish == true; i++) {
		for(int j=0; j<width; j++) {
			if(map[i][j] == '.') {
				y = i;
				x = j;
				finish = false;
				break;
			}
		}
	}

	if(finish == true)
		return 1;

	for(int k=0; k<4; k++) {
		if(valid(y, x, k)) {
			map[y][x] = '#';
			map[y+tetris[k][0][0]][x+tetris[k][0][1]] = '#';
			map[y+tetris[k][1][0]][x+tetris[k][1][1]] = '#';
			count += cover();
			map[y][x] = '.';
			map[y+tetris[k][0][0]][x+tetris[k][0][1]] = '.';
			map[y+tetris[k][1][0]][x+tetris[k][1][1]] = '.';
		}
	}

	return count;
}

int main(void) {
	int count = 0;

	cin>>count;
	for(int ct = 0; ct < count; ct++) {
		cin>>height>>width;

		for(int i=0; i<height; i++) {
			for(int j=0; j<width; j++) {
				cin>>map[i][j];
			}
		}
		cout<<cover()<<endl;
	}

	return 0;
}