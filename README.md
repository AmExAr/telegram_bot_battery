# Для чего это нужно?
Этот репозиторий нужен для отслеживания статуса баттареи ноутбука, который вы можете использовать как сервер, передавая нужную информацию через вашего личного Telegram бота.


# Какие виды статуса можно получить?
- Работа от сети
- Зарядка
- Работа от баттареи


# Конфидециальность
Данные о состоянии вашей баттареи передаётся вам и только вам, или же вы можете задать в файле ***config*** кому надо вместо вас.


# Установка и запуск
1. Скачать репозиторий
2. Установить зависимости из файла ***requirements.txt***
   ```
   pip install -r requirements.txt
   ```
3. В файле ***config***:
    1. В первой строке прописать *api_token*, полученный от официального Telegram бота *[BotFather](https://t.me/BotFather)*
    2. Во второй строке прописать ваш id как админа. Его можно получить в этом *[боте](https://t.me/my_id_bot)*
4. Запустить файл main.py команндой:
    ```
    python main.py
    ```
5. *Profit!!!*
## Пример файла ***config***:
```
999999999:FFFFFFFFFFFFFFFFFFFFFF
11111111
```