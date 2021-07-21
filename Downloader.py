from pytube import YouTube

link = input("Enter link\n")
yt = YouTube(link) 

ys=yt.streams.get_highest_resolution()

print('Downloading....')

ys.download('Downloads/')

print('Download Complete')
