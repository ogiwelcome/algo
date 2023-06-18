#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int m = n, len = 0;
    while (m)
    {
        len++;
        m /= 10;
    }
    n /= pow(10, len - 3);
    n *= pow(10, len - 3);
    cout << n << endl;
    return 0;
}
