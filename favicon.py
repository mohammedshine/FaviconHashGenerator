import mmh3
import requests
import codecs

val = input("Enter your value: ")
response = requests.get(val)
favicon = codecs.encode(response.content,"base64")
hash = mmh3.hash(favicon)
print("Shodan Dork: http.favicon.hash:"+str(hash))
