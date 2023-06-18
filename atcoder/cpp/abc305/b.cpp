#include <bits/stdc++.h>
using namespace std;

int main()
{
    int ans = 0;
    char p, q;
    cin >> p >> q;
    if (q < p)
        swap(p, q);
    vector<int> a = {3, 1, 4, 1, 5, 9};
    for (int i = p - 65; i < q - 65; i++)
    {
        ans += a.at(i);
    }
    cout << ans << endl;
}
