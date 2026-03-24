import http.client

conn = http.client.HTTPSConnection("streaming-availability.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "3b3b0d5268mshb124e7d9881ba56p122ac9jsn27e4f05aeb82",
    'x-rapidapi-host': "streaming-availability.p.rapidapi.com"
}

conn.request("GET", "/shows/%7Btype%7D/%7Bid%7D", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))