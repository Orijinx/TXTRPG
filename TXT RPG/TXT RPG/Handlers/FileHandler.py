from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

dir = r'C:\Users\Acer\Documents\TXTRPG\TXT RPG\TXT RPG'

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        print (event)

    def on_deleted(self, event):
        print( event)

    def on_moved(self, event):
        print (event)

    def on_modify(self,event):
        print(event)


observer = Observer()
observer.schedule(Handler(), path=r'C:\Users\Acer\Documents\TXTRPG\TXT RPG\TXT RPG', recursive=True)
observer.start()
