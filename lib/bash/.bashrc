# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi
if [ -d $HOME/.bashrc.d ]; then
  for i in $HOME/.bashrc.d/*; do
    if [ -r $i ]; then
      . $i
    fi
  done
  unset i
fi

alias ls='ls --color'
# User specific aliases and functions
