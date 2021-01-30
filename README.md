# stepik-auto_tests-final_project
Stepik Course: "Test automation with Selenium and Python", Final project.

Привет!
Спасибо, что заглянул в мой репозиторий!

Что нужно знать о моих автотестах:
- При разработке автотестов я использовал Python v3.9.0.
- В файлах в качестве отступов используется табуляция, а не пробелы.
- Тесты запускались на ОС Windows 10 через Anaconda Prompt с использованием Google Chrome v88.
- Если в консоле при выполнении автотестов появляются ошибки вида "DevTools listening on ... Getting Default Adapter failed" и они мешают просмотру лога, можно добавить следующую строку в файл conftest.py:
options.add_experimental_option("excludeSwitches", ["enable-logging"])
(расположить строку под номером 22 после добавления функции языков). После этого ошибки не будут отображаться.
