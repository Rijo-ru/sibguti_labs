#include <QApplication>
#include <QWidget>
#include <QVBoxLayout>
#include <QTextEdit>
#include <QLabel>
#include <QPushButton>
#include <QProcess>
#include <QComboBox>
#include <QLineEdit>
#include <QNetworkInterface>

class PacketSniffer : public QWidget
{
    Q_OBJECT

public:
    PacketSniffer(QWidget *parent = nullptr) : QWidget(parent)
    {
        QVBoxLayout *layout = new QVBoxLayout(this);
        QLabel *label = new QLabel("Packet Sniffer", this);
        layout->addWidget(label);

        textEdit = new QTextEdit(this);
        layout->addWidget(textEdit);

        interfaceComboBox = new QComboBox(this);
        layout->addWidget(interfaceComboBox);
        populateInterfaceList();

        portLineEdit = new QLineEdit(this);
        layout->addWidget(portLineEdit);
        portLineEdit->setPlaceholderText("Port (e.g., 80)");

        QPushButton *startButton = new QPushButton("Start", this);
        layout->addWidget(startButton);

        connect(startButton, &QPushButton::clicked, this, &PacketSniffer::startSniffing);
    }

private slots:
    void startSniffing()
    {
        QString interface = interfaceComboBox->currentText();
        QString port = portLineEdit->text();
        QStringList arguments;

        arguments << "-i" << interface;

        if (!port.isEmpty())
            arguments << "port" << port;

        process = new QProcess(this);
        process->start("sudo", QStringList() << "tcpdump" << arguments);
        connect(process, &QProcess::readyReadStandardOutput, this, &PacketSniffer::readOutput);
    }

    void readOutput()
    {
        if (process)
        {
            QByteArray output = process->readAllStandardOutput();
            textEdit->append(QString::fromUtf8(output));
        }
    }

private:
    QTextEdit *textEdit;
    QProcess *process = nullptr;
    QComboBox *interfaceComboBox;
    QLineEdit *portLineEdit;

    void populateInterfaceList()
    {
        QList<QNetworkInterface> interfaces = QNetworkInterface::allInterfaces();
        for (const QNetworkInterface &interface : interfaces)
        {
            if (interface.isValid() && interface.flags().testFlag(QNetworkInterface::IsUp))
                interfaceComboBox->addItem(interface.humanReadableName());
        }
    }
};

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    PacketSniffer sniffer;
    sniffer.show();
    return app.exec();
}

#include "main.moc"

