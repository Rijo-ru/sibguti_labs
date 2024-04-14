import scapy.all as scapy

def sniff_packets(interface):
    # Функция-обработчик, вызываемая при получении каждого пакета
    def packet_callback(packet):
        # Выводим содержимое пакета
        print(packet.show())
        print('wait message')

    # Запускаем сниффер на указанном интерфейсе, передавая обработчик
    scapy.sniff(iface=interface, store=False, prn=packet_callback)

# Запускаем сниффер на интерфейсе "eth0"
sniff_packets("lo")
