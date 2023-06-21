#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    char y;
    int t = 0, a = 0;
    for (int i = 0; i < n; i++)
    {
        cin >> y;
        if (y == 'T')
            t++;
        else
            a++;
        if (i == n - 1 && n % 2 == 0)
        {
            if (y == 'T')
                a++;
            else
                t++;
        }
    }
    if (t > a)
    {
        cout << "T" << endl;
    }
    else
    {
        cout << "A" << endl;
    }
}
