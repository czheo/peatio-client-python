# coding: utf-8
from peatio_client import Client

# access public apis
client = Client()

print(client.get_public("/api/v2/markets.json"))
print(client.get_public("/api/v2/depth.json", params={
    "market": "btccny"
}))

# access secret apis
client = Client(
    access_key="your access key",
    secret_key="your secret key"
)

print(client.get("/api/v2/members/me.json"))
