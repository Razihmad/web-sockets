from channels.consumer import SyncConsumer

class ChatConsumer(SyncConsumer):
    def websocker_connect(self,event):
        print("Websocket connected",event)
    
    def websocket_recieve(self,event):
        print("recieved method is called")

    def websocket_disconnect(self,event):
        print("Websocket disconnected")
