## Установка и запуск
- скачать проект и перейти в директорию проекта
```
$ git clone https://github.com/marsvillan/E1.12-homework-sf
$ cd E1.12-homework-sf
```
- запустить игру
```
$ python game.py
```

## Запуск тестов вручную
- создать виртуальное окружение
```
$ python -m venv env
```
- применить виртуальное окружение
```
### Если у вас Linux:
$ source env/bin/activate
### Если у вас Windows:
$ env\Scripts\activate.bat
```
- установить зависимости
```
$ pip install -r requirements.txt
```
- запустить тесты
```
$ pytest
$ pytest --cov=game
```
