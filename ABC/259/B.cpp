#include <bits/stdc++.h>

using namespace std;
using ll = long long int;

int main() {
    long double a,b,c;
    cin >> a >> b >> c;
    long double deg = 180.000000;
    long double rad = c * M_PI / deg;
    long double a_d = a*cos(rad) - b*sin(rad);
    long double b_d = a*sin(rad) + b*cos(rad);
    cout << setprecision(7) << a_d << " " << setprecision(7) << b_d << endl;
}
