import json
from channels.generic.websocket import WebsocketConsumer
import time


class ScanProgressConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data = json.loads(text_data)
        device = data['device']
        file_type = data['file_type']

        # Simulate scan progress
        for progress in range(1, 101):
            time.sleep(0.1)  # Simulating time-consuming task
            self.send(text_data=json.dumps({
                'progress': progress
            }))
