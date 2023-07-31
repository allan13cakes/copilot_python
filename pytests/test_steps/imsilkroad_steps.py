import config
from pytests.conftest import *


@allure.step('login to imsilkroad')
def login_to_imsilkroad(imsilkroad_page):
    url = 'https://www.imsilkroad.com/login'
    user_name = config.config['username']
    password = config.config['password']
    encrypted_password = password.encode('utf-8')
    # Decrypt the password
    decrypted_password = config.cipher.decrypt(encrypted_password)
    imsilkroad_page.load(url)
    take_screen_shot(imsilkroad_page)
    imsilkroad_page.login(user_name, decrypted_password.decode('utf-8'))
    take_screen_shot(imsilkroad_page)

@allure.step('fill search filters')
def fill_search_filters(imsilkroad_page):
    imsilkroad_page.navigate_to_menu('数据')
    imsilkroad_page.select_tree_data_menus(['亚洲','中国'])
    imsilkroad_page.select_tree_data_menus(['国民经济核算','国内生产总值','国内生产总值：分产业','服务业占GDP的百分比（年度）'])
    imsilkroad_page.select_statistical_period('年')
    # imsilkroad_page.select_date_range('20年')
    take_screen_shot(imsilkroad_page)

@allure.step('get search result')
def get_search_result(imsilkroad_page):
    df = imsilkroad_page.get_result_table_data()
    html_table = df.to_html()
    allure.attach(html_table, name='Processed Data', attachment_type=allure.attachment_type.HTML)
    image = imsilkroad_page.get_result_canvas()
    timestamp = int(time.time())
    with open(image, "rb") as f:
        allure.attach(f.read(), name=f'chart_{timestamp}', attachment_type=allure.attachment_type.PNG)

    # with open(file_name, "rb") as f:
    #     allure.attach(f.read(), name=f"screenshot_{timestamp}", attachment_type=allure.attachment_type.PNG)

    take_screen_shot(imsilkroad_page)



