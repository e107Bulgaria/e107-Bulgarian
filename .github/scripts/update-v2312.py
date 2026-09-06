#!/usr/bin/env python3
CORE_ADDITIONS = {'e107_languages/Bulgarian/Bulgarian.php': [('LAN_LOGOUT_REFUSED_TOKEN_MISSING',
                                                'Не сте излезли от профила си, защото тази връзка не съдържаше защитен токен. '
                                                'Използвайте връзката за изход от собственото меню на сайта, а не отметка или връзка от '
                                                'друг сайт.')],
 'e107_languages/Bulgarian/admin/lan_admin.php': [('ADLAN_REFUSED_TOKEN_MISSING',
                                                        'Заявката не беше изпълнена, защото не съдържаше защитен токен. Използвайте собствените '
                                                        'контроли на административното табло, а не отметка или връзка от друг сайт.')],
 'e107_languages/Bulgarian/admin/lan_db.php': [('DBLAN_REFUSED_TOKEN_MISSING',
                                                     'Операцията не беше стартирана, защото връзката не съдържаше защитен токен. Стартирайте я '
                                                     'от менюто „Инструменти за базата данни“, а не от отметка или връзка от друг сайт.')],
 'e107_languages/Bulgarian/admin/lan_e107_update.php': [('LAN_UPDATE_REFUSED_TOKEN_MISSING',
                                                               'Операцията не беше стартирана, защото връзката не съдържаше защитен токен. Стартирайте '
                                                               'системното обновяване от връзката, която e107 показва в администрацията, а не от отметка или '
                                                               'връзка от друг сайт.')],
 'e107_languages/Bulgarian/admin/lan_lancheck.php': [('LANG_LAN_REFUSED_TOKEN_MISSING',
                                                            'Проверката на езиковия пакет не беше стартирана, защото връзката не съдържаше защитен токен. '
                                                            'Стартирайте я от списъка с езикови пакети, а не от отметка или връзка от друг сайт.')],
 'e107_languages/Bulgarian/admin/lan_mailout.php': [('LAN_MAILOUT_REFUSED_TOKEN_MISSING',
                                                           'Операцията с имейл кампаниите не беше стартирана, защото връзката не съдържаше защитен токен. '
                                                           'Стартирайте я от менюто за имейл кампании, а не от отметка или връзка от друг сайт.')],
 'e107_languages/Bulgarian/admin/lan_menus.php': [('MENLAN_REFUSED_TOKEN_MISSING',
                                                        'Менюто не беше премахнато от оформлението, защото връзката не съдържаше защитен токен. '
                                                        'Премахнете го чрез Мениджъра на менюта, а не чрез отметка или връзка от друг сайт.')],
 'e107_languages/Bulgarian/admin/lan_plugin.php': [('EPL_ADLAN_REFUSED_PULL_TOKEN_MISSING',
                                                          'Плъгинът не беше обновен от Git хранилището си, защото връзката не съдържаше защитен токен. '
                                                          'Стартирайте обновяването от Мениджъра на плъгини, а не от отметка или връзка от друг сайт.'),
                                                         ('EPL_ADLAN_REFUSED_BUILD_TOKEN_MISSING',
                                                          'Не беше записан файл с дефиницията на таблицата, защото връзката не съдържаше защитен токен. '
                                                          'Стартирайте генератора на плъгини от менюто „Плъгини“, а не от отметка или връзка от друг '
                                                          'сайт.')],
 'e107_languages/Bulgarian/admin/lan_theme.php': [('LAN_THEME_OPTIONS_NOT_SAVED', 'Настройките на темата не бяха записани.'),
                                                        ('TPVLAN_REFUSED_TOKEN_MISSING',
                                                         'Темата не беше копирана, защото връзката не съдържаше защитен токен. Стартирайте създаването '
                                                         'от формуляра в Управление на теми, а не от отметка или връзка от друг сайт.')],
 'e107_languages/Bulgarian/admin/lan_users.php': [('USRLAN_REFUSED_TOKEN_MISSING',
                                                        'Действието не беше изпълнено, защото връзката не съдържаше защитен токен. Стартирайте го от '
                                                        'списъка с потребители, а не от отметка или връзка от друг сайт.')],
 'e107_languages/Bulgarian/lan_form_handler.php': [('LAN_EFORM_COPY', 'Копиране'), ('LAN_EFORM_COPIED', 'Копирано')],
 'e107_languages/Bulgarian/lan_rate.php': [('RATELAN_REFUSED_TOKEN_MISSING',
                                                 'Гласът ви не беше отчетен, защото връзката не съдържаше защитен токен. Гласувайте от полето за '
                                                 'оценяване на самата страница, а не чрез отметка или връзка от друг сайт.')],
 'e107_languages/Bulgarian/lan_signup.php': [('LAN_SIGNUP_REFUSED_TOKEN_MISSING',
                                                   'Не беше изпратен тестов имейл за активиране, защото връзката не съдържаше защитен токен. '
                                                   'Използвайте бутона на страницата за регистрация, а не отметка или връзка от друг сайт.')],
 'e107_languages/Bulgarian/lan_upload_handler.php': [('LANUPLOAD_REFUSED_TOKEN_MISSING',
                                                            'Нищо не беше качено, защото заявката не съдържаше защитен токен. Качвайте файлове чрез Медийния '
                                                            'мениджър, а не чрез отметка или връзка от друг сайт.')],
 'e107_languages/Bulgarian/lan_user.php': [('LAN_XUP_REFUSED_TOKEN_MISSING',
                                                 'Входът не беше стартиран, защото връзката не съдържаше защитен токен. Стартирайте го от бутон за '
                                                 'вход в този сайт, а не от отметка или връзка от друг сайт.'),
                                                ('LAN_XUP_REFUSED_NOT_A_NAVIGATION',
                                                 'Входът не беше стартиран, защото друг сайт го заяви във фонов режим, вместо да ви пренасочи тук. '
                                                 'Стартирайте го от бутон за вход в този сайт.')],
 'e107_languages/Bulgarian/lan_usersettings.php': [('LAN_USET_CONFIRM_PASSWORD_CHANGE', 'Потвърдете промените, като въведете текущата си парола: '),
                                                         ('LAN_USET_CHANGE_NOT_COMPLETED', 'Промените не бяха завършени. Моля, опитайте отново. '),
                                                         ('LAN_USET_DELETE_LINK_INVALID',
                                                          'Профилът ви не беше изтрит, защото тази връзка за потвърждение вече не е валидна. Заявете '
                                                          'изтриване отново по-долу, за да получите нова връзка.')]}

