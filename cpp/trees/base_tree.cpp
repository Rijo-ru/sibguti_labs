#include <iostream>
#include <time.h>
using namespace std;

typedef int T; // тип элемента
#define compLT(a, b) (a < b)
#define compEQ(a, b) (a == b)

typedef struct Node_
{
    T data;                // значение узла
    struct Node_ *left;    // левый потомок
    struct Node_ *right;   // правый потомок
    struct Node_ *parent;  // родитель
} Node;
Node *root = NULL; // корень бинарного дерева поиска

// функция выделения памяти для нового узла и вставка в дерево
Node *insertNode(T data)
{
    Node *x, *current, *parent;
    current = root;
    parent = 0;
    while (current)
    {
        if (data == current->data)
            return (current);
        parent = current;
        current = data < current->data ? current->left : current->right;
    }
    x = new Node;
    x->data = data;
    x->parent = parent;
    x->left = NULL;
    x->right = NULL;
    if (parent)
    {
        if (x->data < parent->data)
            parent->left = x;
        else
            parent->right = x;
    }
    else
        root = x;
    return (x);
}

// функция удаления узла из дерева
void deleteNode(Node *z)
{
    Node *x, *y;
    if (!z || z == NULL)
        return;
    if (z->left == NULL || z->right == NULL)
        y = z;
    else
    {
        y = z->right;
        while (y->left != NULL)
            y = y->left;
    }
    if (y->left != NULL)
        x = y->left;
    else
        x = y->right;
    if (x)
        x->parent = y->parent;
    if (y->parent)
    {
        if (y == y->parent->left)
            y->parent->left = x;
        else
            y->parent->right = x;
    }
    else
        root = x;
    if (y != z)
    {
        y->left = z->left;
        if (y->left)
            y->left->parent = y;
        y->right = z->right;
        if (y->right)
            y->right->parent = y;
        y->parent = z->parent;
        if (z->parent)
        {
            if (z == z->parent->left)
                z->parent->left = y;
            else
                z->parent->right = y;
        }
        else
            root = y;
        delete z;
    }
    else
    {
        delete y;
    }
}

// функция поиска узла, содержащего data
Node *findNode(T data)
{
    Node *current = root;
    while (current != NULL)
        if (compEQ(data, current->data))
            return (current);
        else
            current = compLT(data, current->data) ? current->left : current->right;
    return (0);
}

// функция вывода бинарного дерева поиска
void printTree(Node *node, int l)
{
    int i;
    if (node != NULL)
    {
        printTree(node->right, l + 1);
        for (i = 0; i < l; i++)
            cout << "  ";
        cout << " " << node->data;
        printTree(node->left, l + 1);
    }
    else
        cout << endl;
}

// использование основных операций в программе
int main()
{
    int i, *a, maxnum;
    cout << "Введите количество элементов maxnum : ";
    cin >> maxnum;
    cout << endl;
    a = new int[maxnum];
    srand(time(NULL) * 10);
    // генерация массива
    for (i = 0; i < maxnum; i++)
        a[i] = rand() % 20 - 10;
    cout << "Вывод сгенерированной последовательности" << endl;
    for (i = 0; i < maxnum; i++)
        cout << a[i] << " ";
    cout << endl;
    cout << endl;
    // добавление элементов в бинарное дерево поиска
    for (i = 0; i < maxnum; i++)
    {
        insertNode(a[i]);
    }
    cout << "Вывод бинарного дерева поиска" << endl;
    printTree(root, 0);
    cout << endl;
    // поиск элементов по бинарному дереву поиска
    for (i = maxnum - 1; i >= 0; i--)
    {
        findNode(a[i]);
    }
    // очистка бинарного дерева поиска
    for (i = 0; i < maxnum; i++)
    {
        deleteNode(findNode(a[i]));
    }
    return 0;
}
