# rsyncのエイリアス
rsyncbbg='(){rsync -avcz debian@192.168.6.2:~/$1 $2}'
rsyncbbgs='(){rsync -avcz $1 debian@192.168.6.2:~/$2}'

