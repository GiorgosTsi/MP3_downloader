#!/bin/bash

function help_menu()
{
    echo "********************* MP3 DOWNLOADER HELP MENU *********************"
    echo ""
    echo "-f option for declaring the folder to download the songs"
    echo "-u option for declaring the file which contains the urls to download"
    echo ""
    echo "********************************************************************"

}

function main()
{
    ## $1  -> folder to save the songs
    ## $2  -> file to read the urls
    
    while read -r url
    do
        python3 main.py $1 "${url}"
    done < $2
}

## check for help option:
if [ "$1" == "-h" ]
then
    help_menu

## continue with the commands
elif [ "$#" -lt 4 ]
then
    echo "Missing parameters!"
    help_menu

elif [ "$1" != "-f" ] || [ "$3" != "-u" ] 
then
    echo "Wrong options given!"
    help_menu

elif [ ! -d "$2" ] || [ ! -e "$4" ] ## check file and directory existance
then
    echo "Files given dont exist!"

else
    main "$2" "$4"
fi

