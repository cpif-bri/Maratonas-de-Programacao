#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int p[8], n, t[100][9], m;

    for (int i = 0; i < 8; i++)
    {
        cin >> p[i];
    }

    cin >> n;

    for (int i = 0; i < n; i++)
    {
        int cont = 0;

        for (int j = 0; j < 8; j++)
        {
            cin >> t[i][j];
            if( t[i][j] == p[j])
            {
                cont++;
            }
        }

        t[i][8] = cont;
    }

    cin >> m;
    int passa = 0;
    double corte;

    for (int i = 0; i < m; i++)
    {
        passa = 0;
        cin >> corte;
        for (int j = 0; j < n; j++)
        {
            if((double(t[j][8]) / 8) * 100 >= corte)
            {
                passa++;
            }
        }

        cout << fixed << setprecision(2) << (double(passa) / n) * 100 << endl;
    }

    return 0;
}
