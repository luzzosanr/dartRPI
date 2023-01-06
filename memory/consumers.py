from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        print('connected')

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        print(text_data)
        self.send(text_data='Hello from Django!')