#!/usr/bin/env bash
SOURCE_DIR=`dirname $BASH_SOURCE`
for i in ${SOURCE_DIR}/setup.d/*.sh
do
    echo EXE $i
    . $i
done
