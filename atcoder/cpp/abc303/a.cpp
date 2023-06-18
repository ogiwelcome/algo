#include <iostream>
using namespace std;

int main()
{
    int n;
    string a, b;
    cin >> n >> a >> b;
    int c = 0;
    for (int i = 0; i < n; i++)
    {
        if (a[i] == b[i])
        {
            c++;
        }
        else if ((a[i] == '0' && b[i] == 'o') || (a[i] == 'o' && b[i] == '0') || (a[i] == '1' && b[i] == 'l') || (a[i] == 'l' && b[i] == '1'))
        {
            c++;
        }
    }
    if (c == n)
    {
        cout << "Yes" << endl;
    }
    else
    {
        cout << "No" << endl;
    }
}
