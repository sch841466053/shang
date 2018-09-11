from suds.client import Client
url = "http://127.0.0.1:8000/?wsdl"
client = Client(url)
result = client.service.say_hello("洪哥", 10)
print(result)