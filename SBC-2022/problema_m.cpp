#include <iostream>
#include <vector>

using namespace std;

int maxComumDivisor(int x, int y)
{
    if (y == 0)
    {
        return x;
    }
    else
    {
        return maxComumDivisor(y, x % y);
    }
}

void optimize()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
}

int main()
{

    optimize();

    long long n, q;
    long long cq, dq, val;
    long long j, i, k;

    cin >> n >> q;

    vector<long long> jogadores;
    vector<long long> pos;
    vector<long long> casaZero;

    for (i = 0; i < n; i++)
    {
        cin >> val;
        jogadores.push_back(val);
        pos.push_back(i);
        casaZero.push_back(-1);
    }

    long long tam = n;

    for (j = 0; j < q; j++)
    {
        cin >> cq >> dq;
        i = 0;
        while (i < tam)
        {
            if (maxComumDivisor(pos[i] + 1, cq) > 1)
            {
                jogadores[i] -= dq;
                if (jogadores[i] <= 0)
                {
                    casaZero[pos[i]] = j + 1;
                    jogadores.erase(jogadores.begin() + i);
                    pos.erase(pos.begin() + i);
                    tam--;
                }
                else
                {
                    i++;
                }
            }
            else
            {
                i++;
            }
            k++;
        }
        // for (i = 0; i < n; i++)
        // {
        //     cout << casaZero[i] << " | ";
        // }
    }

    for (i = 0; i < n; i++)
    {
        cout << casaZero[i] << "\n";
    }

    return 0;
}

// for (i = 0; i < n; i++)
// {
//     if (jogadores[i] > 0)
//     {
//         if (maxComumDivisor(i + 1, cq) > 1)
//         {
//             jogadores[i] -= dq;
//             if (jogadores[i] <= 0)
//             {
//                 casaZero[i] = j + 1;
//             }
//         }
//     }
// }