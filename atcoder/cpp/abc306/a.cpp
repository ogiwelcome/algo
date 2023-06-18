#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    string s;
    cin >> n >> s;
    string ans;
    for (char c : s)
    {
        ans += c;
        ans += c;
    }
    cout << ans << endl;
    return 0;
}
