#include <iostream>
#include <vector>

using namespace std;

void optimize()
{
    // ios_base::sync_with_stdio(0);
    // cin.tie(false);
}

int main()
{

    optimize();

    long N, X, temp;
    long mortes = 0;
    long i = 0;
    vector<long> pessoas;
    cin >> N;
    cin >> X;

    while (pessoas.size() > 1)
    {
        mortes++;
        if (mortes == X)
        {
            cout << "Morte " << mortes << ": " << pessoas[i] << "\n";
        }
        pessoas.erase(pessoas.begin() + i);
        if (i > pessoas.size() - 1)
        {
            i = 1;
        }
        else if (i + 1 > pessoas.size() - 1)
        {
            i = 0;
        }
        else
        {
            i++;
        }
    }

    cout << "Sobrevivente: " << pessoas[0] << "\n";

    return 0;
}