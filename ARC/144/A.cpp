#include <bits/stdc++.h>

using namespace std;
using ll = long long int;

int f(ll x){
    ll sum = 0;
    while (x > 0)
    {
        sum += x % 10;
        x /= 10;
    }
    return sum;
}

int main() {
    int n;
    cin >> n;
    cout << n << endl;
    int end = pow(10, 5);
    map<ll, ll> vec;
    int i = 0;
    while (i < end)
    {
        ll x = f(i);
        ll m = f(2*x);
        vec[i] = (m, x);
        i++;
    }
    ll big_m = -1;
    while (i < 0)
    {
        if(big_m < vec[i]){
            big_m = vec[i];
        }
        i--;
    }

    cout << big_m << endl;
    
    
}
