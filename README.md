## Проект YaMDb

### Описание:
Проект YaMDb собирает отзывы пользователей на произведения, если подробнее:
```
 - Писать отзыв к произведениям
 - Выставлять оценки произведениям
 - Находить интеоесующие произведения
 - Искать произведения по категориям и жанрам
 ```

### Технологии:
При реализации проекта были использованы следующие основные технологии, фреймворки и библиотеки:

```
Python 3.8
Django 2.2.16
Django Rest FrameWork 3.12.4
REST API
```
___

### Как запустить проект:

<details>
  <summary markdown="span">Нажми, чтобы увидеть инструкцию</summary>
 
 -------

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:naelsa/api_yamdb.git
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

</details>

_____

<details>
  <summary markdown="span">Api-документация</summary>
 
 ------

```
http://127.0.0.1:8000/redoc/
 
```

  
</details>


### Авторы:
- [Хасбутдинов Наил](https://github.com/naelsa)
- [Дмитрий Петухов](https://github.com/Dmitry-russ)
- [Константин Тетерин](https://github.com/E9401)