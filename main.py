
import random

print("Что хотите сделать?")
print("1 - Регистрация и авторизация")
print("2 - Добавить проект (категории, теги, клиент)")
print("3 - Управление статусом проекта")

choice = input("Введите номер (1/2/3): ")

if choice == "1":
    email = input("Email: ")
    password = input("Пароль (мин. 8 символов, нач. с буквы): ")
    password_repeat = input("Повторите пароль: ")
    name = input("Имя: ")
    role = input("Роль (дизайнер/заказчик): ")

    has_at = "@" in email
    has_dot = "." in email
    has_space = " " in email
    at_index = email.find("@")
    dot_index = email.find(".")
    valid_email = has_at and has_dot and not has_space and at_index > 0 and dot_index > at_index

    valid_length = len(password) >= 8
    valid_start = password[0].isalpha() if len(password) > 0 else False
    valid_match = password == password_repeat

    valid_name = len(name.strip()) >= 2
    valid_role = role.lower() == "дизайнер" or role.lower() == "заказчик"

    if not valid_email:
        print("Ошибка: некорректный email")
    elif not valid_length:
        print("Ошибка: пароль короче 8 символов")
    elif not valid_start:
        print("Ошибка: пароль должен начинаться с буквы")
    elif not valid_match:
        print("Ошибка: пароли не совпадают")
    elif not valid_name:
        print("Ошибка: имя слишком короткое")
    elif not valid_role:
        print("Ошибка: роль должна быть 'дизайнер' или 'заказчик'")
    else:
        login = email.split("@")[0].lower()
        print("регистрация прошла успешно")
        print(f"Логин: {login}")
        print(f"Имя:   {name}")
        print(f"Роль:  {role}")

      
        print("авторизация")

        login_try = input("Логин: ").lower()
        password_try = input("Пароль: ")

        if login_try != login:
            print("Пользователь с таким логином не найден")
        elif password_try != password:
            print("Неверный пароль")
        else:
            print(f"Добро пожаловать, {name}!")
            print("Доступ к портфолио открыт.")
        pass
elif choice == "2":
    print("добавление проекта:категории и теги")
    
    title = input("Название проекта: ")
    category = input("Категория (логотип/сайт/баннер/брендинг): ").lower().strip()
    tags = input("Теги через запятую: ").lower().replace(" ", "")
    client = input("Клиент: ").strip()
    client_type = input("Тип клиента (новый/постоянный): ").lower().strip()


    valid_category = (
        category == "логотип"
        or category == "сайт"
        or category == "баннер"
        or category == "брендинг"
    )
    if category == "логотип":
        auto_tags = "branding,identity,vector"
    elif category == "сайт":
        auto_tags = "web,ui,ux"
    elif category == "баннер":
        auto_tags = "ads,banner,marketing"
    elif category == "брендинг":
        auto_tags = "brand,strategy,guideline"
    else:
        auto_tags = "design,creative"

    has_duplicate = category in tags

    final_tags = tags + "," + auto_tags

    valid_client = len(client) >= 2



    project_id = random.randint(10000, 99999)

    if not valid_category:
        print(f"Неизвестная категория: {category}")
    elif not valid_client:
        print("Имя клиента слишком короткое")
    else:
        
        print("карточка проекта")
       
        print(f"ID проекта:   P-{project_id}")
        print(f"Название:     {title}")
        print(f"Категория:    {category}")
        print(f"Теги:         {final_tags}")
        print(f"Дубль тега?   {'да' if has_duplicate else 'нет'}")
    pass
elif choice == "3":
    
    print("управление статусом проекта")
  
    title = input("Название проекта: ")
    current_status = input("Текущий статус (черновик/опубликовано/архив): ").lower().strip()
    action = input("Действие (опубликовать/в архив/вернуть в черновик): ").lower().strip()
    is_complete = input("Работа завершена? (да/нет): ").lower() == "да"
    has_cover = input("Есть обложка? (да/нет): ").lower() == "да"

  
    if current_status == "черновик":
        if action == "опубликовать":
            if not is_complete:
                new_status = "черновик"
                message = "Нельзя опубликовать незавершённую работу"
            elif not has_cover:
                new_status = "черновик"
                message = "Нельзя опубликовать проект без обложки"
            else:
                new_status = "опубликовано"
                message = "Проект опубликован в портфолио"
        elif action == "в архив":
            new_status = "архив"
            message = " Черновик перемещён в архив"
        else:
            new_status = "черновик"
            message = "Статус не изменён"

    elif current_status == "опубликовано":
        if action == "в архив":
            new_status = "архив"
            message = "Проект убран из публичного портфолио"
        elif action == "вернуть в черновик":
            new_status = "черновик"
            message = " Проект возвращён в черновики"
        else:
            new_status = "опубликовано"
            message = "ℹ Статус не изменён"

    elif current_status == "архив":
        if action == "вернуть в черновик":
            new_status = "черновик"
            message = "Проект восстановлен из архива"
        elif action == "опубликовать" and is_complete and has_cover:
            new_status = "опубликовано"
            message = " Проект восстановлен и опубликован"
        else:
            new_status = "архив"
            message = " Из архива можно только восстановить в черновик или опубликовать завершённый проект"

    else:
        new_status = "неизвестно"
        message = " Неизвестный статус"

    print("результат")
 
    print(f"Проект:         {title}")
    print(f"Было:           {current_status}")
    print(f"Действие:       {action}")
    print(f"Стало:          {new_status}")
    print(f"Сообщение:      {message}")
   
else:
    print(" Неизвестный выбор")