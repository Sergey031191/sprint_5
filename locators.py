class RegistrationPageLocators:
    # Строка ввода имени
    NAME_INPUT = "(.//input[@name='name'])[1]"
    # Строка ввода почты
    EMAIL_INPUT = "(.//input[@name='name'])[2]"
    # Строка ввода пароля
    PASSWORD_INPUT = ".//input[@name='Пароль']"
    # Кнопка зарегистрироваться
    REGISTER_BUTTON = ".//button[text()='Зарегистрироваться']"
    # Текст попапа о неверном пароле CSS
    WRONG_PASSWORD_POPUP = ".input__error.text_type_main-default"
    # Кнопка входа (class)
    LOGIN_BUTTON = "Auth_link__1fOlj"


class LoginPageLocators:
    # кнопка войти
    LOGIN_BUTTON = ".//button[text()='Войти']"
    # поле имя
    NAME_FIELD = "name"
    # поле пароль
    PASSWORD_FIELD = "Пароль"


class MainPageLocators:
    # Кнопка войти в аккаунт
    ENTER_ACCOUNT_BUTTON = ".button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg"
    # Кнопка личный кабинет
    USER_ACCOUNT_BUTTON = ".//p[text()='Личный Кабинет']"
    # Кнопка булочки
    PANS_BUTTON = ".//span[text()='Булки']"
    # Кнопка соусы
    SAUCES_BUTTON = ".//span[text()='Соусы']"
    # Кнопка начинки
    INSIDES_BUTTON = ".//span[text()='Начинки']"
    # Раздел булки
    SECTION_PANS = ".//div[span[text()='Булки']]"
    # Раздел соусы
    SECTION_SAUCE = ".//div[span[text()='Соусы']]"
    # Раздел начинки
    SECTION_INSIDES = ".//div[span[text()='Начинки']]"


class PasswordRestorePageLocators:
    # кнопка войти
    LOGIN_BUTTON = ".//a[text()='Войти']"


class UserAccountPageLocators:
    # Кнопка сохранить
    SAVE_BUTTON = ".//button[text()='Сохранить']"
    # Кнопка конструктор
    CONSTRUCTOR = ".//p[text()='Конструктор']"
    # Кнопка выход
    EXIT_BUTTON = ".//button[text()='Выход']"
