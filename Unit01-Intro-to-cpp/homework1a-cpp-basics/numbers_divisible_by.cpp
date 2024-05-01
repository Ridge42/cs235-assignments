#include <iostream>
using std::cout, std::endl, std::cerr;

#include <cstdlib>

int main(int argc, char const* argv[]) {

    int start = atoi(argv[1]);
    int end = atoi(argv[2]);
    int divisor = atoi(argv[3]);

    if (start < end) {
        for (;end >= start; start++) {
            if (start % divisor == 0) {
                cout << start << endl;
            }
        }
    }
    else if (start >= end) {
        for (; start >= end; end++) {
            if (end % divisor == 0) {
                cout << end << endl;
            }
        }
    }

    return 0;
}

