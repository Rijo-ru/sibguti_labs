#include <iostream>
#include <time.h>

using namespace std;

typedef int ElementType;
typedef struct AvlNode *Position;
typedef struct AvlNode *AvlTree;
struct AvlNode {
            ElementType Element;
            AvlTree Left;
            AvlTree Right;
            int Height;
        };

AvlTree MakeEmpty( AvlTree T );
Position Find( ElementType X, AvlTree T );
Position FindMin( AvlTree T );
Position FindMax( AvlTree T );
AvlTree Insert( ElementType X, AvlTree T );
ElementType Retrieve( Position P );
void printTree(AvlTree T, int l = 0);

int main(){
  int i, *a, maxnum;
  AvlTree T;
  Position P;
  int j = 0;
  cout << "Введите количество элементов maxnum : ";
  cin >> maxnum;
  cout << endl;

  a = new int[maxnum];
  srand(time(NULL)*1000);

  // генерация массива
  for (i = 0; i < maxnum; i++)
    a[i] = rand()%100;

  cout << "Вывод сгенерированной последовательности" << endl;
  for (i = 0; i < maxnum; i++)
    cout << a[i] << " ";
  
  cout << endl;
  cout << endl;

  // добавление элементов в АВЛ-дерево
  T = MakeEmpty( NULL );
  for( i = 0; i < maxnum; i++ )
        T = Insert( a[i], T );

  cout << "Вывод АВЛ-дерева" << endl;
  printTree(T);
  cout << endl;

  cout << "Min = " << Retrieve( FindMin( T ) ) << ", Max = "
       << Retrieve( FindMax( T ) ) << endl;
       
  // удаление АВЛ-дерева
  T = MakeEmpty(T);
  delete [] a;

return 0;
}

//функция удаления вершины и ее поддеревьев
AvlTree MakeEmpty( AvlTree T ) {
  if( T != NULL ){
    MakeEmpty( T->Left );
    MakeEmpty( T->Right );
    free( T );
  }
  return NULL;
}

// поиск вершины со значением X
Position Find( ElementType X, AvlTree T ) {
  if( T == NULL )
    return NULL;
  if( X < T->Element )
      return Find( X, T->Left );
    else
      if( X > T->Element )
        return Find( X, T->Right );
      else
        return T;
}

//функция поиска вершины с минимальным значением
Position FindMin( AvlTree T ) {
  if( T == NULL )
    return NULL;
  else
    if( T->Left == NULL )
      return T;
    else
      return FindMin( T->Left );
}

//функция поиска вершины с максимальным значением
Position FindMax( AvlTree T ) {
  if( T != NULL )
    while( T->Right != NULL )
      T = T->Right;
  return T;
}

//функция возвращает вес вершины
static int Height( Position P ) {
  if( P == NULL )
    return -1;
  else
    return P->Height;
}

//функция возвращает максимальное из двух чисел
static int Max( int Lhs, int Rhs ) {
  return Lhs > Rhs ? Lhs : Rhs;
}

/*функция выполняет поворот между вершинами K2 и ее левым потомком*/
static Position SingleRotateWithLeft( Position K2 ) {
  Position K1;
  K1 = K2->Left;
  K2->Left = K1->Right;
  K1->Right = K2;
  K2->Height = Max(Height(K2->Left), Height(K2->Right)) + 1;
  K1->Height = Max( Height( K1->Left ), K2->Height ) + 1;
  return K1;  //Новый корень
}

//функция выполняет поворот между вершинами K1 и ее правым потомком
static Position SingleRotateWithRight( Position K1 ) {
  Position K2;
  K2 = K1->Right;
  K1->Right = K2->Left;
  K2->Left = K1;
  K1->Height = Max(Height(K1->Left), Height(K1->Right)) + 1;
  K2->Height = Max( Height( K2->Right ), K1->Height ) + 1;
  return K2;  //новый корень
}

//функция выполняет двойной левый-правый поворот
static Position DoubleRotateWithLeft( Position K3 ) {
  // поворот между K1 и K2/
  K3->Left = SingleRotateWithRight( K3->Left );
  // поворот между K3 и K2
  return SingleRotateWithLeft( K3 );
}

//функция выполняет двойной правый-левый поворот
static Position DoubleRotateWithRight( Position K1 ) {
  // поворот между K3 и K2
  K1->Right = SingleRotateWithLeft( K1->Right );
  // поворот между K1 и K2
  return SingleRotateWithRight( K1 );
}

//функция вставки вершины в АВЛ-дерево
AvlTree Insert( ElementType X, AvlTree T ){
  if( T == NULL ){ //дерево пустое
    T = new AvlNode();
    if( T == NULL )
      fprintf( stderr, "Недостаточно памяти!!!\n" );
    else {  //добавился элемент в корень дерева
      T->Element = X; T->Height = 0;
      T->Left = T->Right = NULL; // обнуляем поддеревья
    }
  }  //дерево не пустое
  else if( X < T->Element ) { // идем в левое поддерево
    T->Left = Insert( X, T->Left );
    if( Height( T->Left ) - Height( T->Right ) == 2 )
      if( X < T->Left->Element ) // балансировка
        T = SingleRotateWithLeft( T );
      else
        T = DoubleRotateWithLeft( T );
  }
  else if( X > T->Element ) {  // идем в правое поддерево
    T->Right = Insert( X, T->Right );
      if( Height( T->Right ) - Height( T->Left ) == 2 )
        if( X > T->Right->Element )  // балансировка
          T = SingleRotateWithRight( T );
        else
          T = DoubleRotateWithRight( T );
  }
  T->Height = Max(Height(T->Left), Height(T->Right)) + 1;
  return T;
}

//функция возвращает значение, хранящееся в вершине
ElementType Retrieve( Position P ) {
  return P->Element;
}

//функция вывода АВЛ-дерева на печать
void printTree(AvlTree T, int l){
  int i;
  if ( T != NULL ) {
    printTree(T->Right, l+1);
    for (i=0; i < l; i++) cout << "    ";
    printf ("%4ld", Retrieve ( T ));
    printTree(T->Left, l+1);
  }
  else cout << endl;
}