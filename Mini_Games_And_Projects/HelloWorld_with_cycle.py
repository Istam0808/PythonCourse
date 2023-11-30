import time

def printCharacter(text = "Hello World", interval = 100):
    alp = "1234567890!@#$%^&*()_+-=QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnmАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя "
    i = 0
    result = ""
    while True:
        print(result + alp[i])
        if alp[i] == text[len(result)]:
            result += alp[i]
        i += 1
        if i == len(alp):
            i = 0
        if len(result) == len(text):
            break
        time.sleep(interval / 500)

printCharacter("Istam", 10)