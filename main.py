import os
from sys import argv,exit
from downloader import Downloader


def main():
    d = Downloader()

    if len(argv) <= 2:
        print(d)
        return -1
    elif not os.path.exists( argv[1] ):
        print("Path given does not exist!")
        return -1

    # single url:
    if len(argv[2:]) == 1:
        d.download_mp3(argv[1] ,  [ argv[2] ] )
    # multiple urls
    else:
        d.download_mp3(argv[1] , tuple( argv[2:] ) )


if __name__ == '__main__':
    exit(main())

