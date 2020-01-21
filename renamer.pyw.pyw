#%%
import os, requests, bs4, sys
from tkinter import *

url = None

proxies = {
 "http": "http://dishendra:Strings7@172.16.0.1:3128",
 "https": "http://dishendra:Strings7@172.16.0.1:3128",
}

def get_youtube_link():
    root = Tk()
    root.title("Videos Renamer")
    
    label = Label(root, text="Playlist Link",font=("Calibri 12"),fg="red")
    label.pack( side = LEFT,padx=2)
    
    entry = Entry(root, bd =2,width=100,font=("Calibri 12"))
    entry.pack(side = RIGHT,padx=2,pady=5)

    def get_url(event):
        global url
        url = entry.get()
        root.quit()
        
    root.bind('<Return>', get_url)
    root.mainloop()

get_youtube_link()
print("Link: ",url)

con = requests.request("GET",url,proxies=proxies).text
# con = open("main.html","r").read()

soup = bs4.BeautifulSoup(con, 'html.parser')
matches = soup.find_all("tr",class_="pl-video yt-uix-tile")

titles = [i["data-title"] for i in matches]

log = open("log.txt","w")

prefix = 1
for title in titles:
    try:
        os.rename(title+".mp4",str(prefix)+". "+title+".mp4")
        log.write("Renamed: "+title+"\n")
    except:
        log.write("Not Found!: "+title+".mp4\n")
        print("Not Found!: ",title+".mp4")
    prefix += 1

log.close()
os.system("start log.txt")

# for i in range(10):