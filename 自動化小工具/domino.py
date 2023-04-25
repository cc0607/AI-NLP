#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#達美樂99pizza
#尚未針對響應式進行調整


# In[58]:


from selenium import webdriver
driver = webdriver.Chrome('chromedriver')
driver.get('https://www.dominos.com.tw/Alliances/MYBOX99-20230420?utm_source=facebook&utm_medium=post-ads&utm_campaign=mybox-2&fbclid=IwAR2uG1PxkiCx4a3Zpbnn5oAgBQ3MPKinWTGwAUOT1rb4cH6hlClDxI7dVow')


# In[59]:


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# In[60]:


driver.find_element(By.XPATH,"//a[@class='btn btn-primary s']").click()


# In[61]:


driver.find_element(By.XPATH,'//*[@id="County"]/option[3]').click()


# In[62]:


try:
    driver.find_element(By.XPATH,'//*[@id="js-carryout-store-list"]/div[11]//button').click()
except:
    print('sold-out')


# In[63]:


phone_input = driver.find_elements(By.NAME,'Mobile')[0]
phone_input.send_keys('您的手機號碼')


# In[64]:


#勾選不註冊
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/form/section/div/div/div/div[6]/div/div/label'))).click()


# In[65]:


WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/form/section/div/div/div/div[7]/div/button'))).click()


# In[66]:


WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='col-lg-5']//input"))).click()


# In[67]:


#可能出現'請選擇餐點'
try:
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-popup-notice"]/div/div/div/div[3]/div/div/div/button'))).click()
except:
    pass


# In[68]:


WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product-content"]/div/div/div/div[3]/div/div[2]/div[1]/div/a/div/div/div/div[2]'))).click()


# In[69]:


#選pizza->海鮮
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="modal-pizzaflavors-content"]/div/div/div/div[1]/a/div/div/div[1]/div[1]/div/img'))).click()


# In[71]:


#進入選餅皮
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="modal-pizzaflavors-content"]/div/div/div/div[1]/a/div/div/div[1]/div[1]/div/img'))).click()


# In[76]:


#選餅皮
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="modal-pizzacrusts-content"]/div/div/div/div[2]/a/div/div/div[1]/div[1]/div/img'))).click()


# In[77]:


#選點心1
#要先滑到點心欄
first_dessert_target = driver.find_elements(By.XPATH,'//*[@id="product-content"]/div/div/div/div[5]/div/div[2]/div[2]/a/div[1]/div')
#driver.execute_script("arguments[0].scrollIntoView();",first_dessert_target)
first_dessert_target[0].location_once_scrolled_into_view


# In[78]:


WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="product-content"]/div/div/div/div[5]/div/div[2]/div[3]/a/div[1]/div'))).click()


# In[83]:


#選點心2
#要先滑到點心欄
second_dessert_target = driver.find_elements(By.XPATH,'//*[@id="product-content"]/div/div/div/div[5]/div/div[2]')
second_dessert_target[0].location_once_scrolled_into_view


# In[84]:


WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="product-content"]/div/div/div/div[7]/div/div[2]/div[2]/a/div[1]/div'))).click()


# In[85]:


#新增餐點
x_path='//*[@id="product-action"]/div/div/div/input'
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,x_path))).click()


# In[ ]:


#結帳
x_path = '//*[@id="nav-mobile"]/div/div[1]/div[3]/a'
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,x_path))).click()

