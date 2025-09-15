# Week 2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# Music database: dictionary with string keys mapped to lists
music_database = {
    "genres": [
        "Rock", "Jazz", "Classical", "Hip Hop", 
        "Electronic", "Country", "R&B", "Pop"
    ],
    
    "artists": [
        "Radiohead (Rock)", "Miles Davis (Jazz)", 
        "Ludwig van Beethoven (Classical)", "Kendrick Lamar (Hip Hop)",
        "Daft Punk (Electronic)", "Johnny Cash (Country)",
        "Beyoncé (R&B)", "Taylor Swift (Pop)"
    ],
    
    "albums": [
        "OK Computer - Radiohead (1997)",
        "Kind of Blue - Miles Davis (1959)",
        "Symphony No. 9 - Beethoven (1824)",
        "To Pimp a Butterfly - Kendrick Lamar (2015)",
        "Random Access Memories - Daft Punk (2013)",
        "At Folsom Prison - Johnny Cash (1968)",
        "Lemonade - Beyoncé (2016)",
        "1989 - Taylor Swift (2014)"
    ],
    
    "songs": [
        "Paranoid Android - Radiohead (6:06)",
        "So What - Miles Davis (9:22)",
        "Ode to Joy - Beethoven (2:54)",
        "Alright - Kendrick Lamar (3:39)",
        "Get Lucky - Daft Punk (6:09)",
        "Folsom Prison Blues - Johnny Cash (2:51)",
        "Formation - Beyoncé (3:26)",
        "Shake It Off - Taylor Swift (3:39)"
    ],
    
    "instruments": [
        "Guitar (String)", "Piano (Keyboard)", "Drums (Percussion)",
        "Saxophone (Wind)", "Bass (String)", "Violin (String)",
        "Turntables (Electronic)", "Trumpet (Wind)"
    ]
}
# Pretty-print the data structure
pprint(music_database)