PLUGIN_ADDITIONS = {'e107_plugins/download/languages/Bulgarian/Bulgarian_admin.php': [('DOWLAN_LOCAL_PATH', 'Или път в директорията за изтегляния'),
                                                                          ('DOWLAN_LOCAL_PATH_NOT_FOUND',
                                                                           'В директорията за изтегляния няма файл с това име, затова нищо не беше записано. '
                                                                           'Проверете пътя спрямо директорията за изтегляния и изпратете записа отново.')],
 'e107_plugins/forum/languages/Bulgarian/Bulgarian_admin.php': [('FORLAN_REFUSED_TOKEN_MISSING',
                                                                      'Обновяването на форума не извърши промени, защото заявката не съдържаше защитен токен. '
                                                                      'Стартирайте го от административното меню на форума, а не от отметка или връзка от друг '
                                                                      'сайт.')],
 'e107_plugins/forum/languages/Bulgarian/Bulgarian_front.php': [('LAN_FORUM_ATTACHMENT_REFUSED_UNPROTECTED',
                                                                      'Прикаченият файл беше отказан: директорията му не можа да бъде защитена от директно '
                                                                      'изтегляне. Моля, уведомете администратора на сайта.'),
                                                                     ('LAN_FORUM_REFUSED_TOKEN_MISSING',
                                                                      'Нищо не беше маркирано като прочетено, защото връзката не съдържаше защитен токен. '
                                                                      'Използвайте маркера за нови публикации в списъка с форуми, а не отметка или връзка от друг '
                                                                      'сайт.')],
 'e107_plugins/newsletter/languages/Bulgarian_admin.php': [('NLLAN_REFUSED_TOKEN_MISSING',
                                                                  'Абонатът не беше премахнат, защото връзката не съдържаше защитен токен. Използвайте бутона '
                                                                  'за изтриване в списъка с абонати, а не отметка или връзка от друг сайт.')],
 'e107_plugins/pm/languages/Bulgarian.php': [('LAN_PM_REFUSED_TOKEN_MISSING',
                                                   'Нищо не беше променено, защото връзката не съдържаше защитен токен. Използвайте бутоните в '
                                                   'страниците за лични съобщения, а не отметка или връзка от друг сайт.')]}

