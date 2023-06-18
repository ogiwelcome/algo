#include <bits/stdc++.h>
using namespace std;

int main()
{
    int N, M;
    cin >> N >> M;
    vector<vector<int>> a(M, vector<int>(N));
    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> a[i][j];
            a[i][j]--;
        }
    }
    vector<vector<bool>> ok(N, vector<bool>(N, true));
    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N - 1; j++)
        {
            ok[a[i][j]][a[i][j + 1]] = false;
            ok[a[i][j + 1]][a[i][j]] = false;
        }
    }
    int cnt = 0;
    for (int i = 0; i < N; i++)
    {
        for (int j = i + 1; j < N; j++)
        {
            if (ok[i][j])
                cnt++;
        }
    }
    cout << cnt << endl;
}
