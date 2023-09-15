#include <iostream>
#include <cmath>
using namespace std;


double M(double x) {
    return -185 * x + 1650;
}

double bisection(double a, double b, double epsilon) {
    double c;
    int iterations = 0;

    while ((b - a) >= epsilon) {
        c = (a + b) / 2;

        if (M(c) == 0.0) {
            break;
        }
        else if (M(c) * M(a) < 0) {
            b = c;
        }
        else {
            a = c;
        }

        iterations++;
    }

    return c;
}

int main() {
    double a = 6.0;
    double b = 10.0;
    double epsilon = 0.00001;

    double root = bisection(a, b, epsilon);

    if (root >= 6 && root <= 10) {
        cout << "La raíz en el intervalo [6, 10] es aproximadamente: " << root << endl;
        cout << "M(" << root << ") = " << M(root) << endl;
    }
    else {
        cout << "No se encontró una raíz en el intervalo [6, 10]." << endl;
    }

    return 0;
}
