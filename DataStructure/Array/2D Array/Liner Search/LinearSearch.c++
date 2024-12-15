#include <iostream>
using namespace std;

bool linearSearch(int mtx[][2], int rows, int cols, int key)
{
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            if (mtx[i][j] == key)
            {
                return true;
            }
        }
    }
    return false;
}

int main()
{

    int matrix_array[3][2] = {{1, 2}, {3, 4}, {5, 6}}; // two dimantional Aray = [* *]
    int rows = 3;
    int cols = 2;

    cout << linearSearch(matrix_array,rows,cols,0);
}