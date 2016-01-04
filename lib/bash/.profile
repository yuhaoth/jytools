
HOST=`hostname`
if [ x${HOST}x = xdroid04x ]
then
    _byobu_sourced=1 . /usr/bin/byobu-launch
fi
