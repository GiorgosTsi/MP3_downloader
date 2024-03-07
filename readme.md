
# MP3 Downloader 

## Overview

The MP3 Downloader is a Bash script designed to download MP3 songs from URLs provided in a text file. This documentation provides information on how to use the script, its options, and functionality.

## Table of Contents

- [Dependencies](#Dependencies)
- [Installation](#installation)
- [Usage](#usage)

## Dependencies

This script requires the pytube packet.The requrements have been listed in the requirements.txt file.You can ideally run it in a python virtualenv.

```bash
pip install -r requirments.txt
```

## Installation

To install the MP3 Downloader script, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/GiorgosTsi/mp3_downloader.git
    ```

2. Navigate to the project directory:

    ```bash
    cd mp3_downloader
    ```

3. Make the script executable:

    ```bash
    chmod +x mp3_downloader.sh
    ```

## Usage

To use the MP3 Downloader script, execute it from the command line with the appropriate options:

```bash
./mp3_downloader.sh -f <folder_path> -u <url_list_file>
```

Example:

```bash
./mp3_downloader.sh -f /home/giwrghs/Music -u songs.txt
```

Use option -h to show the help menu:
```bash
./mp3_downloader.sh -h
```


You can also run it from the python module main.py by providing the folder and the urls as command line args.

```bash
python3 main.py <folder_path> <urls>
```
