class Song:

    count = 0
    genres = ["Rap", "Pop", "Rock"]
    artists = ["Jay Z", "Beyonce", "Nirvana", "Hall and Oates"]
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        if genre not in Song.genre_count:
            Song.genre_count[genre] = 1
        else:
            Song.genre_count[genre] += 1
        if artist not in Song.artist_count:
            Song.artist_count[artist] = 1
        else:
            Song.artist_count[artist] += 1