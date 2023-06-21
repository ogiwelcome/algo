#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    char s[n];
    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> s[i];
    bool flg = false;
    for (int i = 0; i < n; i++)
    {
        if (s[i] == '*' && flg)
        {
            cout << "in" << endl;
            break;
        }
        else if (s[i] == '|' && flg)
        {
            cout << "out" << endl;
            break;
        }
        else if (s[i] == '|')
        {
            flg = true;
        }
    }
    return 0;
}
