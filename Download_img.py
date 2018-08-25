# downloading images from URL

import urllib

def dl_img(url, file_name,file_path):
    full_path = file_path + file_name +'.jpg'
    urllib.request.urlretrieve(url,full_path)


url = input('Enter the url :')
file_name = input("Enter the file name to be saved")

