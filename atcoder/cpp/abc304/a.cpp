#include <bits/stdc++.h>
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<string> S(N);
    vector<int> A(N);
    for (int i = 0; i < N; i++)
    {
        cin >> S[i] >> A[i];
    }
    int p = 0;
    for (int i = 1; i < N; i++)
    {
        if (A[i] < A[p])
        {
            p = i;
        }
    }
    for (int i = 0; i < N; i++)
    {
        cout << S[(p + i) % N] << endl;
    }
}
