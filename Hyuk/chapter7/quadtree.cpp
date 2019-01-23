#include <iostream>

using namespace std;

string quadtree(string old) {
	string newStr[4];

	if(old.size() == 1 || old.size() == 0)
		return old;

	for(int i=0, j=0; i<old.size() && j < 4; j++) {
		if(old[i] == 'x') {
			newStr[j] = old[i] + quardtree(old.substr(i+1, old.size()));
			i += newStr[j].size();
		}
		else {
			newStr[j] = old[i];
			i++;
		}
	}
	
	old = newStr[2] + newStr[3] + newStr[0] + newStr[1];

	return old;
}


int main(void) {

	string str;
	int count;
	cin>>count;

	for(int i=0; i<count; i++) {
		cin>>str;

		str = quadtree(str.substr(0, str.size()));

		cout<<str<<endl;
	}

	return 0;
}