from pytube import YouTube
url = "https://www.youtube.com/watch?v=FExoHW7_noE"




def progress_function(chunk, file_handle, bytes_remaining):
    global filesize
    current = ((filesize - bytes_remaining)/filesize)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    print(f" ↳ |{status}| {percent}%")

yt = YouTube(url, on_progress_callback=progress_function)

stream = yt.streams.filter(progressive=True , res= "720p" )
filesize = stream.first().filesize


stream.first().download(filename="test.mp4")

