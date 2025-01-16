class RegistrationPageLocators:
    # Строка ввода имени
    name = "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input"
    # Строка ввода почты
    email = "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input"
    # Строка ввода пароля
    password = "//*[@id='root']/div/main/div/form/fieldset[3]/div/div/input"
    # Кнопка зарегистрироваться
    register = "//*[@id='root']/div/main/div/form/button"
    # Текст попапа о неверном пароле CSS
    wrong_password = ".input__error.text_type_main-default"
    # Кнопка входа (class)
    login_button = "Auth_link__1fOlj"


class LoginPageLocators:
    # кнопка войти
    login = ".//button[text()='Войти']"
    # поле имя
    name_field = "name"
    # поле пароль
    password_field = "Пароль"


class MainPageLocators:
    # Кнопка войти в аккаунт
    enter_account = ".button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg"
    # Кнопка личный кабинет
    user_account = ".//p[text()='Личный Кабинет']"
    # Кнопка булочки
    pans_button = ".//span[text()='Булки']"
    # Кнопка соусы
    sauces_button = ".//span[text()='Соусы']"
    # Кнопка начинки
    insides_button = ".//span[text()='Начинки']"


class PasswordRestorePageLocators:
    # кнопка войти
    login = ".//a[text()='Войти']"


class UserAccountPageLocators:
    # Кнопка сохранить
    save_button = ".//button[text()='Сохранить']"
    # Кнопка конструктор
    constructor = ".//p[text()='Конструктор']"
    # Кнопка выход
    exit_button = ".//button[text()='Выход']"