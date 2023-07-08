import urllib.request

url = input("link giriniz")

urllib.request.urlretrieve(url, "resim.jpg")
