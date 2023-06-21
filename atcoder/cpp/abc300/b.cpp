#include <iostream>
using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    char a[n][m], b[n][m];
    for (int i = 0; i < n; i++)
        cin >> a[i];
    for (int i = 0; i < n; i++)
        cin >> b[i];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            bool flg = true;
            for (int k = 0; k < n; k++)
            {
                for (int l = 0; l < m; l++)
                {
                    if (a[(i + k) % n][(j + l) % m] != b[k][l])
                    {
                        flg = false;
                    }
                }
            }
            if (flg)
            {
                cout << "Yes" << endl;
                return 0;
            }
        }
    }
    cout << "No" << endl;
    return 0;
}
