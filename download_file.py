import urllib

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def open_dropdown(driver, dropdown_xpath, element_name, check_condition=False):
    
    # запомним адрес текущей страницы
    current_url = driver.current_url
    
    # открыть меню с перечнем гран-при, прошедших в текущем сезоне           
    dropdown = WebDriverWait(driver, 15) \
                .until(EC.presence_of_element_located((By.XPATH, dropdown_xpath)))
    # зафиксируем текст внутри выпадающего меню
    dropdown_text = dropdown.get_attribute('textContent')

    driver.execute_script("arguments[0].click();", dropdown)

    # найти элемент( название гран-при, год) по заранее заданному имени имени
    # element = WebDriverWait(driver, 15) \
    #             .until(EC.presence_of_element_located((By.XPATH, \
    #             '//*[contains(text(), "{}")]'.format(element_name))))
    
    element = driver.find_element(By.XPATH, \
                '//*[contains(text(), "{}") and @class="v-list-item__title"]'.format(element_name))

    driver.execute_script("arguments[0].click();", element)
    
    if check_condition:
        # проконтролируем то, что javascript прогрузился полностью и 
        # на странице появились данные именно те данные, которые
        # нам требуются;
        # дл фиксации используем понимание того, что вместе с обновлением
        # данных на странице обновится и ссылка
        # если нам необходимы данные последней прошедшей гонки, то
        # этот пукнт можно не выполнять, так как мы уже находимя на нужной странице
        # с правильным адресом

        # если он не включает в себя название того, что мы ищем
        # (что означает, что пока мы не находимся на странице с нужными данными)
        if element_name not in dropdown_text:

            # зафиксируем состояние
            condition = True
            # если оно не изменилось
            while condition:
                # определяем ссылку странице, на которой находимся
                new_url = driver.current_url
                # если она не совпадает с той, на которой мы находились до 
                # запуска функции, то это означает, что прогрузились новые данные - 
                # те, которые нам нужны
                if new_url not in current_url:
                    # меняем состояние и тем самым завершаем цикл
                    condition = False


def download_file(href, file_name):
    
    if not os.path.isfile(file_name):
        urllib.request.urlretrieve(href, file_name)
        
        
def retry_loading_simple(driver):
    
    print('Timeout, retrying 1...')
    
    # создаем переменную с сылкой текущей страницы
    current_url = chrome.current_url
    # создаем счетчик
    k = 2
    # задаем условие
    condition = True
    # пока оно выполняется
    while condition:
        # пробуем
        try:
            # пройти по текущей ссылке
            driver.get(current_url)
            # если это удалось, условие перестает выполняться
            # и цикла завершается
            condition = False
        # если страница не загрузилась из-за таймаута
        # обновляем страницу и повторяем цикл
        except TimeoutException:
            print('Timeout, retrying {}...'.format(k))
            k += 1
            # driver.refresh()
            pass
        
        
def retry_loading(driver):
    
    print('Timeout, retrying 1...')
    # создаем счетчик
    k = 2
    
    try: 
        # создаем переменную с сылкой текущей страницы
        current_url = driver.current_url
        # задаем условие
        condition = True
        # пока оно выполняется
        while condition:
            # пробуем
            try:
                # пройти по текущей ссылке
                driver.get(current_url)
                # если это удалось, условие перестает выполняться
                # и цикла завершается
                condition = False
            # если страница не загрузилась из-за таймаута
            # обновляем страницу и повторяем цикл
            # данным таймаутом мы контролируем переход по ссылке
            except TimeoutException:
                print('Timeout, retrying {}...'.format(k))
                k += 1
                # обновление здесь не корректно, потому что обновление произойдет по старому адрес
                # эта страница так устроена, что сначала загружается один адрес, а через некотрое 
                # время он меняется на другой; соответственно простое обновление страницы сбросит все
                # введенные до этого данные
                # driver.refresh()
                pass

    # этим таймаутом мы контролируем зависание на моменте получения
    # ссылки текущей страницы вначале первого try
    except TimeoutException:
        pass
    
# преобразовываем название гран-при
grand_prix_name_upper = str(grand_prix_name).upper()

# присваемваем переменным извстные id
cookies_id = 'onetrust-accept-btn-handler'
results_id = 'mmResults'

# присываемваем переменным известные paths
year_dropdown_xpath = \
    '//*[@id="main-container"]/div/div[2]/div/div/div[4]/div[1]/div/div/div'
grand_prix_dropdown_xpath = \
    '//*[@id="main-container"]/div/div[2]/div/div/div[4]/div[2]/div/div/div'
current_grandprix_title_path = '//*[@id="header"]/div/div[1]/div/span'
more_results_xpath = \
    '//*[@id="main-container"]/div/div[3]/div/div[1]/div[1]/span[2]/div/div[1]'
more_results_class_name = 'c-docNav__link qa_menu_world_standing px-0 v-tab'
more_results_xpath_w_class_name = \
    '//div[@class="v-list-group__header v-list-item v-list-item--active v-list-item--link theme--light"]'
analysis_xpath = \
    '//*[@id="main-container"]/div/div[3]/div/div[1]/div[1]/span[2]/div/div[2]/a[1]'
