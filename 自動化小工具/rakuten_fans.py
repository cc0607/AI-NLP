#!/usr/bin/env python
# coding: utf-8

# In[3]:


#不用直接寫入帳號密碼
#以 coofrom selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import Bykies 


# In[4]:


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# In[5]:


from selenium import webdriver
from time import sleep


# In[57]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# In[58]:


import requests
from bs4 import BeautifulSoup

url = "https://ayutrend.com/rakuten-girl-ig/"
response = requests.get(url)
bs = BeautifulSoup(response.text, "html.parser")
#print(bs)
results = bs.find_all("tr")
url = []
names=[]
for result in results:
    r = result.find('a')
    if(r!=None):
        print(r.text)
        print(r.get('href'))
        names.append(r.text)
        url.append(r.get('href'))


# In[59]:


print(names)


# In[63]:


url[1]='https://www.instagram.com/le_dahye/'


# In[44]:


import json

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.instagram.com/')


# In[45]:


import json

if __name__ == '__main__':
    with open('login_cookies.json') as f:
        cookies = json.load(f)
    driver = webdriver.Chrome()
    driver.get('https://www.instagram.com/')

    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()


# In[46]:


# ------ 不開啟通知 ------


# ------ 網頁元素定位 ------ 
#XPATH會變，改用class name
notification_click = driver.find_elements(By.CLASS_NAME,'_a9--._a9_1')[0]

#//*[@id="mount_0_0_P4"]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]
# ------ 點擊不開啟通知 ------
notification_click.click()

print("Log in!")

#登入完成


# In[64]:


for i in range(len(url)):
    driver.get(url[i])
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//ul/li[2]/a/span/span"))
    )
    fan = driver.find_elements(By.XPATH,"//ul/li[2]/a/span/span")[0]
    print(names[i])
    print(fan.text)

