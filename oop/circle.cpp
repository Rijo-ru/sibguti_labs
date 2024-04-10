#include <iostream>
#include <cmath>

using namespace std;

class Location {
public:
    double x;
    double y;

    Location() : x(0), y(0) {}
    Location(const Location& obj) : x(obj.x), y(obj.y) {}
    Location(double xx, double yy) : x(xx), y(yy) {}
};

class Clip {
public:
    Location min;
    Location max;

    Clip() : min(), max() {}
    Clip(const Clip& obj) : min(obj.min), max(obj.max) {}
    Clip(double xn, double yn, double xk, double yk) {
        if (xn < xk) { min.x = xn; max.x = xk; }
        else { min.x = xk; max.x = xn; }
        if (yn < yk) { min.y = yn; max.y = yk; }
        else { min.y = yk; max.y = yn; }
    }

    double sizeX() const { return (max.x - min.x); }
    double sizeY() const { return (max.y - min.y); }
};

class Geometry {
public:
    static const double pi;
    static const double pi2;
    static const double extent;

    static double accurateExtent(double value) {
        return ((value < -extent) ? -extent : (value > extent) ? extent : value);
    }
};

const double Geometry::pi = 3.14159265358979323846;
const double Geometry::pi2 = 6.28318530717958647693;
const double Geometry::extent = 1E6;

class Primitive {
private:
    bool visible;
    unsigned char color;
public:
    int getColor() const { return int(color); }
    void setColor(int tint) { color = (tint < 0) ? 0 : (tint > 255) ? 255 : static_cast<unsigned char>(tint); }
    bool isVisible() const { return visible; }
    void setShow() { visible = true; }
    void setHide() { visible = false; }
    Primitive() : visible(false), color(0) {}
    Primitive(const Primitive& obj) : visible(obj.visible), color(obj.color) {}
};

class Point : public Primitive, public Location {
public:
    Point() : Primitive(), Location() {}
    Point(const Point& obj) : Primitive(obj), Location(obj) {}
    Point(double xx, double yy, int tint) {
        setX(xx); setY(yy);
        setShow(); setColor(tint);
    }

    double getX() const { return x; }
    double getY() const { return y; }
    Location getPosition() const { return Location(x, y); }
    virtual void setX(double xx) { x = Geometry::accurateExtent(xx); }
    virtual void setY(double yy) { y = Geometry::accurateExtent(yy); }
    virtual Clip getClipBox() const { return Clip(x, y, x, y); }
};

class Figure : public Point {
private:
    double radius;
public:
    Figure() : Point(), radius(0) {}
    Figure(const Figure& obj) : Point(obj), radius(obj.radius) {}
    Figure(double xc, double yc, double rd, int tint) {
        setColor(tint); setShow();
        setRadius(rd); 
        setX(xc); setY(yc);
    }

    double getRadius() const { return radius; }
    void setRadius(double r) { radius = ((r < 0) ? -r : r); }
    double getLength() const { return radius * Geometry::pi2; }
    double getSquare() const { return radius * radius * Geometry::pi; }
    virtual void setX(double xx) { x = (((xx - radius) < -Geometry::extent) ? (-Geometry::extent + radius) : ((xx + radius) > +Geometry::extent) ? (+Geometry::extent - radius) : xx); }
    virtual void setY(double yy) { y = (((yy - radius) < -Geometry::extent) ? (-Geometry::extent + radius) : ((yy + radius) > +Geometry::extent) ? (+Geometry::extent - radius) : yy); }
    virtual Clip getClipBox() const { return Clip(x - radius, y - radius, x + radius, y + radius); }
};

void ErrorValue() {
    cin.clear(); cin.sync();
    cout << "Ошибка: некорректное значение" << endl;
}

void ModifyFigure(Figure& Fig) {
    char ch = 'P';
    do {
        switch (ch) {
        case 'P':
        case 'p':
            cout << endl << "Свойства фигуры:"
                << endl << "Центр = (" << Fig.getX() << ";" << Fig.getY() << ")"
                << endl << "Радиус = " << Fig.getRadius()
                << endl << "Площадь = " << Fig.getSquare()
                << endl << "Периметр = " << Fig.getLength()
                << endl << "Видимость = " << ((Fig.isVisible()) ? "On" : "Off")
                << endl << "Номер цвета = " << Fig.getColor()
                << endl;
            {
                Clip area = Fig.getClipBox();
                cout << "Область = (" << area.min.x << ";" << area.min.y
                    << ")--(" << area.max.x << ";" << area.max.y << ")" << endl
                    << "Размер = [" << area.sizeX() << "x" << area.sizeY() << "]"
                    << endl;
            }
            break;
        case 'X':
        case 'x':
            double value;
            cout << endl << "Введите X-координату:>";
            cin >> value;
            if (!cin.fail()) Fig.setX(value);
            else ErrorValue();
            break;
        case 'Y':
        case 'y':
            cout << endl << "Введите Y-координату:>";
            cin >> value;
            if (!cin.fail()) Fig.setY(value);
            else ErrorValue();
            break;
        case 'R':
        case 'r':
            cout << endl << "Введите радиус [R > 0]:>";
            cin >> value;
            if (!cin.fail()) Fig.setRadius(value);
            else ErrorValue();
            break;
        case 'T':
        case 't':
            int tint;
            cout << endl << "Введите цвет [0..255]:>";
            cin >> tint;
            if (!cin.fail()) Fig.setColor(tint);
            else ErrorValue();
            break;
        case 'V':
        case 'v':
            cout << endl << "Видимость [N-on|F-off]:>";
            cin >> ch;
            if (ch == 'N' || ch == 'n') Fig.setShow();
            else if (ch == 'F' || ch == 'f') Fig.setHide();
            else ErrorValue();
            break;
        default: cout << "Ошибка: некорректная операция" << endl;
        }

        cout << endl << "(T) Изменить цвет"
            << endl << "(R) Изменить радиус"
            << endl << "(V) Изменить видимость"
            << endl << "(X) Изменить X-координату"
            << endl << "(Y) Изменить Y-координату"
            << endl << "(P) Печатать все свойства"
            << endl << "(Q) Выход";
        cout << endl << "Выберите пункт:>";
        cin >> ch;
    } while (ch != 'Q' && ch != 'q');
}

int main() {
    setlocale(LC_ALL, "Russian");
    cout << "Работа 3" << endl;
    Figure fig(1, 1, 1, 255);
    ModifyFigure(fig); 
    return 0;
}