CRON_BG = '<?php\n/*\n * e107 website system - Bulgarian administrative language file\n */\nif (!defined("PAGE_NAME")) { define("PAGE_NAME", "Задачи по график"); }\n\n// Меню\ndefine("LAN_CRON_M_02", "Обновяване");\ndefine("LAN_CRON_M_SETUP", "Настройка");\n\n// Заглавия на таблицата\ndefine("LAN_CRON_2", "Функция");\ndefine("LAN_CRON_3", "Раздел");\ndefine("LAN_CRON_4", "Последно изпълнение");\n\n// Стандартни задачи\ndefine("LAN_CRON_01_1", "Тестов имейл");\ndefine("LAN_CRON_01_2", "Изпращане на тестов имейл до [eml].");\ndefine("LAN_CRON_01_3", "Препоръчва се за проверка на системата за задачи по график.");\n\ndefine("LAN_CRON_02_1", "Опашка за имейли");\ndefine("LAN_CRON_02_2", "Обработване на опашката за имейли.");\n\ndefine("LAN_CRON_03_1", "Проверка за върнати имейли");\ndefine("LAN_CRON_03_2", "Проверка за недоставени и върнати имейли.");\n\ndefine("LAN_CRON_04_1", "Повторна проверка на блокиранията");\ndefine("LAN_CRON_04_2", "Обработване на повторно задействани блокирания.");\ndefine("LAN_CRON_04_3", "Необходимо е само ако е активирано повторното задействане на блокирания.");\n\ndefine("LAN_CRON_05_1", "Резервно копие на базата данни");\ndefine("LAN_CRON_05_2", "Създаване на резервно копие на системната база данни в");\n\ndefine(\'LAN_CRON_06_1\', "Обработване на условие за блокиране");\n\n// Грешки и информационни съобщения\ndefine("LAN_CRON_6", "Настройките не можаха да бъдат импортирани");\ndefine("LAN_CRON_7", "Настройките за изпълнение не можаха да бъдат импортирани");\ndefine("LAN_CRON_8", "Импортирани настройки за изпълнение за");\n\ndefine("LAN_CRON_9", "преди [x] минути и [y] секунди.");\ndefine("LAN_CRON_10", "преди [y] секунди.");\n\ndefine("LAN_CRON_11", "Активни задачи");\ndefine("LAN_CRON_12", "Последно обновяване на cron");\n\n// Информация за checkCoreUpdate\ndefine("LAN_CRON_20_1", "Проверка за обновяване на e107");\ndefine("LAN_CRON_20_2", "Проверка в e107.org за обновявания на ядрото");\ndefine("LAN_CRON_20_3", "Препоръчва се, за да поддържате системата актуална.");\ndefine("LAN_CRON_20_4", "Обновяване на това Git хранилище");\ndefine("LAN_CRON_20_5", "Обновяване на тази e107 инсталация с най-новите файлове от GitHub.");\ndefine("LAN_CRON_20_6", "Препоръчва се само за разработчици.");\ndefine("LAN_CRON_20_8", "Може да причини нестабилност на сайта.");\n\ndefine("LAN_CRON_30", "Всяка минута");\ndefine("LAN_CRON_31", "През минута");\ndefine("LAN_CRON_32", "На всеки 5 минути");\ndefine("LAN_CRON_33", "На всеки 10 минути");\ndefine("LAN_CRON_34", "На всеки 15 минути");\ndefine("LAN_CRON_35", "На всеки 30 минути");\n\ndefine("LAN_CRON_36", "Всеки час");\ndefine("LAN_CRON_37", "През час");\ndefine("LAN_CRON_38", "На всеки 3 часа");\ndefine("LAN_CRON_39", "На всеки 6 часа");\n\ndefine("LAN_CRON_40", "Всеки ден");\ndefine("LAN_CRON_41", "Всеки месец");\ndefine("LAN_CRON_42", "Всеки делничен ден");\n\ndefine("LAN_CRON_50", "Минути:");\ndefine("LAN_CRON_51", "Часове:");\ndefine("LAN_CRON_52", "Дни:");\ndefine("LAN_CRON_53", "Месеци:");\ndefine("LAN_CRON_54", "Дни от седмицата:");\ndefine("LAN_CRON_55", "Резервното копие на базата данни е неуспешно");\ndefine("LAN_CRON_56", "Резервното копие на базата данни е завършено");\n\ndefine("LAN_CRON_61", "Генериране на нов cron токен");\ndefine("LAN_CRON_62", "Изпълнява се конфигурационна функция [b][x][/b]");\ndefine("LAN_CRON_63", "Конфигурационната функция [b][x][/b] не е намерена.");\ndefine("LAN_CRON_64", "Администраторът може да автоматизира задачи чрез системата „Задачи по график“ на e107.[br]\\nНищо тук няма да се изпълнява, докато сървърът не извиква [b]cron.php[/b] веднъж в минута. Разделът „Настройка“ показва как да го конфигурирате и предоставя команда за копиране.[br]\\nВ раздела „Управление“ можете да редактирате, изтривате и стартирате задачи.[br]\\nПри редактиране на задача можете да зададете минутите, часовете, дните, месеца или деня от седмицата, в които да се изпълнява. Използвайте * за всеки период и свойството „Активно“, за да включите задачата.[br]\\n\\nЗабележка: не се препоръчва да изтривате стандартните задачи.[br]");\n\ndefine("LAN_CRON_BACKUP", "Резервно копие");\ndefine("LAN_CRON_LOGGING", "Запис в журнал");\ndefine("LAN_CRON_RUNNING", "Изпълнява се");\n\ndefine("LAN_CRON_65", "Обновяване на Git хранилището на темата");\ndefine("LAN_CRON_66", "Не е намерено Git хранилище");\ndefine("LAN_CRON_67", "В директорията на темата не е намерено Git хранилище");\n\ndefine("LAN_CRON_SETUP_INTRO", "За да се изпълняват задачите по график, сървърът трябва да извиква [b]cron.php[/b] веднъж в минута. Изберете една от опциите по-долу, копирайте показаното в планировчика на сървъра и използвайте само една опция, иначе задачите, чието време е настъпило, ще се изпълняват два пъти.");\ndefine("LAN_CRON_SETUP_HTTP_TITLE", "Уеб заявка");\ndefine("LAN_CRON_SETUP_HTTP_WHY", "Планировчикът извлича URL адрес веднъж в минута. Заявката се изпълнява с PHP версията, избрана за този сайт, не изисква файлови права и работи както с cron задачи в контролен панел, така и с външни cron услуги.");\ndefine("LAN_CRON_SETUP_CLI_TITLE", "PHP от команден ред");\ndefine("LAN_CRON_SETUP_CLI_WHY", "Планировчикът стартира PHP интерпретатора за cron.php. Използва се PHP изпълнимият файл, посочен в командата, затова поддържайте командата съобразена с PHP версията на сайта.");\ndefine("LAN_CRON_SETUP_SHEBANG_TITLE", "Shell скрипт");\ndefine("LAN_CRON_SETUP_SHEBANG_WHY", "Планировчикът стартира cron.php директно, а първият му ред избира php от PATH. Файлът трябва да е изпълним, а PATH на cron обикновено е ограничен, затова може да не бъде намерен php или да бъде използвана грешна версия.");\ndefine("LAN_CRON_SETUP_COMMAND_LABEL", "Команда (поставете я в cron задачата на контролния панел)");\ndefine("LAN_CRON_SETUP_CRONTAB_LABEL", "Ред за crontab (изпълнява се всяка минута)");\ndefine("LAN_CRON_SETUP_URL_LABEL", "URL (за външни cron услуги като cron-job.org или EasyCron)");\ndefine("LAN_CRON_SETUP_WINDOWS_COMMAND_LABEL", "Команда (за действие в Windows Task Scheduler)");\ndefine("LAN_CRON_SETUP_SCHTASKS_LABEL", "Създаване на задачата с една команда (Command Prompt като администратор)");\ndefine("LAN_CRON_SETUP_RECOMMENDED", "Препоръчително");\ndefine("LAN_CRON_SETUP_PANEL_HOWTO", "В cPanel, DirectAdmin или Plesk отворете страницата за cron задачи и добавете задача, която се изпълнява всяка минута с тази команда. Без контролен панел изпълнете [b]crontab -e[/b] и добавете реда за crontab.");\ndefine("LAN_CRON_SETUP_WGET_LABEL", "С wget вместо curl");\ndefine("LAN_CRON_SETUP_HTTP_FALLBACK_NOTE", "Ако сървърът не може да достъпи собствения URL адрес на сайта (някои хостинги го блокират), използвайте вместо това опцията PHP от команден ред.");\ndefine("LAN_CRON_SETUP_PHP_FOUND", "PHP е намерен на [x].");\ndefine("LAN_CRON_SETUP_PHP_NOT_FOUND", "Не можа да бъде потвърден PHP изпълним файл, затова командата приема, че [b]php[/b] е наличен в PATH. Ако не е, попитайте хостинг доставчика за пътя до PHP [x] изпълнимия файл за команден ред.");\ndefine("LAN_CRON_SETUP_OPEN_BASEDIR_NOTE", "open_basedir предотврати проверката за PHP изпълними файлове.");\ndefine("LAN_CRON_SETUP_EXECUTABLE", "cron.php е изпълним.");\ndefine("LAN_CRON_SETUP_NOT_EXECUTABLE", "cron.php не е изпълним. Първо го направете изпълним:");\ndefine("LAN_CRON_SETUP_REGENERATE_WARNING", "Генерирането на нов токен обезсилва вече настроената команда. След това копирайте новата команда в планировчика.");\ndefine("LAN_CRON_REFUSED_SUMMARY", "От [y] са отказани [x] заявка/заявки към cron.php; последната е в [z].");\ndefine("LAN_CRON_REFUSED_LAST_FROM", "Последната заявка е от [x].");\ndefine("LAN_CRON_REFUSED_TOKEN_INCORRECT", "Заявките съдържат токен, който не съвпада.");\ndefine("LAN_CRON_REFUSED_TOKEN_MISSING", "Заявките не съдържат токен.");\ndefine("LAN_CRON_REFUSED_COPY_AGAIN", "Копирайте командата отново от раздела [x].");\ndefine("LAN_CRON_NEVER_REPORTED", "Все още няма отчет от задача по график. Следвайте указанията в раздела [x], за да насрочите cron.php на сървъра.");\ndefine("LAN_CRON_LASTRUN_HTTP", "през HTTP");\ndefine("LAN_CRON_LASTRUN_HTTP_FROM", "през HTTP от [x]");\ndefine("LAN_CRON_LASTRUN_CLI", "от командния ред");\ndefine("LAN_CRON_SETUP_DETECTED_ENVIRONMENT", "Открита среда: [x]");\ndefine("LAN_CRON_SETUP_OPEN_PANEL", "Отваряне на [x]");\ndefine("LAN_CRON_SETUP_CONTROL_PANEL", "Контролен панел");\ndefine("LAN_CRON_SETUP_SCHTASKS_ACCOUNT_NOTE", "Task Scheduler изпълнява командата с избрания от вас акаунт; използвайте акаунт, който има достъп за четене до файловете на сайта.");\ndefine("LAN_CRON_SETUP_CURL_EXE_NOTE", "curl.exe е включен в Windows 10 и по-новите версии; при по-стари системи използвайте опцията PHP от команден ред.");\ndefine("LAN_CRON_TOKEN_REGENERATED", "Генериран е нов cron токен. Обновете командата в планировчика на сървъра.");\n'

