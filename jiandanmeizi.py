__author__ = "Bob"
import os
from bs4 import BeautifulSoup
import requests

headers={'referer':'http://jandan.net/', 'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'}

# name          :   save_imgs
# function      :   1) extract all the pictures from the parm res_url
#                   2) save all pictures under different folder (folder name = page #)
# parm          :   url which contains pictures (http://jandan.net/ooxx/page-2388#comments)
# changed date  :   2017-03-11
# changed by    :   Bob
def save_imgs(res_url):

    html = BeautifulSoup(requests.get(res_url, headers=headers).text,"html.parser")
    for link in html.find_all('a', {'class': 'view_img_link'}):
        strURL = "http:" + link.get('href')
        strFileName = link.get('href').split('/')[-1]
        
        #Check if file already exists. If YES, skip download
        if os.path.exists(strFileName):
            print ("File already exists: " + strFileName)
            iter
        
        with open(strFileName,'wb') as jpg:
            try:
                jpg.write(requests.get(strURL).content)
                jpg.close()
            except:
                print("FileExistsError, existing image overrided!")
                jpg.close()

# name          :   download_mm
# function      :   1) main funtion to process the download reqeust
#                   2) called by __main__
# parm          :   folder: folder name
#                   pages:  total pages to be extracted 
# changed date  :   2017-03-11
# changed by    :   Bob
def download_mm(folder='ooxx',pages=10):
    try:
        os.mkdir(folder) #create folder
    except FileExistsError:
        print ("Folder already exists: " + folder)

    os.chdir(folder) #Change current working folder
    folder_top = os.getcwd() #Get current folder path
    url = 'http://jandan.net/ooxx/'

    for i in range(pages):

        print ("================== Downing OOXX " + str(i+1) + "/" + str(pages) + " pages")
        save_imgs(url)
        url = BeautifulSoup(requests.get(url, headers=headers).text,"html.parser").find('a', {'class': 'previous-comment-page'}).get('href')

# name          :   __main__
# function      :   1) program entry
#                   2) Spider for JianDan.NET and save the pictures on user's requested folder
#                   3) By default folder name is "ooxx" and page number is 10
# parm          :   N/A
# input         :   folder name & page number
# changed date  :   2017-03-11
# changed by    :   Bob
if __name__ == '__main__':
    folder = input ("Please enter a folder (by default 'ooxx'): ")
    pages = input ("How many pages do you wan to download (by default 10): ")
    if folder == '':
        folder = "ooxx"
    if pages == '':
        pages = 10

    print ("================== Download in progress ==================")
    download_mm(str(folder),int(pages))
    print ("================== Download completed! ==================")