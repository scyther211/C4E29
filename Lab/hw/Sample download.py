from youtube_dl import YoutubeDL

# dl = YoutubeDL()
# dl.download(['https://www.youtube.com/watch?v=KDGfAYD7R0o'])

# options = {
#     'format': 'bestaudio/audio' # Tell the downloader to download only the best quality of audio
# }
# dl = YoutubeDL(options)
# dl.download(['https://www.youtube.com/watch?v=KDGfAYD7R0o'])

options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1, # Tell downloader to download only the first entry (audio)
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['Yêu như ngày hôm qua the sheep'])