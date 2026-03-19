def get_filename(path):
    return path.split("\\")[-1]

def get_song_name(path):
    filename = get_filename(path)
    return filename.rsplit(".", 1)[0]


path = "d:\\music\\muabui.mp3"

print(get_filename(path))
print(get_song_name(path))