SIGNIN_BG = '<?php\n/*\n * e107 website system\n *\n * Bulgarian translation - Signin plugin frontend\n */\ndefine("LAN_SIGNIN_USERNAME", "Потребителско име: ");\ndefine("LAN_SIGNIN_EMAIL", "Имейл: ");\ndefine("LAN_SIGNIN_USEREMAIL", "Потребителско име или имейл: ");\ndefine("LAN_SIGNIN_SIGNIN", "Вход");\ndefine("LAN_SIGNIN_SIGNUP", "Регистрация");\ndefine("LAN_SIGNIN_REMEMBER", "Запомни ме");\ndefine("LAN_SIGNIN_FPW", "Забравена парола?");\ndefine("LAN_SIGNIN_RESEND", "Повторно изпращане на имейла за активиране");\ndefine("LAN_SIGNIN_PROFILE", "Профил");\ndefine("LAN_SIGNIN_ADMIN", "Администрация");\ndefine("LAN_SIGNIN_MAINTENANCE", "Режимът за поддръжка е включен — това означава, че обикновените посетители се пренасочват към sitedown.php. За да изключите режима, отидете в Администрация → Поддръжка.");\n'

PAIRS = [('e107_languages/English/English.php', 'e107_languages/Bulgarian/Bulgarian.php'),
 ('e107_languages/English/admin/lan_admin.php', 'e107_languages/Bulgarian/admin/lan_admin.php'),
 ('e107_languages/English/admin/lan_cron.php', 'e107_languages/Bulgarian/admin/lan_cron.php'),
 ('e107_languages/English/admin/lan_db.php', 'e107_languages/Bulgarian/admin/lan_db.php'),
 ('e107_languages/English/admin/lan_e107_update.php', 'e107_languages/Bulgarian/admin/lan_e107_update.php'),
 ('e107_languages/English/admin/lan_lancheck.php', 'e107_languages/Bulgarian/admin/lan_lancheck.php'),
 ('e107_languages/English/admin/lan_mailout.php', 'e107_languages/Bulgarian/admin/lan_mailout.php'),
 ('e107_languages/English/admin/lan_menus.php', 'e107_languages/Bulgarian/admin/lan_menus.php'),
 ('e107_languages/English/admin/lan_plugin.php', 'e107_languages/Bulgarian/admin/lan_plugin.php'),
 ('e107_languages/English/admin/lan_theme.php', 'e107_languages/Bulgarian/admin/lan_theme.php'),
 ('e107_languages/English/admin/lan_users.php', 'e107_languages/Bulgarian/admin/lan_users.php'),
 ('e107_languages/English/lan_form_handler.php', 'e107_languages/Bulgarian/lan_form_handler.php'),
 ('e107_languages/English/lan_rate.php', 'e107_languages/Bulgarian/lan_rate.php'),
 ('e107_languages/English/lan_signup.php', 'e107_languages/Bulgarian/lan_signup.php'),
 ('e107_languages/English/lan_upload_handler.php', 'e107_languages/Bulgarian/lan_upload_handler.php'),
 ('e107_languages/English/lan_user.php', 'e107_languages/Bulgarian/lan_user.php'),
 ('e107_languages/English/lan_usersettings.php', 'e107_languages/Bulgarian/lan_usersettings.php'),
 ('e107_plugins/download/languages/English/English_admin.php', 'e107_plugins/download/languages/Bulgarian/Bulgarian_admin.php'),
 ('e107_plugins/forum/languages/English/English_admin.php', 'e107_plugins/forum/languages/Bulgarian/Bulgarian_admin.php'),
 ('e107_plugins/forum/languages/English/English_front.php', 'e107_plugins/forum/languages/Bulgarian/Bulgarian_front.php'),
 ('e107_plugins/newsletter/languages/English_admin.php', 'e107_plugins/newsletter/languages/Bulgarian_admin.php'),
 ('e107_plugins/pm/languages/English.php', 'e107_plugins/pm/languages/Bulgarian.php'),
 ('e107_plugins/signin/languages/English/English_front.php', 'e107_plugins/signin/languages/Bulgarian/Bulgarian_front.php')]

