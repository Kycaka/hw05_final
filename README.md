# hw05_final - Проект спринта: подписки на авторов, спринт 6 в Яндекс.Практикум

## Спринт 6 - Проект спринта: подписки на авторов

### hw05_final - Проект спринта: подписки на авторов, Яндекс.Практикум.

Покрытие тестами проекта Yatube из спринта 6 Питон-разработчика бекенда Яндекс.Практикум. Все что нужно, это покрыть тестами проект, в учебных целях. Реализована система подписок/отписок на авторов постов.

### **ЗАМЕЧАНИЕ**:
* Не работает статика должным образом, пофиксить, переходом на Django 3 или 4

Стек:

- Python 3.10.5
- Django==2.2.28
- mixer==7.1.2
- Pillow==9.0.1
- pytest==6.2.4
- pytest-django==4.4.0
- pytest-pythonpath==0.7.3
- requests==2.26.0
- six==1.16.0
- sorl-thumbnail==12.7.0
- Pillow==9.0.1
- django-environ==0.8.1

### Настройка и запуск на ПК

Клонируем проект:

```bash
git clone https://github.com/Kycaka/hw05_final.git
```

или

```bash
git clone git@github.com:Kycaka/hw05_final.git
```

Переходим в папку с проектом:

```bash
cd hw05_final
```

Устанавливаем виртуальное окружение:

```bash
python -m venv venv
```

Активируем виртуальное окружение:

```bash
source venv/Scripts/activate
```

> Для деактивации виртуального окружения выполним (после работы):
> ```bash
> deactivate
> ```

Устанавливаем зависимости:

```bash
python -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Применяем миграции:

```bash
python yatube/manage.py makemigrations
python yatube/manage.py migrate
```

Создаем супер пользователя:

```bash
python yatube/manage.py createsuperuser
```
