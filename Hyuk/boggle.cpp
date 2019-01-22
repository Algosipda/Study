#include <iostream>

using namespace std;

const int dx[8] = {-1, -1, -1, 1, 1, 1, 0, 0};
const int dy[8] = {-1, 0, 1, -1, 0, 1, -1, 1};

char board[5][5] = {
	{'U', 'R', 'L', 'P', 'M'} ,
	{'U', 'R', 'L', 'P', 'M'} ,
	{'U', 'R', 'A', 'S', 'M'} ,
	{'U', 'R', 'L', 'E', 'M'} ,
	{'U', 'R', 'L', 'P', 'S'} 
};

bool inRange(int y, int x) {
	return (y >= 0) && (y < 5) && (x >= 0) && (x < 5);
}

bool hasWord(int y, int x, const string& word) {
	if(!inRange(y,x)) return false;
	if(board[y][x] != word[0]) return false;

	if(word.size() == 1) return true;

	for(int direction = 0; direction < 8; direction++) {
		int nextY = y + dy[direction], nextX = x + dx[direction];
		if(hasWord(nextY, nextX, word.substr(1)))
			return true;
	}
	return false;
}

int main(void) {

	string str = "ASASASAS";

	if(hasWord(2, 2, str) == true)
		cout<<"TRUE"<<endl;
	cout<<"EXIT"<<endl;

	return 0;
}