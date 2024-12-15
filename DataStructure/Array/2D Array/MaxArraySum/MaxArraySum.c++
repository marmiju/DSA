#include <iostream>
using namespace std;

int sumofarrysrow(int array[][3], int rows,int cols)
{
    int maxofarrayrowsum = 0; 
   for (int i=0; i<rows;i++){
     int sum = 0;
       for (int j = 0; j < cols; j++)
       {
         sum += array[i][j];
       }
       if (sum>maxofarrayrowsum){
         maxofarrayrowsum = sum;
       }
       
   }
   return maxofarrayrowsum;
}


int main()
{
    int arr[3][3] = {{1,3,5},{5,36,6},{8,6,3}};
    int rows = 3;
    int cols =3;

    cout << sumofarrysrow(arr,rows,cols)<<endl;

    return 0;
}



