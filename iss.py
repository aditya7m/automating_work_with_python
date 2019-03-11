import requests
parameters = {"lat": 28.629801, "lon":77.371872}
response = requests.get("http://api.open-notify.org/iss-pass.json",params=parameters)
print(response.content.decode("utf-8"))
