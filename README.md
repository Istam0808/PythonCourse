# Python
 Hi i'm learning Python, I created this repository for learning Python


# ISTAM
      ___ ___ ___  __   _   _  
       |  \__  |  |__| | \ / |  
      _|_  __| |  |  | |  |  | 
                                                                                   

<h1>TABLE OF CONTENTS</h1>

- [Exercises](#exercises)
- [Semantic versioning:](#semantic-versioning)
- [Install pipenv](#install-pipenv)
- [To create requirements.txt file](#to-create-requirementstxt-file)
- [Modules](#modules)
  - [random](#random)
  - [math](#math)
  - [time / datetime / timedelta](#time--datetime--timedelta)
  - [json](#json)
  - [logging](#logging)
  - [requests](#requests)
  - [faker](#faker)
  - [translators](#translators)
  - [re](#re)
  - [collections](#collections)


# Exercises
🎯 Here are some resources to help you get started with Python and exercise 💪👇️
1. Practice Python (https://www.practicepython.org/)
2. HackerRank (https://www.hackerrank.com/domains/python)
3. Project Euler (https://projecteuler.net/archives)
4. Codewars (https://www.codewars.com/kata/search/python)


# Semantic versioning: 
https://semver.org/

> - ex: 3.11.0
> - 1. "3"  => Patch version
> -         (Bug fixes) (Big changes that affect everything inside our project)
> - 2. "11" => Major version
> -         (Major changes that affect something inside our project)
> - 3. "0"  => Minor version
> -         (Changes that don't affect anything inside our project)



# Install pipenv
1. python -m pip uninstall virtualenv pipenv -y
2. py -m pip uninstall virtualenv pipenv -y
3. python3 -m pip uninstall virtualenv pipenv -y
4. python -m pip install --upgrade setuptools wheel
5. python -m pip install --user pipenv

- -- or -- 
```bash
python -m pip install pipenv
``` 

- If you however get 
```
    'pipenv' is not recognized as an internal or external command, operable program or batch file 
```

```md
get the Python>- path to the base directory for the user site-packages by running:
Mine is C:\Users\drgabrielharris\AppData\Roaming\Python\Python37\site-packages
Replace site-packages in the path with Scripts then add to your system PATH 
(on Windows: Edit environment variables for your account > in the User variables select 
Path > Edit > New > C:\Users\drgabrielharris\AppData\Roaming\Python\Python37\Scripts )
```


# To create requirements.txt file
1. ```pipenv lock -r > requirements.txt```  - is outdated
2. 🎯 New version is: ```pipenv run pip freeze  > requirements.txt``` 
___

# Modules
<span>
   <a  style="background:linear-gradient(to right, black, blue, black);  padding:10px;  border-radius:10px; color:snow;"
      href="https://codete.com/blog/10-built-in-modules-in-python-you-should-know#overview">
      **Codete**
   </a>
   - 10 Built-in Modules in Python You Should Know
   <br>
   <a  style="background:linear-gradient(to right, black, blue, black);  padding:10px;  border-radius:10px; margin-left:10px; color:snow;"
      href="https://levelup.gitconnected.com/11-most-useful-built-in-python-modules-you-might-not-know-yet-eff3e0e6f586">
      **Levelup**
   </a>
   - 11 Most Useful Built-in Python Modules You Might Not Know Yet
   <br>
   <br>
</span>

1. `random`      (https://docs.python.org/3/library/random.html)
2. `math` 
3. `time`        (https://docs.python.org/3/library/time.html)
   - datetime  (https://www.pythoncheatsheet.org/modules/datetime-module)
   - timedelta (https://www.pythoncheatsheet.org/modules/datetime-module)
4. `json`        (https://medium.com/analytics-vidhya/json-in-python-163857b00415)
5. `logging`     (https://majianglin2003.medium.com/python-logging-6a688fa63587)
6. `requests`    (https://medium.com/@stayml/python-requests-a-simple-visual-introduction-1c57a60a7c46)
7. `faker`       (https://andsilvadrcc.medium.com/how-to-generate-fake-data-using-the-faker-python-package-b6734b944cb2)
8. `translators` (https://pypi.org/project/translators/)
9. `re`          (https://docs.python.org/3/library/re.html)
10. `collections`  (https://medium.com/this-code/python-collections-the-in-depth-guide-to-those-special-data-structures-8f03d537f9d4)


## random
-  RU: Модуль random предоставляет доступ к функциям, которые поддерживают множество операций.
   Возможно, самое важное - это то, что он позволяет генерировать случайные числа.

1. `random.random()` : 
- Return the next random floating point number in the range [0.0, 1.0).
- RU: Возвращает следующее случайное число с плавающей запятой в диапазоне [0.0, 1.0).
2. `random.randint(a, b)` : 
- Return a random integer N such that a <= N <= b.
- RU: Возвращает случайное целое число N такое, что a <= N <= b.
- ex:
  ```python
   import random
   print(random.randint(0, 10))
  ```
3. `random.choice(seq)` : 
- Return a random element from the non-empty sequence seq. If seq is empty, raises IndexError.
- RU: Возвращает случайный элемент из непустой последовательности seq. Если seq пуст, возникает IndexError.
- ex:
  ```python
   import random
   x = [i for i in range(10)]
   print(x)
   print(random.choice(x))
  ```
4. `random.shuffle(x[, random])` : 
- Shuffle the sequence x in place.
- RU: Перемешивает последовательность x на месте.
- ex:
  ```python
   import random
   x = [[i] for i in range(10)]
   print(x)
   random.shuffle(x)
   print(x)
  ```

## math
- RU: Этот модуль предоставляет доступ к математическим функциям, определенным стандартом C.
(Стандартная библиотека C - это набор заголовочных файлов, которые определяют различные библиотечные функции и макросы.
Большинство функций стандартной библиотеки C также включены в стандартную библиотеку C ++, хотя и в разных заголовочных файлах.)

1. `math.ceil(x)` : 
- Return the ceiling of x as a float, the smallest integer value greater than or equal to x.
- RU: Возвращает потолок x в виде плавающего числа, наименьшее целое значение, большее или равное x.
2. `math.floor(x)` : 
- Return the floor of x as a float, the largest integer value less than or equal to x.
- RU: Возвращает пол x в виде плавающего числа, наибольшее целое значение, меньшее или равное x.
3. `math.trunc(x)` : 
- Return the Real value x truncated to an Integral (usually an integer). 
- RUL Возвращает действительное значение x, усеченное до целого (обычно целое число). 
4. `math.factorial(x)` : 
- Return x factorial as an integer. Raises ValueError if x is not integral or is negative.
- RU: Возвращает факториал x в виде целого числа. Выдает ValueError, если x не является целым или отрицательным.  
5. `math.gcd(a, b)` : 
- Return the greatest common divisor of the specified integer arguments. If any argument is nonzero, 
   then the absolute value of the greatest common divisor is smaller than or equal to the smallest absolute value of the arguments.
- RU: Возвращает наибольший общий делитель указанных целых аргументов. Если любой аргумент отличен от нуля, 
   то абсолютное значение наибольшего общего делителя меньше или равно наименьшему абсолютному значению аргументов.
ex:
```python
import math
print(math.gcd(10, 20))
```

6. `math.pow(x, y)` : 
- Return x raised to the power y. Exceptional cases follow Annex ‘F’ of the C99 standard as far as possible. 
   In particular, pow(1.0, x) and pow(x, 0.0) always return 1.0, even when x is a zero or a NaN. If both x and y are finite, 
   x is negative, and y is not an integer then pow(x, y) is undefined, and raises ValueError.
- RU: Возвращает x, возведенный в степень y. Исключительные случаи следуют Приложению «F» стандарта C99 насколько это возможно. 
   В частности, pow(1.0, x) и pow(x, 0.0) всегда возвращают 1.0, даже когда x является нулем или NaN. Если x и y конечны, 
   x отрицателен, а y не является целым числом, то pow(x, y) не определен и вызывает ValueError.
7. `math.sqrt(x)` : 
- Return the square root of x.
- RU: Возвращает квадратный корень из x.
8. `math.pi` : 
- The mathematical constant π = 3.141592…, to available precision.
- RU: Математическая константа π = 3.141592…, до доступной точности.

## time / datetime / timedelta

1. `time.time()`:
- Return the time in seconds since the epoch as a floating point number.
- RU: Возвращает время в секундах с начала эпохи в виде числа с плавающей запятой.
```python
import time
print(time.time())

print("tm_wday  =>", time_z.tm_wday)
print("tm_min  =>", time_z.tm_min)
print("tm_isdst  =>", time_z.tm_isdst)
print("tm_mday  =>", time_z.tm_mday)
print("tm_year  =>", time_z.tm_year)
print("tm_zone  =>", time_z.tm_zone)
```
2. `time.sleep(secs)`:
- Suspend execution of the calling thread for the given number of seconds. 
   The argument may be a floating point number to indicate a more precise sleep time. 
   The actual suspension time may be less than that requested because any caught signal will terminate the sleep() following execution of that signal’s catching routine. 
   Also, the suspension time may be longer than requested by an arbitrary amount because of the scheduling of other activity in the system.
- RU: Приостанавливает выполнение вызывающего потока на заданное количество секунд.
   Аргументом может быть число с плавающей запятой, чтобы указать более точное время сна.
   Фактическое время приостановки может быть меньше запрошенного, потому что любой перехваченный сигнал прерывает sleep() после выполнения процедуры перехвата этого сигнала.
   Кроме того, время приостановки может быть дольше запрошенного на произвольную величину из-за планирования другой активности в системе.
```python
time.sleep(1) # sleep for 1 second
```

3. `time.localtime([secs])`:
- Convert a time expressed in seconds since the epoch to a struct_time in time. 
   If secs is not provided or None, the current time as returned by time() is used. 
   Fractions of a second are ignored. 
   Note that since not all time functions handle leap seconds, this is not necessarily a precise inverse function to time().
- RU: Преобразует время, выраженное в секундах с начала эпохи, в struct_time в time.
   Если secs не предоставляется или None, используется текущее время, возвращаемое time().
   Доли секунды игнорируются.
   Обратите внимание, что поскольку не все функции времени обрабатывают високосные секунды, это не обязательно точная обратная функция к time().

```python
print(time.localtime(UNIX-time))
```

4. `time.strftime(format[, t])`:
- Convert a tuple or struct_time representing a time as returned by gmtime() or localtime() to a string as specified by the format argument. 
   If t is not provided, the current time as returned by localtime() is used. 
   format must be a string. 
- RU: Преобразует кортеж или struct_time, представляющий время, возвращаемое gmtime() или localtime(), в строку, указанную аргументом format.
   Если t не предоставляется, используется текущее время, возвращаемое localtime().
   Формат должен быть строкой.
```python
print(time.strftime("%y-%m-%d %H:%M:%S", time.localtime()))

1. %y  => is year in short version  =>  Годы в краткой версии
2. %Y  => is year in full version  =>  Годы в полной версии
3. %m  => is month in number =>  Месяцы в числовом формате
4. %M  => is minute in number =>  Минуты в числовом формате
5. %d  => is day in number =>  Дни в числовом формате
6. %D  => is Date (full date) =>  Дата (полная дата)
7. %h  => is month in short version =>  Месяцы в краткой версии
8. %H  => is hour in number =>  Часы в числовом формате
9. %s  => DOES NOT EXIST =>  НЕ СУЩЕСТВУЕТ
10. %S => is second in number =>  Секунды в числовом формате
```



5. `datetime.datetime.now()`:
- Return the current local date and time.
- RU: Возвращает текущую локальную дату и время.
```python
import datetime
print(datetime.datetime.now())
```

6. `datetime.datetime(year, month, day ...)`:
- The year, month and day arguments are required. tzinfo may be None, or an instance of a tzinfo subclass. 
   The remaining arguments may be ints, longs, or floats, and may be positive or negative.
- RU: Требуются аргументы год, месяц и день. tzinfo может быть None или экземпляром подкласса tzinfo.
   Оставшиеся аргументы могут быть целыми числами, длинными или плавающими, и могут быть положительными или отрицательными.
```python
print(datetime.datetime(2020, 5, 17, 12, 30, 0, 0))
```

7. `timedelta`
- EN: The timedelta class is used to represent the `difference` between two dates or times.
- RU: Класс timedelta используется для представления `разницы` между двумя датами или временем.
```python
import datetime
print(datetime.timedelta(days=365, hours=5, minutes=1))
```

- timedelta can add `days`, `seconds` and `microseconds` to a datetime object
- RU: timedelta может добавлять `дни`, `секунды` и `микросекунды` к объекту datetime
```python
import datetime
now = datetime.now()
print(now)
>>> datetime.datetime(2023, 7, 31, 12, 30, 10, 999999)

print(now + datetime.timedelta(days=365))
>>> datetime.datetime(*2024*, 7, 30, 12, 30, 10, 999999)
```

## json
```python
print(json.dumps({}))   # => "{}"  =>  JSON.stringify()
print(json.loads("{}"))  # =>  {}  =>  JSON.parse()
```

## logging
> - Logging is a means of tracking events that happen when some software runs.
> ex: errors that occur, warnings about resource utilization, or even just informational messages that are generated by an application.
> - RU: Журналирование - это способ отслеживания событий, которые происходят при запуске какого-либо программного обеспечения. 
> например: ошибки, возникающие, предупреждения о использовании ресурсов или даже просто информационные сообщения, генерируемые приложением.
> It has an ordered list of levels that indicate the severity of events.
> 1. DEBUG     => Detailed information, typically of interest only when diagnosing problems.
>              Подробная информация, как правило, интересна только при диагностике проблем.
> 2. INFO      => Confirmation that things are working as expected.
>              Подтверждение того, что все работает, как ожидалось. 
> 3. WARNING   => An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’).
>             Признак того, что что-то неожиданное произошло или указывающий на какую-то проблему в ближайшем будущем (например, «мало места на диске»).
> 4. ERROR     => Due to a more serious problem, the software has not been able to perform some function.
>             Из-за более серьезной проблемы программное обеспечение не смогло выполнить некоторую функцию.
> 5. CRITICAL  => A serious error, indicating that the program itself may be unable to continue running.
>            Серьезная ошибка, указывающая на то, что сама программа может быть не в состоянии продолжать работу.
> - By default, the logging module logs the messages with a severity level of WARNING or above.
> - RU: По умолчанию модуль регистрации регистрирует сообщения с уровнем серьезности WARNING или выше.

`CONFIGURATION`
- To configure the logging module, you must use the basicConfig() function.
ex: 
```python
import logging

WRITE_AND_APPEND = 'a+'
logging.basicConfig(
    level=logging.DEBUG,
    filename='app.log',
    filemode=WRITE_AND_APPEND,
    format='%(levelname)s - %(message)s - %(asctime)s'
)
# NOTE: RUN THIS ONLY ONE TIME !!!

logging.debug(f'This is warning message')
```
> - filename: Specifies that a file should be used to store the logs.
> - RU: filename: указывает, что для хранения журналов должен использоваться файл.
  
> - filemode: Specifies the mode to open the file, if filename is specified (if filemode is unspecified, it defaults to 'a').
> - RU: filemode: указывает режим открытия файла, если указано имя файла (если режим файла не указан, по умолчанию используется «a»).
  
> - format: Specifies the format of the log message.
> - RU: format: указывает формат сообщения журнала.
  
> - level: Specifies the lowest-severity log message a logger will handle, where debug is the lowest built-in severity level and critical is the highest built-in severity.
> -  RU: level: указывает самое низкое сообщение журнала, которое обработчик регистратора будет обрабатывать, где отладка является самым низким встроенным уровнем серьезности, а критический - самым высоким встроенным уровнем серьезности.
  
> - datefmt: Specifies the format of the date/time portion of a log message.
> -  RU: datefmt: указывает формат даты / времени части сообщения журнала.

## requests
This library is like axios in JS
```python
# In js we would do:
# axios.get('https://...')

# In python we do:
import requests
response = requests.get('https://...')

# To get the status code:
print(response.status_code)

# To get the content:
print(response.content)

# To get the json:
print(response.json())
```
## faker

This is a library that generates fake data
```python
from faker import Faker
fake = Faker()
print(fake.name())
print(fake.address())
print(fake.text())
print(fake.email())
print(fake.phone_number())
print(fake.country())
print(fake.url())
...
```
## translators

```python
import translators as ts
q_text = 'Какая погода сегодня?'
print(ts.translate_text(q_text))
```
## re

```python
# Source: https://regexr.com/

import re
re.findall(pattern, string)  # => It returns a list of all matching patterns.
re.search(pattern, string)   # => It returns first match's position
re.split(pattern, string)    # => Works like split() method of strings but can take RE as separator.
re.sub(pattern, repl, string, count=0, flags=re...)  
   # => It returns a new string with all matches of the pattern replaced by repl.
   1. pattern  =>  The regular expression pattern string.
   2. repl     =>  The replacement string.
   3. string   =>  The source string.
   4. count    =>  Maximum number of occurrences that will be replaced. 
                   If not specified or is 0, all occurrences will be replaced. 
   5. flags    =>  A combination of re flags.
re.compile(pattern, flags=0)  # => It returns a regular expression object.
   # ======= Username pattern =======
   # re.compile(r'@([A-Za-z0-9_]+)')
   # @  ->   indicates the start of the username
   # () ->   indicates the start and end of the username
   # [] ->   indicates the range of characters that can be used in the username
   # +  ->   indicates that the username must contain at least one character
   # A-Za-z0-9_ -> indicates the range of characters that can be used in the username
   # Ex: @username
   # Ex: @user_name
   # To test if it works, use the following code:
   # username = '@user_name'
   # print(re.search(r'@([A-Za-z0-9_]+)', username) != None)

# ============================================================
# ^ (Caret)    =>  It matches the start of the string.
string = "Hello World!"
x = re.findall("^Hello", string)
print(x)
# ============================================================
# $ (Dollar)   =>  It matches the end of the string.
string = "Hello World!"
x = re.findall("World!$", string)
print(x)
# ============================================================
# . (Dot)   =>  It matches any character except a newline.
string = "Hello World!"
x = re.findall("H.ll.", string)
print(x)
```
## collections
```python 
# collections
# 1. collections.deque
# ex:
queue = collections.deque()
queue.append(5)
queue.append("Mine")
queue.append(True)
# DIFFERENCES FROM LIST
queue.appendleft(10)
>>> print(queue)
queue.rotate(2)
>>> print(queue)
# ====================================================================
# ====================================================================
# 2. collections.Counter()
# ex:
arr = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3]
word = "Hello World"
lc = collections.Counter(arr)
wc = collections.Counter(word)
>>> print(lc)
>>> print(wc)
>>> print(lc.most_common(2))  # 2 most common elements
>>> print(wc.total())         # total number of elements (==  len(wc))
# ====================================================================
# ====================================================================
# 3. collections.defaultdict()
# ex:
d = collections.defaultdict(int)  =>  gives default value of 0 if the key is not present
d['a'] = 1
d['b'] = 2
>>> print(d['c'])  =>  is 0
```                                                                  

