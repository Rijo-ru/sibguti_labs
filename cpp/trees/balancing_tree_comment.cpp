#include <iostream> // Подключение библиотеки для ввода/вывода данных
#include <time.h> // Подключение библиотеки для работы со временем

using namespace std; // Использование пространства имен std

typedef int ElementType; // Определение псевдонима типа данных ElementType как int
typedef struct AvlNode *Position; // Определение указателя Position на структуру AvlNode
typedef struct AvlNode *AvlTree; // Определение указателя AvlTree на структуру AvlNode
struct AvlNode { // Определение структуры AvlNode
    ElementType Element; // Поле структуры - значение элемента
    AvlTree Left; // Поле структуры - указатель на левое поддерево
    AvlTree Right; // Поле структуры - указатель на правое поддерево
    int Height; // Поле структуры - высота узла в дереве
};

AvlTree MakeEmpty(AvlTree T); // Прототип функции очистки дерева
Position Find(ElementType X, AvlTree T); // Прототип функции поиска элемента в дереве
Position FindMin(AvlTree T); // Прототип функции поиска минимального элемента в дереве
Position FindMax(AvlTree T); // Прототип функции поиска максимального элемента в дереве
AvlTree Insert(ElementType X, AvlTree T); // Прототип функции вставки элемента в дерево
AvlTree Delete(ElementType X, AvlTree T); // Ппрототип функции удаления элемента из дерева
ElementType Retrieve(Position P); // Прототип функции получения значения из узла
void printTree(AvlTree T, int l = 0); // Прототип функции вывода дерева на экран

int main() { // Основная функция программы
    int i, *a, maxnum, delnum; // Объявление переменных
    AvlTree T; // Объявление переменной для хранения дерева
    Position P; // Объявление переменной для хранения позиции в дереве
    int j = 0; // Инициализация переменной j
    cout << "Введите количество элементов maxnum : "; // Вывод сообщения на экран
    cin >> maxnum; // Чтение значения из ввода пользователя
    cout << endl; // Вывод пустой строки

    a = new int[maxnum]; // Выделение памяти под массив размером maxnum
    srand(time(NULL) * 1000); // Инициализация генератора случайных чисел

    // генерация массива случайных чисел
    for (i = 0; i < maxnum; i++) // Цикл заполнения массива случайными числами
        a[i] = rand() % 100; // Заполнение элементов массива случайными числами от 0 до 99

    cout << "Вывод сгенерированной последовательности" << endl; // Вывод сообщения на экран
    for (i = 0; i < maxnum; i++) // Цикл вывода элементов массива на экран
        cout << a[i] << " "; // Вывод очередного элемента массива

    cout << endl << endl; // Вывод двух пустых строк

    T = MakeEmpty(NULL); // Очистка дерева
    for (i = 0; i < maxnum; i++) // Цикл вставки элементов массива в дерево
        T = Insert(a[i], T); // Вставка элемента в дерево

    cout << "Вывод АВЛ-дерева" << endl; // Вывод сообщения на экран
    printTree(T); // Вывод дерева на экран
    cout << endl; // Вывод пустой строки

    cout << "Min = " << Retrieve(FindMin(T)) << ", Max = " // Вывод сообщения на экран с минимальным и максимальным значением
         << Retrieve(FindMax(T)) << endl;

    cout << "Введите число, которое нужно удалить : "; // Вывод сообщения на экран
    cin >> delnum; // Чтение значения из ввода пользователя
    cout << endl; // Вывод пустой строки

    T = Delete(delnum, T); // Удаление элемента из дерева
    cout << endl; // Вывод пустой строки
    
    printTree(T); // Вывод дерева на экран

    T = MakeEmpty(T); // Очистка памяти, выделенной под дерево
    delete[] a; // Освобождение памяти, выделенной для массива

    return 0; // Возврат нуля как кода успешного завершения программы
}

// Функция очистки дерева
AvlTree MakeEmpty(AvlTree T) {
    if (T != NULL) { // Если дерево не пустое
        MakeEmpty(T->Left); // Рекурсивно очищаем левое поддерево
        MakeEmpty(T->Right); // Рекурсивно очищаем правое поддерево
        free(T); // Освобождаем память, занимаемую текущим узлом
    }
    return NULL; // Возвращаем NULL, указывая на пустое дерево
}

// Функция поиска элемента в дереве
Position Find(ElementType X, AvlTree T) {
    if (T == NULL) // Если дерево пустое или элемент не найден
        return NULL; // Возвращаем NULL, элемент не обнаружен
    if (X < T->Element) // Если искомое значение меньше значения текущего узла
        return Find(X, T->Left); // Рекурсивно ищем элемент в левом поддереве
    else if (X > T->Element) // Если искомое значение больше значения текущего узла
        return Find(X, T->Right); // Рекурсивно ищем элемент в правом поддереве
    else
        return T; // Элемент найден, возвращаем указатель на узел
}

// Функция поиска минимального элемента в дереве
Position FindMin(AvlTree T) {
    if (T == NULL) // Если дерево пустое
        return NULL; // Возвращаем NULL, минимальный элемент не обнаружен
    else if (T->Left == NULL) // Если нет левого поддерева
        return T; // Возвращаем указатель на текущий узел
    else
        return FindMin(T->Left); // Рекурсивно ищем минимальный элемент в левом поддереве
}

// Функция поиска максимального элемента в дереве
Position FindMax(AvlTree T) {
    if (T != NULL) { // Если дерево не пустое
        while (T->Right != NULL) // Пока есть правое поддерево
            T = T->Right; // Переходим к правому узлу
    }
    return T; // Возвращаем указатель на максимальный узел
}

