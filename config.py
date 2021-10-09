python3 -m tgtlg
 
  - `TG_BOT_TOKEN`: 1948841770:AAGX5_t7-q0uodiq_U3XwI2qV7d80LFDASA
  - `APP_ID` 3495663
  - `API_HASH`: bd2c2a8c9fa3169038cdf3c9c8215f19
  - `AUTH_CHANNEL`: -1001585071628
  - `OWNER_ID`: 1874954413
  - `CLONE_COMMAND_G`: /gclone@Leech96bot
  - `UPLOAD_COMMAND`: /upload@Leech96bot
  - `RENEWME_COMMAND`: /leech@Leech96bot
  - `SAVE_THUMBNAIL`: /savethumb@Leech96bot
  - `CLEAR_THUMBNAIL`: /clearthumb@Leech96bot
  - `GET_SIZE_G`: /clearthumb@Leech96bot
  - `TOGGLE_VID`: /togglevid@Leech96bot
  - `TOGGLE_DOC`: /toggledoc@Leech96bot
  - `RENAME_COMMAND`: /rename@Leech96bot
  - `CANCEL_COMMAND_G`: /cancel@Leech96bot

  - `MAX_FILE_SIZE`:
  - `TG_MAX_FILE_SIZE`:
  - `FREE_USER_MAX_FILE_SIZE`
  - `MAX_TG_SPLIT_FILE_SIZE`:
  - `CHUNK_SIZE`:
  - `MAX_MESSAGE_LENGTH`:
  - `PROCESS_MAX_TIMEOUT`:
  - `ARIA_TWO_STARTED_PORT`:
  - `EDIT_SLEEP_TIME_OUT`:
  - `MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START`:
  - `FINISHED_PROGRESS_STR`:
  - `UN_FINISHED_PROGRESS_STR`:
  - `TG_OFFENSIVE_API`:
  - `CUSTOM_FILE_NAME`:

  - `UPLOAD_AS_DOC`: Takes two option True or False. If True file will be uploaded as document. This is for people who wants video files as document instead of streamable.

  - `INDEX_LINK`: (Without `/` at last of the link, otherwise u will get error) During creating index, plz fill `Default Root ID` with the id of your `DESTINATION_FOLDER` after creating. Otherwise index will not work properly.

  - `DESTINATION_FOLDER`: Name of your folder in your respective drive where you want to upload the files using the bot.

</details>

  ### Available Commands

  - `/rclone`: This will change your drive config on fly. (First one will be default)
  - `/gclone`: This command is used to clone gdrive files or folder using gclone.

  - `/help`: To get a list of commands

  - `/leech`: This command should be used as reply to a magnetic link, a torrent link, or a direct link. [this command will SPAM the chat and send the downloads a seperate files if there is more than one file, in the specified torrent]
  - `/archive`: This command should be used as reply to a magnetic link, a torrent link, or a direct link. [This command will create a .tar.gz file of the output directory, and send the files in the chat, splited into PARTS of 1024MiB each, due to Telegram limitations]
  - `/extract`: This will unarchive file and upload to telegram.

  - `/gleech`: This command should be used as reply to a magnetic link, a torrent link, or a direct link. And this will download the files from the given link or torrent and will upload to the cloud using rclone.
  - `/garchive`: This command will compress the folder/file and will upload to your cloud.
  - `/gextract`: This will unarchive file and upload to cloud.
  - `/gclone`: This command is used to clone gdrive files or folder using gclone.

Syntax: `[ID of the file or folder][one space][name of your folder only (If the ID is of file, don't put anything)]` and then reply /gclone to it.

  - `/tleech`: This will mirror the telegram files to your respective cloud.
  - `/textract`: This will unarchive telegram file and upload to cloud.

  - `/ytdl`: This command should be used as reply to a [supported link](https://ytdl-org.github.io/youtube-dl/supportedsites.html)
  - `/pytdl`: This command will download videos from youtube playlist link and will upload to telegram.
  - `/gytdl`: This will download and upload to your cloud.
  - `/gpytdl`: This download youtube playlist and upload to your cloud.
  - `/getsize`: This will give you total size of your destination folder in cloud.
  - `/renewme`: This will clear the remains of downloads which are not getting deleted after upload of the file or after /cancel command.
  - `/rename`: To rename the telegram files.

  - `/rclone`: This will change your drive config on fly. (First one will be default)
  - `/log`: This will send you a txt file of the logs.

Only works with direct link and youtube link for now.
You can add a custom name as it's prefix to the file. Example: if gk.txt uploaded will be what you add in CUSTOM_FILE_NAME + gk.txt

  You can add a custom name as it's prefix of the original file name.
  e.g: if file is `gk.txt` uploaded will be what you added in ``CUSTOM_FILE_NAME`` + ``gk.txt``
  It is like you can add custom name as prefix of the original file name.
  Like if your file name is `gk.txt` uploaded will be what u add in `CUSTOM_FILE_NAME` + `gk.txt`

  ## How to Use?

  * send any one of the available commands, as a reply to a valid link/magnet/torrent.


  ## Credits
  - [GautamKumar](https://github.com/gautamajay52/TorrentLeech-Gdrive)
  - [SpEcHiDe](https://github.com/SpEcHiDe/PublicLeech) for his wonderful code
  - [cihanvol](https://github.com/cihanvol) for [direct_link_generator](https://github.com/reaitten/tgtlg/blob/main/tgtlg/helper_funcs/direct_link_generator.py)
  - [MaxxRider](https://github.com/MaxxRider) for tweaked version of [TorrentLeech-Gdrive](https://github.com/MaxxRider/Leech-Pro)
  - [Rclone Team](https://rclone.org) for theirs awesome tool
  - [Dan Tès](https://telegram.dog/haskell) for his [Pyrogram Library](https://github.com/pyrogram/pyrogram)
  - [Robots](https://telegram.dog/Robots) for their [@UploadBot](https://telegram.dog/UploadBot)
  - [@AjeeshNair](https://telegram.dog/AjeeshNait) for his [torrent.ajee.sh](https://torrent.ajee.sh)
  - [@gotstc](https://telegram.dog/gotstc), @aryanvikash, [@HasibulKabir](https://telegram.dog/HasibulKabir) for their TORRENT groups

