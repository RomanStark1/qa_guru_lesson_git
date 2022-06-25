# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__

def print_func(this_func):
    name = this_func.__name__
    params = this_func.__code__.co_varnames
    if len(params) > 1:
        print(f'имя функции {name} и ее у нее есть аргументы: {params}')
    elif len(params) == 1 :
        print(f'имя функции {name} и ее у нее есть аргумент: {params}')
    else:
        print(f'имя функции {name} и у нее нет аргументов')


def open_browser(browser_name):
    pass


def go_to_companyname_homepage(page_url):
    pass


def find_registration_button_on_login_page(page_url, button_text):
    pass

def some_func_without_arg():
    pass



list_func = [open_browser, go_to_companyname_homepage, find_registration_button_on_login_page, some_func_without_arg]

for i in range(len(list_func)):
    print_func(list_func[i])