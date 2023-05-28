#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

int sumOddElements(Node* head) {
    int sum = 0;
    while (head != NULL) {
        if (head->data % 2 != 0) {
            sum += head->data;
        }
        head = head->next;
    }
    return sum;
}

void delNode(Node*& head) {
    if (head == NULL) {
        cout << "Список пуст" << endl;
        return;
    }

    int sum = 0;
    int count = 0;
    Node* current = head;
    while (current != NULL) {
        sum += current->data;
        count++;
        current = current->next;
    }
    double avg = static_cast<double>(sum) / count;
    cout << "Среднее значение равно: " << avg << endl;

    if (head->data < avg) {
        Node* temp = head;
        head = head->next;
        cout << "Удаляемое число равно = " << temp << endl;
        delete temp;
        return;
    }    

    Node* prev = head;
    current = head->next;
    while (current != NULL) {
        if (current->data < avg) {
            prev->next = current->next;
            cout << "Удаляемое число равно = " << current->data << endl;
            delete current;
            return;
        }
        prev = current;
        current = current->next;
    }

    cout << "Не найдено элементов меньше среднего значения." << endl;
}

void printList(Node* head) {
    if (head == NULL) {
        cout << "Список пуст!" << endl;
        return;
    }

    Node* current = head;
    while (current != NULL) {
        cout << current->data << " ";
        current = current->next;
    }
    cout << endl;
}

void addNode(Node*& head, int value) {
    Node* newNode = new Node;
    newNode->data = value;
    newNode->next = NULL;

    if (head == NULL) {
        head = newNode;
    } else {
        Node* current = head;
        while (current->next != NULL) {
            current = current->next;
        }
        current->next = newNode;
    }
}

int main() {
    Node* head = NULL;
    int n, val;
    cout << "Введите количество элементов списка: ";
    cin >> n;
    cout << "Введите значения элементов списка: " << endl;
    for (int i = 0; i < n; i++) {
        cout << "Элемент " << i + 1 << ": ";
        cin >> val;
        addNode(head, val);
    }
    cout << "Список: ";
    printList(head);

    cout << "Сумма нечетных элементов равна: " << sumOddElements(head) << endl;

    delNode(head);
    printList(head);
    return 0;
}
