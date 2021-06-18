/*
    Nhóm 5:
    Cao Trần Hoàng
    Nguyễn Quang Huy
    Trần Lê Huy

    Câu hỏi cho nhóm thuyết trình: Thuật toán tham lam nên được sử dụng như thế nào để tránh đưa ra những kết quả không chính xác ?
*/
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

typedef struct {
    int value;
    int weight;
    float density;
}Item;

void input(Item items[],int sizeOfItems){
    cout << "Nhap gia tri va can nang cua "<< sizeOfItems <<" mon hang" << endl;
    for(int i=0; i<sizeOfItems; i++){
        cout << "Mon hang "<< i+1 << " co gia tri ";
        cin >> items[i].value;
        cout << "Mon hang "<< i+1 << " co can nang ";
        cin >> items[i].weight;
    }
}

void display(Item items[],int sizeOfItems){
  cout << "Gia tri:   ";
  for(int i=0; i<sizeOfItems; i++){
      cout << items[i].value << "\t";
  }

  cout << endl << "Can nang:   ";
  for(int i=0; i<sizeOfItems; i++){
      cout << items[i].weight << "\t";
  }
  cout << endl;
}

bool compare(Item i1, Item i2){
    return (i1.density > i2.density);
}

float knapsack(Item items[],int sizeOfItems, int W){
    float totalValue=0, totalWeight=0;
    for(int i=0; i<sizeOfItems; i++){
        items[i].density = items[i].value/items[i].weight;
    }
    sort(items, items+sizeOfItems,compare);

  for(int i=0; i<sizeOfItems; i++){
    if(totalWeight + items[i].weight<= W){
      totalValue += items[i].value ;
      totalWeight += items[i].weight;
    } else {
      int wt = W-totalWeight;
      totalValue += (wt * items[i].density);
      totalWeight += wt;
      break;
    }
}
  cout << "Tong gia tri can nang " << totalWeight<<endl;
  return totalValue;
}
int main()
{
  int W;
  int n;
  cout<<"So mon do trong cua hang: ";
  cin>>n;
  Item items[n];
  input(items,n);
  cout<< "Nhap gioi han ma balo co the chua: ";
  cin >> W;
  cout << "Cac thong tin duoc nhap \n";
  display(items,n);

  float mxVal = knapsack(items,n,W);
  cout << "-->Gia tri max de co duoc ket qua toi uu nhat la "<< mxVal;
  return 0;
}
