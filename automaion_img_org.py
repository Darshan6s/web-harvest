from selenium import webdriver as wr
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 
import requests
import io
from PIL import Image

search_name=str(input("enter the search iteam:"))
driver = wr.Firefox()
images =[]
image_store=[]
def finder(driver, max_size, delay):
    def scroll_down(driver):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(delay)
        
    driver.get("https://www.google.com/")
    search = driver.find_element(By.NAME, "q")
    search.send_keys(search_name)
    search.send_keys(Keys.ENTER)
    time.sleep(1)
    end=0
    click_image = driver.find_element(By.XPATH, "/html/body/div[5]/div/div[4]/div/div/div[1]/div/div/div[1]/div/div/div[1]/a[1]/div/span")
    click_image.click()
    print("successfully")
    time.sleep(3)
    while len(images)+end < max_size:  
        print("images",len(images))
        scroll_down(driver)
        photos_finder = driver.find_elements(By.CLASS_NAME, "Q4LuWd")
        print("photos_finder",len(photos_finder))
       
        for img in photos_finder[0:max_size]:
            print("img;louytredfgerhtjuashnc")
            img.click() 
            time.sleep(delay)
            image = driver.find_element(By.XPATH, '/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]') 
            image_store.append(image.get_attribute("src"))
        print("sgsdgrsgthrehr",len(image_store))
        for i in image_store:
            images.append(i)
            end+=1
        print(len(images))    
    return images


def download_image(download_path, url, filename):
    try:
        img_content = requests.get(url).content
        image_bt=io.BytesIO(img_content)
        image=Image.open(image_bt)
        file_path=download_path+filename
        with open(file_path,"wb") as f:
            image.save(f,"PNG")
            print("success")    
    except(Exception):
        print(Exception)

urls = finder(driver, 18, 1)
print("jeiot",len(urls))
count=0
for url in urls:  
    print(count)
    download_image("F:",url, str(count)+ ".png")
    count+=1

driver.quit()


