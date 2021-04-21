import os
import time

from selenium import webdriver


project_dir=os.path.join(os.getcwd(),"..")
chromedriver_dir=os.path.join(project_dir,'Chromedriver')
print("project_dir:"+project_dir)
print("chromedriver_dir:"+chromedriver_dir)

#chromedriver设置
chrome_path = os.path.join(chromedriver_dir,'chromedriver_'+'89')
print("chrome_path:",chrome_path)
chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_argument('--no--sandbox')
driver = webdriver.Chrome(executable_path=chrome_path, desired_capabilities=chrome_opt.to_capabilities())

url = "https://map.baidu.com/search/%E6%B3%B0%E5%B1%B1%E5%8E%9F%E6%B5%86/@12950826.39,4820435,11z?querytype=s&da_src=shareurl&wd=%E6%B3%B0%E5%B1%B1%E5%8E%9F%E6%B5%86&c=131&src=0&pn=0&sug=0&l=11&b=(12831543.837819671,4802640.952786885;13030601.309295082,4893875.627213115)&from=webmap&biz_forward=%7B%22scaler%22:2,%22styles%22:%22pl%22%7D&seckey=1c7e316a4540e50ac95e9230bec47dbcb80e3ae5bb6a5e50a29d1f9face80bde809c0809b62dc348fb8e9375c542f12cea0f3973b2f8374a4ee078076449048d18aef843c8855ee0c428e1f1d5a5075f27485b02b1ef2b7ed769e4be768edd52a3dfdf4d02ff1ab9892680ff3dd237685205f6086112e74057bc181fbe811250bebdb892c21f3f4320307ac8a38d3103e50363a2cc15d658bded79c8b41ff885f12f9d9fa54ef7a3ee92f42f91c648920fb3cbfca71ecb099d135df5110f4deda71b2c5c780f2aa256437bbf731f2e5023ddc0ae424d0956dadcdfb8e0e4cc9d5764eb9b1385b902e4b0c8d9a6e0b8d0&device_ratio=2https://map.baidu.com/search/%E6%B3%B0%E5%B1%B1%E5%8E%9F%E6%B5%86/@12950826.39,4820435,11z?querytype=s&da_src=shareurl&wd=%E6%B3%B0%E5%B1%B1%E5%8E%9F%E6%B5%86&c=131&src=0&pn=0&sug=0&l=11&b=(12831543.837819671,4802640.952786885;13030601.309295082,4893875.627213115)&from=webmap&biz_forward=%7B%22scaler%22:2,%22styles%22:%22pl%22%7D&seckey=1c7e316a4540e50ac95e9230bec47dbcb80e3ae5bb6a5e50a29d1f9face80bde809c0809b62dc348fb8e9375c542f12cea0f3973b2f8374a4ee078076449048d18aef843c8855ee0c428e1f1d5a5075f27485b02b1ef2b7ed769e4be768edd52a3dfdf4d02ff1ab9892680ff3dd237685205f6086112e74057bc181fbe811250bebdb892c21f3f4320307ac8a38d3103e50363a2cc15d658bded79c8b41ff885f12f9d9fa54ef7a3ee92f42f91c648920fb3cbfca71ecb099d135df5110f4deda71b2c5c780f2aa256437bbf731f2e5023ddc0ae424d0956dadcdfb8e0e4cc9d5764eb9b1385b902e4b0c8d9a6e0b8d0&device_ratio=2"
driver.get(url)
time.sleep(5)
store_name_length = 0

def get_store_info(index=0):
    temp_store_name = driver.find_elements_by_class_name('n-blue')[index].text
    print(temp_store_name)
    try:
        temp_store_addr = driver.find_elements_by_class_name('n-grey')[index].text
        print(temp_store_addr)
    except Exception as e:
        print('no address\n')
    try:
        xpath_name=f'//*[@id="card-1"]/div/ul/lia[{index+1}]/div[1]/div[3]/div[3]'
        print("xpath_name:",xpath_name)
        temp_store_tel = driver.find_element_by_xpath(xpath_name).text
        print("temp_store_tel:",temp_store_tel)
        temp_store_tel = temp_store_tel.split(":")[-1]
        print(temp_store_tel)
    except:
        print('no tel\n')

num=0
while store_name_length==0  and  num<5:
    num=num+1

    store_name_length=len(driver.find_elements_by_class_name('n-blue'))
    print('stroe_name_length:',store_name_length)
    for i in range(0,store_name_length):
        get_store_info(i)

    time.sleep(5)