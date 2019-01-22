#include <iostream>
#include <cmath>

using namespace std;

bool areFriends[10][10];
bool mat[10];

int trip(int frid) {
	int count = 0;
	bool finish = true;
	int start = 0;

	for(int i=0; i < frid; i++) {
		if(mat[i] == false) {
			start = i;
			finish = false;
			break;
		}
	}
	if(finish == true)	return 1;

	for(int i=start+1; i<frid; i++) {
		if(!mat[i] && !mat[start] && areFriends[i][start]) {
			mat[i] = true;
			mat[start] = true;
			count += trip(frid);
			mat[i] = false;
			mat[start] = false;
		}
	}
	return count;
}

int main(void) {
	int count, frid, cop;
	int friendly[2];

	cout<<"---------------"<<endl;
	cin>>count;

	for( ; count > 0 ; count--) {
		memset(areFriends, 0, 100 * sizeof(int));
		memset(mat, 0, 10 * sizeof(int));

		cin>>frid;
		cin>>cop;

		for(int i = 0; i < cop; i++) {
			cin>>friendly[0];
			cin>>friendly[1];
			areFriends[friendly[0]][friendly[1]] = true;
			areFriends[friendly[1]][friendly[0]] = true;
		}

		cout<<trip(frid)<<endl;
		cout<<"-------------------"<<endl;
	}

	return 0;
}