from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
VERSION = "2.3.12"
DATE = "2026-09-06"

def p(rel):
    return ROOT / rel

def php_define(key, value):
    value = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'define("{key}", "{value}");'

def active_keys(text):
    keys = []
    in_block = False
    for line in text.splitlines():
        s = line.lstrip()
        if in_block:
            if "*/" in s:
                in_block = False
                s = s.split("*/", 1)[1].lstrip()
            else:
                continue
        if s.startswith("/*"):
            if "*/" in s:
                s = s.split("*/", 1)[1].lstrip()
            else:
                in_block = True
                continue
        if not s or s.startswith("//") or s.startswith("#"):
            continue
        m = re.search(r'\bdefine\s*\(\s*["\']([^"\']+)["\']', s)
        if m:
            keys.append(m.group(1))
    return keys

def append_defines(rel, defs):
    path = p(rel)
    text = path.read_text(encoding="utf-8")
    existing = set(active_keys(text))
    out = text.rstrip() + "\n"
    added = 0
    for key, value in defs:
        if key in existing:
            continue
        out += php_define(key, value) + "\n"
        existing.add(key)
        added += 1
    path.write_text(out, encoding="utf-8", newline="\n")
    print(f"{rel}: +{added}")

def write_file(rel, content):
    path = p(rel)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8", newline="\n")
    print(f"{rel}: written")

