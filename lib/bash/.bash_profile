# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi

# User specific environment and startup programs

PATH=$HOME/bin:$PATH

export PATH

HOST=`hostname`
if [ x${HOST}x = xdroid04x ]
then
    _byobu_sourced=1 . /usr/bin/byobu-launch
fi