// Функция возвращает высоту узла
static int Height(Position P) {
    if (P == NULL)
        return -1; // Возвращаем -1, если узел не существует (пустой)
    else
        return P->Height; // Возвращаем высоту узла
}

// Функция возвращает максимальное из двух чисел
static int Max(int Lhs, int Rhs) {
    return Lhs > Rhs ? Lhs : Rhs; // Возвращаем большее из двух чисел
}

// Функция выполняет одиночный поворот влево между узлами K2 и её левым потомком
static Position SingleRotateWithLeft(Position K2) {
    Position K1;
    K1 = K2->Left;
    K2->Left = K1->Right;
    K1->Right = K2;
    K2->Height = Max(Height(K2->Left), Height(K2->Right)) + 1;
    K1->Height = Max(Height(K1->Left), K2->Height) + 1;
    return K1; // Новый корень
}

// Функция выполняет одиночный поворот вправо между узлами K1 и её правым потомком
static Position SingleRotateWithRight(Position K1) {
    Position K2;
    K2 = K1->Right;
    K1->Right = K2->Left;
    K2->Left = K1;
    K1->Height = Max(Height(K1->Left), Height(K1->Right)) + 1;
    K2->Height = Max(Height(K2->Right), K1->Height) + 1;
    return K2; // Новый корень
}

// Функция выполняет двойной поворот влево-право
static Position DoubleRotateWithLeft(Position K3) {
    // Поворот между K1 и K2
    K3->Left = SingleRotateWithRight(K3->Left);
    // Поворот между K3 и K2
    return SingleRotateWithLeft(K3);
}

// Функция выполняет двойной поворот право-влево
static Position DoubleRotateWithRight(Position K1) {
    // Поворот между K3 и K2
    K1->Right = SingleRotateWithLeft(K1->Right);
    // Поворот между K1 и K2
    return SingleRotateWithRight(K1);
}

// Функция вставки элемента в АВЛ-дерево
AvlTree Insert(ElementType X, AvlTree T) {
    if (T == NULL) { // Если дерево пустое
        T = new AvlNode(); // Выделяем память под новый узел
        if (T == NULL)
            fprintf(stderr, "Недостаточно памяти!!!\n"); // Вывод сообщения об ошибке
        else {
            T->Element = X; T->Height = 0; // Устанавливаем значение и высоту узла
            T->Left = T->Right = NULL; // Обнуляем ссылки на поддеревья
        }
    } else if (X < T->Element) { // Идем в левое поддерево
        T->Left = Insert(X, T->Left); // Рекурсивно вставляем элемент в левое поддерево
        if (Height(T->Left) - Height(T->Right) == 2) // Балансировка
            if (X < T->Left->Element) // Проверяем тип поворота
                T = SingleRotateWithLeft(T);
            else
                T = DoubleRotateWithLeft(T);
    } else if (X > T->Element) { // Идем в правое поддерево
        T->Right = Insert(X, T->Right); // Рекурсивно вставляем элемент в правое поддерево
        if (Height(T->Right) - Height(T->Left) == 2) // Балансировка
            if (X > T->Right->Element) // Проверяем тип поворота
                T = SingleRotateWithRight(T);
            else
                T = DoubleRotateWithRight(T);
    }
    T->Height = Max(Height(T->Left), Height(T->Right)) + 1; // Обновляем высоту узла
    return T; // Возвращаем указатель на корень дерева
}

// Функция возвращает значение элемента, хранящееся в вершине
ElementType Retrieve(Position P) {
    return P->Element; // Возвращаем значение узла
}

// Функция вывода АВЛ-дерева на экран
void printTree(AvlTree T, int l) {
    int i;
    if (T != NULL) { // Если дерево не пустое
        printTree(T->Right, l + 1); // Рекурсивно выводим правое поддерево
        for (i = 0; i < l; i++) cout << "    "; // Выводим отступы
        printf("%4ld", Retrieve(T)); // Выводим значение текущего узла
        printTree(T->Left, l + 1); // Рекурсивно выводим левое поддерево
    } else
        cout << endl; // Выводим пустую строку для пустого узла
}

// Функция удаления элемента из дерева по значению
AvlTree Delete(ElementType X, AvlTree T) {
    if (T == NULL) { // Если дерево пустое или элемент не найден
        return NULL; // Возвращаем NULL, элемент не обнаружен
    }
    if (X < T->Element) { // Если искомое значение меньше значения текущего узла
        T->Left = Delete(X, T->Left); // Рекурсивно удаляем элемент из левого поддерева
    } else if (X > T->Element) { // Если искомое значение больше значения текущего узла
        T->Right = Delete(X, T->Right); // Рекурсивно удаляем элемент из правого поддерева
    } else { // Найден узел для удаления
        if (T->Left == NULL) { // Если нет левого потомка
            AvlTree temp = T->Right; // Сохраняем ссылку на правого потомка
            free(T); // Освобождаем память узла
            return temp; // Возвращаем правого потомка для присоединения к родительскому узлу
        } else if (T->Right == NULL) { // Если нет правого потомка
            AvlTree temp = T->Left; // Сохраняем ссылку на левого потомка
            free(T); // Освобождаем память узла
            return temp; // Возвращаем левого потомка для присоединения к родительскому узлу
        }
        // Узел имеет двух потомков
        AvlTree temp = FindMin(T->Right); // Находим минимальный узел в правом поддереве
        T->Element = temp->Element; // Копируем значение минимального узла
        T->Right = Delete(temp->Element, T->Right); // Удаляем узел с минимальным значением из правого поддерева
    }
    return T; // Возвращаем указатель на измененное дерево
}

