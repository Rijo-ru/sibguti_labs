#include <iostream>
using namespace std;

// нужно сформировать исходный список целых чисел и вывести
// его на экран, затем решить задачу и вывести результат
// сумму нечетных элементов
struct Node { // создание структуры для элемента списка
    int data;
    Node* next;
};

// Функция добавления элемента в список
void addNode(Node*& head, int val) {
    Node* newNode = new Node;
    newNode->data = val;
    newNode->next = head;
    head = newNode;
}

// Функция для печати списка
void printList(Node* head) {
    while (head != NULL) {
        cout << head->data << " ";
        head = head->next;
    }
}

// Функция нахождения суммы нечетных элементов
int sumOddElements(Node* Head) {
    int sum = 0;
    while (Head != NULL) {
        if (Head->data % 2 != 0) {
            sum += Head->data;
        }
        Head = Head->next;
    }
    return sum;
}

// Функция удаления первого элемента, который меньший среднего
void delNode(Node** Head) {
    if (*Head == NULL) {
        cout << "Список пуст";
        return;
    }

    Node* temp = *Head;
    Node* prev = NULL;
    int sum = 0;
    int count = 0;
    
    // считаем сумму элементов списка
    while (temp != NULL) {
        sum += temp->data;
        count++;
        temp = temp->next;
    }

    double avg = (double)sum / count; // находим среднее

    temp = *Head;
    
    // поиск и удаление первого элемента, который ниже среднеего значения
    while (temp != NULL && temp->data < avg) {
        *Head = temp->next;
        delete temp;
        temp = *Head;
    }
}


int main() {
    Node* Head = NULL;
    int n, val;
    cout << "Введите количество элементов списка: ";
    cin >> n;
    cout << "Введите значения элементов списка: " << "\n";
    for (int i = 0; i < n; i++) {
        cout << "Элемент: " << i + 1 << "\t";
        cin >> val;
        addNode(Head, val);
    }
    cout << "Список: ";
    printList(Head);
    
    cout << "Сумма нечетных элемнтов равна:" << sumOddElements(Head);
    return 0;
}