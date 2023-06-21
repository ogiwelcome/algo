#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n, t;
    cin >> n >> t;
    vector<int> c(n);
    for (int i = 0; i < n; i++)
        cin >> c[i];
    vector<int> r(n);
    for (int i = 0; i < n; i++)
        cin >> r[i];
    int ans = 0;
    for (int i = 1; i < n; i++)
    {
        if (c[ans] == c[i] && r[i] > r[ans] || c[ans] != t && c[i] == t)
            ans = i;
    }
    cout << ans + 1 << endl;
}