def update_xml():
    path = p("e107_languages/Bulgarian/Bulgarian.xml")
    text = path.read_text(encoding="utf-8")
    text = re.sub(r'compatibility="[^"]+"', f'compatibility="{VERSION}"', text)
    text = re.sub(r'date="[^"]+"', f'date="{DATE}"', text)
    path.write_text(text, encoding="utf-8", newline="\n")

def update_readme():
    path = p("README.md")
    text = path.read_text(encoding="utf-8")
    text = text.replace("e107 v2.3.11", "e107 v2.3.12")
    text = text.replace('compatibility="2.3.11"', 'compatibility="2.3.12"')
    text = text.replace("**108 core/admin PHP файла** — 35 основни, 44 административни и 29 файла в `admin/help/`;",
                        "**107 core/admin PHP файла** — 35 основни, 44 административни и 28 файла в `admin/help/`;")
    text = text.replace("**84 PHP езикови файла** на стандартните bundled плъгини;",
                        "**85 PHP езикови файла** на стандартните bundled плъгини;")
    text = text.replace("всички 29 PHP help файла от `e107_languages/English/admin/help/`;",
                        "всички 28 PHP help файла от `e107_languages/English/admin/help/`;")
    text = text.replace("**29/29** PHP файла в `admin/help/`;", "**28/28** PHP файла в `admin/help/`;")
    text = text.replace("**29/29** PHP admin help файла;", "**28/28** PHP admin help файла;")
    text = text.replace("**84** езикови файла на стандартните bundled плъгини;",
                        "**85** езикови файла на стандартните bundled плъгини;")
    text = text.replace("`search_menu`, `signin`, `contact` и `admin_menu`",
                        "`search_menu`, `contact` и `admin_menu`")
    text = text.replace("`alt_auth`, `login_menu`, `user`;", "`alt_auth`, `login_menu`, `signin`, `user`;")
    replacement = """## Актуализация за e107 v2.3.12

Направено е директно сравнение на официалните upstream тагове **v2.3.11 → v2.3.12**.

Между двете версии има **551 upstream commits**. Променени са 23 съществуващи езикови ресурса, добавен е нов frontend language файл за плъгина `signin`, а legacy `e107_languages/English/admin/help/cron.php` е премахнат, тъй като помощта за задачите по график вече е интегрирана в `admin/lan_cron.php`.

Основните промени в българския пакет са:

- нови съобщения за отказани действия при липсващ security token в core и администрацията;
- изцяло обновен превод на `admin/lan_cron.php`, включително новия раздел за настройка на `cron.php`, HTTP/CLI/shell варианти, Windows Task Scheduler, cPanel/DirectAdmin/Plesk и диагностиката на cron заявките;
- нови текстове за копиране във form handler, оценяване, регистрация, качване, потребителски вход и настройки на профила;
- нови текстове в Download, Forum, Newsletter и Private Messenger;
- нов български frontend language файл за bundled плъгина `signin`;
- премахнат е `admin/help/cron.php` в синхрон с upstream структурата.

Структурната промяна запазва общия брой от **196 PHP езикови/help файла**: core/admin файловете стават 107 заради премахнатия cron help файл, а plugin language файловете стават 85 заради новия `signin` language resource.

"""
    text = re.sub(r"## Актуализация за e107 v2\.3\.12.*?(?=\n## Основен e107 превод)", replacement, text, flags=re.S)
    text = text.replace("сравнение на официалните тагове `v2.3.10` и `v2.3.12`;",
                        "сравнение на официалните тагове `v2.3.11` и `v2.3.12`;")
    path.write_text(text, encoding="utf-8", newline="\n")

