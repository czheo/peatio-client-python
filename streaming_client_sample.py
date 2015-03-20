from peatio_client import StreamingClient

sc = StreamingClient(
    access_key = "your access key",
    secret_key = "your secret key"
)

def on_message(msg):
    print(msg)

sc.run(on_message)
