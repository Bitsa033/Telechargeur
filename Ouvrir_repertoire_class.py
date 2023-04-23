from tkinter import Entry
from tkinter import filedialog

""" def youtube():
    YouTube('https://youtu.be/2lAe1cqCOXo').streams.first().download()
    yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
    yt.streams
    yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

def downloader():
    _tkinter.TclError: failed to create color bitmap for "moncv.png"
    url = 'https://github.com/party98/Python-Parallel-Downloader/archive/master.zip'
    downloader = Downloader(url=url)
    if downloader.is_running:
        time.sleep(1)
    print('File downloaded to %s' % downloader.file_name) """
    

def ouvrir_repertoire(e:Entry):
    filename = filedialog.asksaveasfilename(initialdir="C:/Users/PascalBitsa/Downloads", title="Enregistrer sous",
    filetypes=(("mp4 files", "*.mp4"), ("mp3 files", "*.mp3"), ("all files", "*.*")))
    e.insert(0,filename)
    