def apply():
    for rel, defs in CORE_ADDITIONS.items():
        append_defines(rel, defs)
    for rel, defs in PLUGIN_ADDITIONS.items():
        append_defines(rel, defs)
    write_file("e107_languages/Bulgarian/admin/lan_cron.php", CRON_BG)
    cron_help = p("e107_languages/Bulgarian/admin/help/cron.php")
    if cron_help.exists():
        cron_help.unlink()
        print("admin/help/cron.php: removed")
    write_file("e107_plugins/signin/languages/Bulgarian/Bulgarian_front.php", SIGNIN_BG)
    update_xml()
    update_readme()

def check_local():
    changed_php = list(CORE_ADDITIONS) + list(PLUGIN_ADDITIONS) + [
        "e107_languages/Bulgarian/admin/lan_cron.php",
        "e107_plugins/signin/languages/Bulgarian/Bulgarian_front.php",
    ]
    errors = []
    for rel in changed_php:
        path = p(rel)
        keys = active_keys(path.read_text(encoding="utf-8"))
        dups = sorted({k for k in keys if keys.count(k) > 1})
        if dups:
            errors.append(f"{rel}: duplicate keys {dups}")
        r = subprocess.run(["php", "-l", str(path)], capture_output=True, text=True)
        if r.returncode:
            errors.append(f"{rel}: php -l failed: {r.stdout}{r.stderr}")
    if p("e107_languages/Bulgarian/admin/help/cron.php").exists():
        errors.append("admin/help/cron.php should be removed")
    xml = p("e107_languages/Bulgarian/Bulgarian.xml").read_text(encoding="utf-8")
    if 'compatibility="2.3.12"' not in xml:
        errors.append("Bulgarian.xml compatibility mismatch")
    if errors:
        raise SystemExit("\n".join(errors))
    print("Local QA passed.")

def check_upstream(upstream_dir):
    upstream = Path(upstream_dir)
    errors = []
    for en_rel, bg_rel in PAIRS:
        ek = active_keys((upstream / en_rel).read_text(encoding="utf-8"))
        bk = active_keys(p(bg_rel).read_text(encoding="utf-8"))
        missing = sorted(set(ek) - set(bk))
        extra = sorted(set(bk) - set(ek))
        if missing or extra:
            errors.append(f"{bg_rel}: missing={missing}, extra={extra}")
    if (upstream / "e107_languages/English/admin/help/cron.php").exists():
        errors.append("upstream v2.3.12 unexpectedly has admin/help/cron.php")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Upstream v{VERSION} define-key parity passed for {len(PAIRS)} changed resources.")

if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--check-upstream":
        check_upstream(sys.argv[2])
    else:
        apply()
        check_local()
