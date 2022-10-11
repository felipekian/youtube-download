import youtube_dl

links = ['https://sdsds', 'https://sdsds2']

with youtube_dl.YouttubeDL() as ydl:
  ydl.download(links)