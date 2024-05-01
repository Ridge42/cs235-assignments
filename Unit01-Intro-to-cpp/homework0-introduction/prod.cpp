#include <iostream>
using std::cout, std::endl, std::cerr;

#include <cstdlib>
using std::strtod;

int main(int argc, char const* argv[]) {
    char* end;

    if (argc > 2) {
        double num1 = strtod(argv[1], &end);
        double num2 = strtod(argv[2], &end);
        cout << num1 << " * " << num2 << " = " << num1 * num2 << endl;
    }
    else {
        cerr << "prod requires 2 arguments" << endl;
        return 1;
    }

    return 0;
}
//  :)
