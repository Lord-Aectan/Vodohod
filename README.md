# Пример проекта автотестов для компании ВодоходЪ
> ВодоходЪ - крупнейшая круизная компания и туристический 
> оператор России. Входит в тройку крупнейших компаний
> российского рынка речных круизов,
> на 2018 год охватывавших 80 % пассажиропотока.
> По результатам исследования, проведённого изданием
> Cruise Market Report в 2020 году, компания «Водоходъ»
> занимает первое место в России с 33,8 % долей рынка
> и третье — в Европе. 

### Используемые технологии
<p  align="center">
  <code><img width="5%" title="Pycharm" src="images/logo/pycharm.png"></code>
  <code><img width="5%" title="Python" src="images/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="images/logo/selene.png"></code>
  <code><img width="5%" title="Selenium" src="images/logo/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="images/logo/github.png"></code>
  <code><img width="5%" title="Jenkins" src="images/logo/jenkins.png"></code>
  <code><img width="5%" title="Selenoid" src="images/logo/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="images/logo/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="images/logo/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="images/logo/jira.png"></code>
  <code><img width="5%" title="Telegram" src="images/logo/tg.png"></code>
</p>

## Покрываемый функционал
### UI
- Авторизация в десктопной и мобильной версии браузера
- Авторизация в интерфейсе бронирования booking
- Доступность интерфейса «Таблица цен» для не авторизованных пользователей
- Наличие схемы теплохода у теплохода люксовой категории

### API
- Регистрация и получение токена
- При запросе существующего круиза по нему возвращается информация
- Если круиза не существует, то возвращается 'Круиз не найден'

## Запуск тестов
#### Все UI тесты запускаются удалённо на Selenoid

### Локально
1. Склонируйте репозиторий
2. Откройте проект в PyCharm
3. Введите в териминале команду
``` 
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest .
```

### Запуск тестов в [Jenkins](https://jenkins.autotests.cloud/job/005-MoiseenkoDaniil_DiplomaProject/)
Нажмите кнопку «Собрать сейчас»
<p><img src="images/screenschot/jenkins_job.png"></p>

### <img width="3%" title="Allure Report" src="images/logo/allure_report.png"> Отчетность о прохождении тестов в Allure
#### Если тест запускался локально:
Введите в терминале команду 
```
allure serve allure-results
``` 
#### Если тест запускался в Jenkins
Нажмите Allure Report или кликните по иконке отчёта в завершённой сборке
<p><img title="Jenkins_Allure" src="images/screenschot/jenkins_allure.png"></p>

### Примеры отображения тестов
<img title="Allure_Report" src="images/screenschot/Allure Report.png">
<img title="Allure_Example_Report" src="images/screenschot/allure_example_report_01.png">

#### Так же в отчетах для каждого UI-теста прикрепляется видео
<img src="images/screenschot/video_test_allure.gif">

### Проект интегрирован с Allure TestOps и Jira
<img title="Allure_TestOps" src="images/screenschot/allure_testops.png">
<img title="Jira" src="images/screenschot/Jira.png">