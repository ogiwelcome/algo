#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n, a, b;
    cin >> n >> a >> b;
    vector<int> c(n);
    for (int i = 0; i < n; i++)
        cin >> c[i];
    for (int i = 0; i < n; i++)
    {
        if (a + b == c[i])
        {
            cout << i + 1 << endl;
            return 0;
        }
    }
}
