#include <iostream>
#include <vector>

using namespace std;

void printPicked(vector<int>& picked) {
	cout<<"sizze : "<<picked.size()<<endl; 
	for(int i=0; i < picked.size(); i++) {
		cout<<picked[i]<<" ";
	}
	cout<<endl;
}

void pick(int n, vector<int>& picked, int toPick) {
	if(toPick == 0)
		printPicked(picked);

	int smallest = picked.empty() ? 0 : picked.back() + 1;

	for(int next = smallest; next < n; ++next) {
		picked.push_back(next);
		pick(n, picked, toPick - 1);
		picked.pop_back();
	}
}

int main(void) {
	vector<int> vc;

	pick(3, vc, 2);

	return 0;
}