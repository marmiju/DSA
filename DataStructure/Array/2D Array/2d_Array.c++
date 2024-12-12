#include <iostream>
using namespace std;

int main()
{
    int matrix_array[3][2] = {{1,2},{3,4},{5,6}}; // two dimantional Aray = [* *]
    int rows = 3;
    int cols = 2;                                                   //      [* *]
                                                                   //       [* *]

     cout<<matrix_array[2][1]<<endl; // result 6

     //print 2d Array Value with Loop 
     for(int i=0; i<rows;i++)
     {
         for (int j = 0; j < cols; j++)
         {
            cout<<matrix_array[i][j]<<" "; //Space after Ever number printed
         }
         cout<<endl;  // line breake for Every rows
         
     }


     return 0;
}