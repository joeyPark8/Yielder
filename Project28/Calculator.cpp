#include "Yielder.h"

int main() {
	yielder yid;
	yid.load();

	yid.yield();

	/*
	for (auto [subject, score] : yid.results) {
		cout << subject << "   " << score << endl;
	}
	*/

	yid.save();
	
	return 0;
}