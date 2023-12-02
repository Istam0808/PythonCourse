# We create an input application using input() function in python and use postgresql to store the data.

<!-- =========================================================== -->
<!-- =========================================================== -->
<!-- =========================================================== -->
<!-- =========================================================== -->

## The application is as follows:
1. **Create psql db to connect (at least 2 more)**
RU: *Создать psql db для подключения (как минимум 2)*
UZ: `Ulanish uchun psql db yaratish (kamida 2 ta)`

2. **Ask from user to which db to connect**
RU: *Спросить у пользователя к какой db подключиться*
UZ: `Foydalanuvchidan qaysi db ga ulanishini so'rang`

3. **Create class User to hold all user related methods and info**
RU: *Создать класс для хранения всех методов и информации о пользователе*
UZ: `Foydalanuvchi bilan bog'liq metodlarni va ma'lumotlarni saqlash `
    `uchun klass yaratish`

4. **Create 2 function to register and login into account (separate from Class)**
RU: *Создать 2 функции для регистрации и входа в аккаунт (Отдельно от Class-а)*
UZ: `Ro'yxatdan o'tish va hisobga kirish uchun 2 ta funksiya yaratish (Class dan ajratilgan holda)`

5. **Each time, for new user, create new instance of class and store**
   **it in psql db**
RU: *Каждый раз, для нового пользователя, создавать новый экземпляр* 
    *класса и хранить его в psql db*
UZ: `Har bir yangi foydalanuvchi uchun klassning yangi misolini yaratib,` 
    `uni psql db da saqlang`

6. **Class should have 5 informations about user:**
   **- first_name - last_name - email - password - record_points**
RU: *Класс должен иметь 5 информаций о пользователе:*
   *- имя - фамилия - почта - пароль - рекорд очков*
UZ: `Klass foydalanuvchi haqida 5 ta ma'lumotlarni saqlash kerak:`
   `- ism - familiya - email - parol - rekord baho`

7. **Create 4 methods for class:**
   **- get_my_points - get my points from db**
   **- update_my_points - update my points in db (called if new record)**
   **- start_game - start game**
   **- end_game - e
   nd game**
RU: *Создать 4 метода для класса:*
    *- get_my_points - получить мои очки из db*
    *- update_my_points - обновить мои очки в db (вызывается если новый рекорд)*
    *- start_game - начать игру*
    *- end_game - закончить игру*
UZ: `Klass uchun 4 ta metod yaratish:`
    `- get_my_points - db dan o'z bahoimni olish`
    `- update_my_points - db da o'z bahoimni yangilash (yangi rekord bo'lsa)`
    `- start_game - o'yinni boshlash`
    `- end_game - o'yinni tugatish`

8. **Create number guessing game:**
  **- user should guess number from 1 to 100**
  **- user should have 6 attempts**
  **- each time for incorrect answer, user should be notified**
    **and number of attempts should be decreased and shown to the user**
  **- if user guessed the number, he should be notified and**
    **his record should be updated if he has less attempts than before**
RU: *Создать игру угадывания чисел:*
    *- пользователь должен угадать число от 1 до 100*
    *- пользователь должен иметь 6 попыток*
    *- каждый раз при неправильном ответе, пользователь должен быть уведомлен*
        *и количество попыток должно быть уменьшено и показано пользователю*
    *- если пользователь угадал число, он должен быть уведомлен и*
        *его рекорд должен быть обновлен, если у него меньше попыток, чем раньше*
UZ: `Sonni topish o'yini yaratish:`
    `- foydalanuvchi 1 dan 100 gacha bo'lgan sonni topishga harakat qilishi kerak`
    `- foydalanuvchining 6 ta urinishi bo'lishi kerak`
    `- har bir noto'g'ri javob uchun foydalanuvchi xabardor qilinishi kerak`
        `va urinishlar soni kamayishi va foydalanuvchiga ko'rsatilishi kerak`
    `- foydalanuvchi sonni topgan bo'lsa, u xabardor qilinishi kerak va`
        `agar avvalgi urinishlar sonidan kam bo'lsa, uning rekordi yangilanishi kerak`

9. **Every user related info should be stored in psql db**
RU: *Вся информация о пользователе должна храниться в psql db*
UZ: `Foydalanuvchi haqida ma'lumotlar psql db da saqlanishi kerak`


<!-- =========================================================== -->
<!-- =========================================================== -->
<!-- =========================================================== -->
<!-- =========================================================== -->

> When Terminal starts it shows options of databases and asks the user to select one of them.
```python
# Get all available databases from postgresql
**import** psycopg2

conn = psycopg2.connect(host="localhost", database="postgres",
                        user="postgres", password="...")

cur = conn.cursor()
cur.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
databases = cur.fetchall()
print("Available databases:")
for i in range(len(databases)):
    print(f"{i+1}. {databases[i][0]}")

db = input("Enter the database you want to use: ")
print(f"Using database - {db.upper()}")

# or
# To add new database
# cur.execute("CREATE DATABASE <database_name>")
# # To delete database
# cur.execute("DROP DATABASE <database_name>")
```

> After selecting the database you have to connect to db.
> We use psycopg2 library to connect to postgresql database.
```python
import psycopg2

def connect_db(db:str, user:str, password:str, host:str, port:str):
    # ...  Your code here
    return conn


conn = connect_db(db, user, password, host, port)
conn.autocommit = True
cur = conn.cursor()
```

> After connecting to db we have to ask to register or login.
> Based on the answer we call the respective function (login() or register()).
```python
print("1. Register")
print("2. Login")
answer = input("Enter your choice (1) or (2): ")
if answer == "1":
    register() 
    # Remember to use login function after registering a new user
elif answer == "2":
    login()
else:
    print("Invalid choice")
```

> register() =>  should use a class named User to store the data of user.
> - 1. Create a class instance and store the data in it.
> - 2. Insert the data into the table.
```python
```