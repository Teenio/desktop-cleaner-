import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source_folder = r"C:\Users\eteun\Downloads"  # Change this to your downloads path
photo_destination = r"C:\Users\eteun\OneDrive\Afbeeldingen\Mia Mia images"  # Change this to your desired photo destination
video_destination = r"C:\Users\eteun\OneDrive\Afbeeldingen\mia Dance videos"  # Change this to your desired video destination

time.sleep(1)  # Wait for the file to be fully created

os.makedirs(photo_destination, exist_ok=True)
os.makedirs(video_destination, exist_ok=True)

class DesktopCleanerHandler(FileSystemEventHandler):
    def check_and_moved(self, file_path):
        filename = os.path.basename(file_path)
        time.sleep(1)  # Wait for the file to be fully created

        if not os.path.exists(file_path):
            return  # File does not exist, skip processing

        if filename.lower().endswith(('.jpg', 'png', 'jpeg')):
            try:
                shutil.move(file_path, os.path.join(photo_destination, filename))
                print(f"Moved photo: {filename} to {photo_destination}")
            except Exception as e:
                print(f"Error occurred while moving photo {filename}: {e}")


        elif filename.lower().endswith(('mp4')):
            try:
                shutil.move(file_path, os.path.join(video_destination, filename))
                print(f"Moved video: {filename} to {video_destination}")
            except Exception as e:
                print(f"Error occurred while moving video {filename}: {e}")

    def on_moved(self, event):
        if not event.is_directory:
            self.check_and_moved(event.dest_path)

    def on_created(self, event):
        if not event.is_directory:
            self.check_and_moved(event.src_path)


    
if __name__ == "__main__":
    event_handler = DesktopCleanerHandler()
    observer = Observer()
    observer.schedule(event_handler, source_folder, recursive=False)
    observer.start()
    print(f"Monitoring {source_folder} for new files...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