lapchart_xpath = \
    '//*[@id="main-container"]/div/div[3]/div/div[1]/div[1]/span[2]/div/div[2]/a[4]'

# инициируем переменную с настройками chrome
options = webdriver.ChromeOptions()

# запустить chrome в полноэкранном режиме
if fullscreen:
    options.add_argument("--kiosk")
    options.add_argument("--start-maximized")

# не отображать интерфейс и окно chrome 
if not browser_interface:
    options.add_argument("--headless")

options.add_argument("window-size=1920x1080")

# неотображать надпись о том, что браузером управляет тестовое ПО
options.add_experimental_option("excludeSwitches", ['enable-automation'])

# создаем эмулятор браузера
chrome = webdriver.Chrome(options=options)

# определяем максимальную длительность загрузки
# сайта для таймаута
chrome.set_page_load_timeout(20)

# переходим на сайт motogp
k = 1
condition = True
while condition:
    try:
        chrome.get('http://www.motogp.com')
        condition = False
    except TimeoutException:
        print('Timeout, retrying {}...'.format(k))
        chrome.refresh()
        k += 1
del k

# убедимся, что открылось нужно окно
assert 'MotoGP' in chrome.title
print(chrome.current_url)

# cookies accept
cookies_form = WebDriverWait(chrome, 5).until( \
               EC.element_to_be_clickable((By.ID, cookies_id)))

cookies_form.click()

# создем переменную, в которой будет храниться элемент
# results на главной странице сайта
results = WebDriverWait(chrome, 15) \
            .until(EC.presence_of_element_located((By.ID, results_id)))

# кликаем по results и переходим на новую страницу
try:
    chrome.execute_script("arguments[0].click();", results)
    # зафиксируем, что retrying не было
    retrying = False
except TimeoutException:
    # учтем, что retrying был, это пригодится в дальнейшем
    retrying = True
    retry_loading(chrome)
    
# убедимся, что открылось нужное окно и страница с результатами прогрузилась полностью
# (потому что изначально страница results открывает с одноим адресом, через некоторое 
# время адрес меняется на другой)
# дождаться изменения адрес необходимо потому, что в следующей функции open_dropdown
# именно через адрес страницы осуществляется контроль того, что подгрузились выбранные 
# нами характеристики - нужные год и название гран-при

# сперва проверим заголовок
# assert 'RESULTS' in chrome.title

# если был retrying и страница уже перезагружалась, то адрес уже
# сменился и данную проверку можно не делать 
if not retrying:
    # фиксирум текущий адрес сртаницы 
    current_url = chrome.current_url
    # если он не содержит слово 'Classification', то адрес еще не изменился
    # (старый адрес не содержит этого слова)
    if 'Classification' not in current_url:
        # фиксируем состояние
        condition = True
        while condition:
            # продолжаем фиксировать адрес страницы
            new_url = chrome.current_url
            # и ждем, пока в нем не появится слово 'Classification'
            if 'Classification' in new_url:
                condition = False

print(chrome.current_url)

# раскрываем выпадающее меню с годом
# и выбираем год, определенный вначале скрипта
open_dropdown(
    driver=chrome,
    dropdown_xpath=year_dropdown_xpath,
    element_name=year_name,
    check_condition=True
)

# раскрываем выпадающее меню с названием гран-при и выбираем гран-при, 
# определенное вначале скрипта
# после того, как мы выбрали интересующий нас год в предыдущем open_dropdown 
# и выбрали интересующий нас гран-при в этом open_dropdown, 
# проконтролируем, что данные полнстью загрузятся с помощью аргумента check_condition
# и только после этого продолжим выполнение скрипта
open_dropdown(
    driver=chrome,
    dropdown_xpath=grand_prix_dropdown_xpath,
    element_name=grand_prix_name_upper,
    check_condition=True
)

# # создем переменную, в которой будет храниться элемент
# more results на этой странице
more_results = WebDriverWait(chrome, 15) \
                .until(EC.presence_of_element_located((By.XPATH, more_results_xpath)))

# кликаем по more results
chrome.execute_script("arguments[0].click();", more_results)

# определяем элементы analysis и lapchart,
# в которых хранятся ссылки на интересующие нас файлы
analysis = WebDriverWait(chrome, 15) \
            .until(EC.presence_of_element_located((By.XPATH, analysis_xpath)))
lapchart = WebDriverWait(chrome, 15) \
            .until(EC.presence_of_element_located((By.XPATH, lapchart_xpath)))

# извлекаем ссылки из элементов analysis и lapchart
analysis_href = analysis.get_attribute('href')
lapchart_href = lapchart.get_attribute('href')

analysis_file_name = year_name + '_' + grand_prix_name_file + '_analysis.pdf'
lapchart_file_name = year_name + '_' + grand_prix_name_file + '_lapchart.pdf'

# скачиваем файлы
download_file(analysis_href, analysis_file_name)
download_file(lapchart_href, lapchart_file_name)

# зафиксируем адрес страницы перед закрытием браузера
print(chrome.current_url)

# закрываем браузер
chrome.close()