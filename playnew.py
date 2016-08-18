import subprocess
import random
with open("/home/pi/projs/player/playlist.txt", "r") as ins:
    array = []
    for line in ins:
        #print line
        array.append(line)
while True:
    playlist = random.choice(array)
    print playlist
    p = subprocess.Popen('/home/pi/projs/player/createplaylist.sh %s' % playlist, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print(line)
    retval = p.wait()

    songs_array=[]
    #If not present create it
    with open("/home/pi/projs/player/temp", "r") as ins:
        for line in ins:
	    line=line.rstrip('\n')
            print line
            songs_array.append(line)

    for song in songs_array:
        print 'playing song : %s' % song
        print 'mpv --no-video `youtube-dl -g \'https://www.youtube.com/watch?v=%s\'`' % song
        #p = subprocess.Popen('mpv --no-video "$(yturl https://www.youtube.com/watch?v=%s)"' % song, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        p = subprocess.Popen('mpv --no-video `youtube-dl -g \'https://www.youtube.com/watch?v=%s\'`' % song, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line)
    retval = p.wait()
