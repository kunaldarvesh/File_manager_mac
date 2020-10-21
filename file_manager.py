#!/usr/bin/python3

from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json


class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            print(src)
            try:
                file_form = filename.split('.')
            except:
                print("Not proper format")
            print(file_form[1])
            if 'pdf' == file_form[1]:
                destination = folder_destination_1 + "/" + filename
            elif 'WhatsApp' in filename:
                destination = folder_destination_2 + "/" + filename
            elif 'xlsx' == file_form[1]:
                destination = folder_destination_3 + "/" + filename
            elif 'jpg' == file_form[1] or 'jpeg' == file_form[1]:
                destination = folder_destination_4 + "/" + filename
            elif 'png' == file_form[1]:
                destination = folder_destination_5 + "/" + filename
            elif 'docx' == file_form[1]:
                destination = folder_destination_6 + "/" + filename
            elif 'mp4' == file_form[1] or 'avi' == file_form[1] or 'mov' == file_form[1]:
                destination = folder_destination_7 + "/" + filename
            elif 'pptx' == file_form[1] or 'ppt' == file_form[1]:
                destination = folder_destination_8 + "/" + filename
            elif 'dmg' in file_form:
                destination = folder_destination_9 + "/" + filename
            else:
                destination = folder_destination_x + "/" + filename
            print(destination)
            os.rename(src, destination)

folder_to_track = '/Users/<username>/Downloads'
folder_destination_1 = '/Users/<username>/Desktop/sorted_downloads/PDFs'
folder_destination_2 = '/Users/<username>/Desktop/sorted_downloads/WhatsApp'
folder_destination_3 = '/Users/<username>/Desktop/sorted_downloads/Excel'
folder_destination_4 = '/Users/<username>/Desktop/sorted_downloads/Images/jpegs'
folder_destination_5 = '/Users/<username>/Desktop/sorted_downloads/Images/png'
folder_destination_6 = '/Users/<username>/Desktop/sorted_downloads/Word_docs'
folder_destination_7 = '/Users/<username>/Desktop/sorted_downloads/vids'
folder_destination_8 = '/Users/<username>/Desktop/sorted_downloads/ppts'
folder_destination_9 = '/Users/<username>/Desktop/sorted_downloads/Software'
folder_destination_x = '/Users/<username>/Desktop/sorted_downloads/To_be_sorted'

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()


try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
    quit()
observer.join()
