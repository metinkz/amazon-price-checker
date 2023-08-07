from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

USER = "username@gmail.com"
PASSWORD="password"
server = smtplib.SMTP("smtp.gmail.com", 587, timeout=120 )
server.starttls()
server.login(USER, PASSWORD)

BUY_PRICE = 1.650

headers = {
    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"    
}

response = requests.get("https://www.amazon.com.tr/Dune-Kutu-Kitap-Tak%C4%B1m-Ciltli/dp/625773763X/ref=sr_1_6_mod_primary_new?__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3J4LPRT0OLRMO&keywords=dune&qid=1691299993&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sprefix=dune%2Caps%2C127&sr=8-6", headers=headers)
website = response.text

soup = BeautifulSoup(website, "lxml")

title = soup.find(name="span", class_="a-size-extra-large celwidget").getText().strip()

price = soup.find(name="span", class_="a-offscreen").getText().split("TL")[0].split(",")
price.pop(1)
price_float = float(price[0])

mail = f"{title} ürününün fiyatı düştü. Şu anki fiyatı {price_float}.".encode("utf-8")

if BUY_PRICE >= price_float:
    #server.sendmail(USER,USER,mail)
    print(f"{title} ürününün fiyatı düştü. Şu anki fiyatı {price_float}.")
server.quit()
