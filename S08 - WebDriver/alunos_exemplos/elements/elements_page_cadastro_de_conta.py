from selenium.webdriver.common.by import By

class CadastrarContaElements():

    NOME = (By.NAME, "firstname")
    LASTNAME = (By.NAME, "lastname")
    EMAIL = (By.NAME, "reg_email__")
    EMAIL_CONFIRM = (By.NAME, "reg_email_confirmation__")
    PASS = (By.NAME, "reg_passwd__")
    SEXO = (By.CSS_SELECTOR, "#reg_form_box label")
    DIA = (By.NAME, "birthday_day")
    MES = (By.NAME, "birthday_month")
    ANO = (By.NAME, "birthday_year")
    SUBMIT = (By.CSS_SELECTOR, "button[type=submit]")
