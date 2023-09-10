import psutil


def get_battery_status():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent
    if plugged and battery.percent == 100:
        return 'Сервер работает от сети'
    elif plugged and battery.percent < 100:
        return f'Сервер заряжается. Текущий заряд: {battery.percent}%'
    elif not plugged:
        return f'Сервер работает от батареи. Текущий заряд: {battery.percent}%'

if __name__ == '__main__':
    print(get_battery_status())
