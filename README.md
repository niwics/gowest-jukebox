# gowest-jukebox
Jukebox app for your party!
- simple song selection from your mp3
- unclearable song queue is the main feature

## Installation requrements
- Python >= 2.7
- wxPython >= 3.0
- hsaudiotag library >= 1.1.1 for reading songs tags (installation via pypi - https://pypi.python.org/pypi/hsaudiotag)
- Pygame library >= 1.9 for playing songs (installation packages available on http://pygame.org/download.shtml)

## How does it work?
- select the folder with your music in Application > Settings dialog
- button Scan in dialog will start to fetch all your song to your music collection
- all songs from your collection will be listed on the right panel in the main window
- use Up and Down keys to move on songs in your collection
- hit Enter or Space key to add the song to the queue and play it
- the queue is limited to 3 songs only - you cannot add more songs to play - you have to wait to finish songs if you want add another
- currently played song is not stoppable - yes, it is the feature!:)

## TODO
- more items in the queue
- clearing the queue after the songs are finished
