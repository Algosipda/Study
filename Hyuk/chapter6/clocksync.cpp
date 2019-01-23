#include <iostream>

#define INF 9999

using namespace std;

int btn[10][5] = {
	{0, 1, 2, -1, -1} ,
	{3, 7, 9, 11, -1} ,
	{4, 10, 14, 15, -1} ,
	{0, 4, 5, 6, 7} ,
	{6, 7, 8, 10, 12} ,
	{0, 2, 14, 15, -1} ,
	{3, 14, 15, -1, -1} ,
	{4, 5, 7, 14, 15} ,
	{1, 2, 3, 4, 5} ,
	{3, 4, 5, 9, 13}
};

int clk[16];

void printClock() {
	for(int i=0; i<16; i++)
		cout<<clk[i]<<" ";
	cout<<endl;
}

void syncAdd(int btnIndex) {
	for(int i=0; i<5; i++) {
		if(btn[btnIndex][i] != -1) {
			clk[btn[btnIndex][i]] += 3;
			if(clk[btn[btnIndex][i]] == 15)
				clk[btn[btnIndex][i]] = 3;
		}
	}
}

int min(int a, int b) {
	return a < b ? a : b;
}

bool check() {
	bool fini = true;
	for(int i=0; i<16; i++) {
		if(clk[i] != 12) {
			fini = false;
			break;
		}
	}
	if(fini == true) {
		printClock();
	}
	return fini;
}

int click(int now) {
	if(now == 10) return check() ? 0 : INF;

	int ret = INF;
	for(int cnt = 0; cnt < 4; cnt++) {
		ret = min(ret, cnt + click(now + 1));
		syncAdd(now);
	}

	return ret;
}

int main(void) {
	int count;

	cin>>count;

	for(int i=0; i<16; i++) {
		cin>>clk[i];
	}

	cout<<click(0)<<endl;

	printClock();

	return 0;
}