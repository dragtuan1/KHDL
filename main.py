#Import libraries
from GoogleImageScrapper import GoogleImageScraper
import os

#Define file path
webdriver_path = os.path.normpath(os.getcwd()+"\\webdriver\\chromedriver.exe")
image_path = os.path.normpath(os.getcwd()+"\\photos")

#Add new search key into array ["cat","t-shirt","apple","orange","pear","fish"]
# search_keys= ["bà nà hils","asia park","Bảo tàng 3D TrickEye","Bãi biển Mỹ Khê","Bãi tắm Phạm Văn Đồng"
#             ,"Tượng cá chép hóa rồng","Cù Lao Chàm","Bán đảo Sơn Trà","Chùa Linh Ứng","Đỉnh Bàn Cờ","Hải đăng Tiên Sa"
#             ,"Bãi tắm Non nước","Ngũ Hành Sơn","Cầu Rồng","Cầu Quay sông Hàn","Phố Cổ Hội An","Cầu tàu tình yêu"]
search_keys= ["Tượng cá chép hóa rồng Đà Nẵng"]
#Parameters
number_of_images = 50
headless = False
min_resolution=(0,0)
max_resolution=(1000,1000)

#Main program
for search_key in search_keys:
    image_scrapper = GoogleImageScraper(webdriver_path,image_path,search_key,number_of_images,headless,min_resolution,max_resolution)
    image_urls = image_scrapper.find_image_urls()
    image_scrapper.save_images(image_urls)