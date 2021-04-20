import os
from time import sleep
from selenium import webdriver
# from util.sql_util import SqlUtil

#数据库配置
host='127.0.0.1'
port=3306
user='root'
passwd='123'
db='shop'
# cursor, conn = SqlUtil(host=host,port=port,user=user,passwd=passwd,db=db).connect_db()
import requests
from bs4 import BeautifulSoup

project_dir=os.path.join(os.getcwd(),"..")
chromedriver_dir=os.path.join(project_dir,'Chromedriver')
print("project_dir:"+project_dir)
print("chromedriver_dir:"+chromedriver_dir)

#chromedriver设置
CHROME_PATH = os.path.join(chromedriver_dir,'chromedriver_'+'89')  # your chromedriver's path，这个是网页和chrome浏览器之间通信必须要用到的
print("CHROME_PATH:",CHROME_PATH)
chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_argument('--no-sandbox')
chrome_opt.add_argument("--disable-dev-shm-usage")
# chrome_opt.add_argument("proxy-server=http://127.0.0.1:1087")  # 加载代理IP

driver = webdriver.Chrome(executable_path=CHROME_PATH, desired_capabilities=chrome_opt.to_capabilities())
# a = driver.execute_cdp_cmd("Emulation.setGeolocationOverride",
#                            cmd_args={'latitude': 39.97947, 'longitude': 116.40914, 'accuracy': 100})  # 北京市的经纬度
# 上海市的经纬度121.4852，31.24956
# print(a)
# sleep(10)


driver.get("http://m.tsbeer.com/mdcf?RH=223e4f84")  #加载对应url
driver.find_element_by_class_name("hc-btn-cancel").click()  #取消
sleep(3)
driver.find_element_by_class_name("hc-current-region").click() #定位
sleep(6)
url=driver.current_url
print("url:"+url)
# print("page_source"+str(driver.page_source))
# result = requests.get(url=url)


mint_cell_texts=driver.find_elements_by_class_name("mint-cell-text")
mint_cell_texts_length= len(mint_cell_texts)
print("mint_cell_texts_length:"+str(mint_cell_texts_length))
hc_region_items=driver.find_elements_by_class_name("hc-region-item")
hc_region_items_length=len(hc_region_items)
print("hc_region_items_length："+str(hc_region_items_length))
print("hc_region_items[10].is_enabled():"+str(hc_region_items[10].is_enabled()))
print("hc_region_items[10].is_displayed():"+str(hc_region_items[10].is_displayed()))
k=0
a=""
#爬取95页的商家信息
for i in range(95, mint_cell_texts_length):

    try:
        sleep(10)
        a =driver.find_elements_by_class_name("mint-cell-text")[i].text
        driver.find_elements_by_class_name("mint-cell-text")[i].click()

    except:
        sleep(8)
        a = driver.find_elements_by_class_name("mint-cell-text")[i].text
        # driver.find_elements_by_class_name("mint-cell-text")[i].click()
        # mint_cell_texts[i].click()
        driver.execute_script("arguments[0].click();", driver.find_elements_by_class_name("mint-cell-text")[i])
    print("i:"+str(i))
    print('省市:'+a)
    if len(a)<=1:
        driver.execute_script("window.scrollBy(0,200)")
        sleep(10)
    #     # driver.find_element_by_class_name("hc-current-city").click()
    #     driver.execute_script("arguments[0].click();", driver.find_element_by_class_name("hc-current-city"))
    #     sleep(3)
    #     driver.find_element_by_class_name("hc-current-region").click()
    #     try:
    #         sleep(6)
    #         a = driver.find_elements_by_class_name("mint-cell-text")[i].text
    #         driver.find_elements_by_class_name("mint-cell-text")[i].click()
    #
    #     except:
    #         sleep(8)
    #         a = driver.find_elements_by_class_name("mint-cell-text")[i].text
    #         driver.find_elements_by_class_name("mint-cell-text")[i].click()
        # print("driver.page_source"+str(driver.page_source))

    for j in range(k, hc_region_items_length):
        # print("j:"+str(j))
        # print("hc_region_items[2].is_displayed():" + str(hc_region_items[2].is_displayed()))
        # print("hc_region_items[3].is_displayed():" + str(hc_region_items[3].is_displayed()))
        # print("hc_region_items[4].is_displayed():" + str(hc_region_items[4].is_displayed()))
        # print("hc_region_items[3].is_enabled():" + str(hc_region_items[3].is_enabled()))
        # print("hc_region_items[4].is_enabled():" + str(hc_region_items[4].is_enabled()))
        # print("hc_region_items[j].is_displayed():"+str(hc_region_items[j].is_displayed()))
        if driver.find_elements_by_class_name("hc-region-item")[j].is_displayed():
            print('driver.find_elements_by_class_name("hc-region-item")[j].text:'+driver.find_elements_by_class_name("hc-region-item")[j].text)
            sleep(1)
            try:
                driver.find_elements_by_class_name("hc-region-item")[j].click()
            except:
                driver.execute_script("window.scrollBy(0,400)")
                driver.execute_script("arguments[0].click();", driver.find_elements_by_class_name("hc-region-item")[j])
            sleep(5)
            #---存储信息----#
            # soup = BeautifulSoup(driver.page_source, 'lxml')
            # print('soup:' + str(soup))
            # input_result_list = soup.select('input.setting-input ')
            # print("input_result_list: ", input_result_list)
            if ("确定" in driver.find_element_by_class_name("hc-message-btn").text):
                driver.find_element_by_class_name("hc-message-btn").click()
                sleep(3)
            else:
                for n in range (0, len(driver.find_elements_by_class_name("hc-main-stoer-name"))):
                    shop_name=driver.find_elements_by_class_name("hc-main-stoer-name")[n].text.split(" ")[0]
                    print("shop_name:"+shop_name)
                    shop_iphone=driver.find_elements_by_class_name("hc-main-sub-text")[3*n+0].text
                    print("shop_iphone:"+shop_iphone)
                    shop_location=driver.find_elements_by_class_name("hc-main-sub-text")[3*n+1].text
                    print("shop_location："+shop_location)
                    sql_param_info = 'insert into shop_info (shop_name,shop_iphone,shop_location) values ("%s","%s","%s");' % (
                    shop_name, shop_iphone, shop_location)
                    # SqlUtil(host=host, port=port, user=user, passwd=passwd, db=db).execu_sql(cursor, sql_param_info)
                    # conn.commit()
                # shop_business_hour=driver.find_elements_by_class_name("hc-main-sub-text")[2].text
                # print("shop_business_hour：" + shop_business_hour)
                # ---存储信息----#
                sleep(3)
                try:
                    driver.find_element_by_class_name("hc-current-region").click()
                except:
                    sleep(7)
                    driver.execute_script("window.scrollBy(0,400)")
                    driver.execute_script("arguments[0].click();", driver.find_element_by_class_name("hc-current-region"))
                    # driver.find_element_by_class_name("hc-current-region").click()
                sleep(4)
            # mint_cell_texts[i].click()
sleep(20)
#将mysql中的数据导入到excel表中
