# Лабораторная работа №1. Реализация удаленного импорта собственного пакета
### 1. Создадим файл myremo  temodule.py, который будет импортироваться, разместим его в каталоге, который далее будет "корнем сервера", и назовем его rootserver. Напишем код.
![step1](https://github.com/elyakkos/prog5-lr1/blob/main/step1)
### 2. Создадим файл Python с содержимым функций url_hook и классов URLLoader, URLFinder из текста конспекта лекции со всеми необходимыми библиотеками и назовем: activation_script.py.
![step2](https://github.com/elyakkos/prog5-lr1/blob/main/step2.png)
![step3](https://github.com/elyakkos/prog5-lr1/blob/main/step3.png)
### 3. Далее, чтобы продемонстрировать работу импорта из удаленного каталога, запустим сервер http так, чтобы наш желаемый для импорта модуль "лежал" на сервере (например, в корневой директории сервера). Откроем каталог rootserver с файлом myremotemodule.py и запустим там сервер:
![step4](https://github.com/elyakkos/prog5-lr1/blob/main/step4.png)
### 4. После этого мы запустили файл, в котором содержится код. python3 -i activation_script.py. Выполнили код: sys.path.append("http://localhost:8000")
![step5](https://github.com/elyakkos/prog5-lr1/blob/main/step5.png)
![step6](https://github.com/elyakkos/prog5-lr1/blob/main/step6.png)

### Задание *.
### Добавим в вывод обработчик, который будет ловить исключения
![step7](https://github.com/elyakkos/prog5-lr1/blob/main/step7.png)

### Ссылка на код: 
[Посмотреть код](https://github.com/elyakkos/prog5-lr1/tree/main/lr1-code)





