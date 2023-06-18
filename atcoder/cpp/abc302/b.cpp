#include <bits/stdc++.h>
using namespace std;

vector<int> dx = {1, 0, -1, 0, 1, 1, -1, -1};
vector<int> dy = {0, 1, 0, -1, 1, -1, 1, -1};
int main()
{
    int H, W;
    cin >> H >> W;
    vector<string> S(H);
    for (int i = 0; i < H; i++)
    {
        cin >> S[i];
    }
    for (int i = 0; i < H; i++)
    {
        for (int j = 0; j < W; j++)
        {
            for (int k = 0; k < 8; k++)
            {
                bool ok = true;
                for (int l = 0; l < 5; l++)
                {
                    int nx = i + dx[k] * l;
                    int ny = j + dy[k] * l;
                    if (!(0 <= nx && nx < H && 0 <= ny && ny < W))
                    {
                        ok = false;
                    }
                    else if (S[nx][ny] != "snuke"[l])
                    {
                        ok = false;
                    }
                }
                if (ok)
                {
                    for (int l = 0; l < 5; l++)
                    {
                        cout << i + dx[k] * l + 1 << ' ' << j + dy[k] * l + 1 << endl;
                    }
                }
            }
        }
    }
}
