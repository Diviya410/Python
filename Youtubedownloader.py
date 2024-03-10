import pytube

link = input('Paste the url here:')


video = pytube.YouTube(link)


video.streams.first().download("YouTube Video")


print("Download Succesfully,",link)