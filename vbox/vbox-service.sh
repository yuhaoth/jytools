#! /bin/sh
#
# chkconfig: 2345 90 10
### BEGIN INIT INFO
# Provides:          vbox-service-template
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: 'service-template' virtual machine
# Description:       Starts and stops a VirtualBox host as a service.
### END INIT INFO

# Author: Brendan Kidwell <brendan@glump.net>
# License: GPL 3 <http://opensource.org/licenses/GPL-3.0>
#
# Based on /etc/init.d/skeleton from Ubuntu 12.04.

#-------------------------------------------------------------------------------
#
#  CONFIGURATION
#
#  What is the name of the VM exactly as it appears in the VirtualBox control
#  panel? This is the 'name' and the 'long name' of the VM.
#
#     Does 'name' contain spaces or other special characters? If so, you must
#     make up some other value for 'name' that doesn't have spaces.
#
#  Setup:
#
#  1. Copy this file to /etc/init.d/vbox-'name'. The filename must start with
#     the prefix "vbox-". Make sure you set the 'x' bit on the file to make it
#     executable.
#
#  2. Edit 'Provides', above, to match the filename.
#
#  3. Edit 'Short-Description' to describe the function of the VM.
#
#  4. If 'long name' is different from 'name' fill it in below, otherwise leave
#     LONGNAME as an empty string.
      VM_LONG_NAME=""
#
#  5. What user owns the virtual machine?
      VM_OWNER=jerry.yu
#
#  6. Which stop command? "hibernate" or "powerbutton"
      VM_STOP=hibernate
#
#  7. For the 'start-wait' command -- waiting until network is up, what is the
#     VM's hostname?
      VM_HOSTNAME=""
#
#-------------------------------------------------------------------------------

# Do NOT "set -e"

# PATH should only include /usr/* if it runs after the mountnfs.sh script

PATH=/sbin:/usr/sbin:/bin:/usr/bin
# Pull DESC from file header

DESC=`grep --max-count=1 "^# Short-Description:" $(readlink -f $0)|cut --delimiter=' ' --field=3-|sed 's/^ *//'`
# Pull NAME from file header

#NAME=`grep --max-count=1 "^# Provides:" $(readlink -f $0)|cut --delimiter=' ' --field=3-|sed 's/^ *//'`
NAME=`basename $0`
echo $NAME
SCRIPTNAME=/etc/init.d/$NAME


MANAGE_CMD=VBoxManage

# Get VM_SHORT_NAME from service name

VM_SHORT_NAME=`echo $NAME|cut --delimiter='-' --field=2-`
#echo $NAME
# Actual filename of VM is VM_SHORT_NAME, or if VM_LONG_NAME is set, use that

if [ ! "$VM_LONG_NAME" ] ; then VM_LONG_NAME=$VM_SHORT_NAME ; fi

# Do not use 'sudo' if this script is actually running as VM_OWNER already

if [ `whoami` = $VM_OWNER ] ; then SUDO_CMD="" ; else SUDO_CMD="sudo -H -u $VM_OWNER" ; fi

# Set VBoxManage command for stop action

if [ $VM_STOP = powerbutton ] ; then VM_STOP_CMD=acpipowerbutton ; else VM_STOP_CMD=savestate ; fi

# If VM_HOSTNAME isn't set (for 'start-wait' command) use VM_SHORTNAME

if [ ! "$VM_HOSTNAME" ] ; then VM_HOSTNAME=$VM_SHORT_NAME; fi

# Load the VERBOSE setting and other rcS variables
. /lib/init/vars.sh

# Define LSB log_* functions.
# Depend on lsb-base (>= 3.2-14) to ensure that this file is present
# and status_of_proc is working.
. /lib/lsb/init-functions
#echo $VM_LONG_NAME
#echo $VM_SHORT_NAME
get_vm_state()
{
    # possible SHORT_STATE values: running, paused, aborted, powered off

    VMINFO=$($SUDO_CMD $MANAGE_CMD showvminfo "$VM_LONG_NAME" 2>/dev/null)
    if [ $? = 0 ] ; then
        # No error retriving state string
        LONG_STATE=$(echo "$VMINFO"|grep --max-count=1 "^State:"|cut --delimiter=' ' \
            --fields=2-|sed 's/^ *//')
        SHORT_STATE=$(echo $LONG_STATE|cut --delimiter="(" --fields=1|sed 's/ *$//')
        # Fix for syntax highlighting in KomodoEdit for previous line
        [ 0 = 1 ] && NOOP=$(echo ")")
    else
        # VM must be missing
        LONG_STATE=missing
        SHORT_STATE=missing
    fi
}

do_start()
{
    # Return
    #   0 if daemon has been started
    #   1 if daemon was already running
    #   2 if daemon could not be started

    get_vm_state

    if [ "$SHORT_STATE" = "missing" ] ; then

        echo Could not access VM \"$VM_LONG_NAME\".
        return 2
    fi


    if [ "$SHORT_STATE" = "running" ] ; then

        echo VM \"$VM_LONG_NAME\" is already running.
        return 1
    fi

    $SUDO_CMD $MANAGE_CMD startvm "$VM_LONG_NAME" -type vrdp || {
        echo Failed to start VM \"$VM_LONG_NAME\".
        return 2
    }

    # No status report; VBoxManage said if it worked.
    return 0
}

do_stop()
{
    # Return
    #   0 if daemon has been stopped
    #   1 if daemon was already stopped
    #   2 if daemon could not be stopped
    #   other if a failure occurred

    get_vm_state

    if [ "$SHORT_STATE" = "missing" ] ; then

        echo Could not access VM \"$VM_LONG_NAME\".
        return 3
    fi


    if [ ! "$SHORT_STATE" = "running" ] ; then

        echo VM \"$VM_LONG_NAME\" is already stopped.
        return 1
    fi

    $SUDO_CMD $MANAGE_CMD controlvm "$VM_LONG_NAME" $VM_STOP_CMD || {
        echo Failed to hibernate VM \"$VM_LONG_NAME\".
        return 2
    }

    echo Waiting for \"$VM_LONG_NAME\" to complete shutdown...
    while [ "$SHORT_STATE" = "running" ] ; do

        sleep 1
        get_vm_state
    done


    echo The VM \"$VM_LONG_NAME\" has been stopped \($VM_STOP\).
    return 0
}

do_status()
{
    get_vm_state
    if [ "$SHORT_STATE" = "missing" ] ; then

        echo Could not access VM \"$VM_LONG_NAME\".
        return 2
    fi

    echo Status of VM \"$VM_LONG_NAME\": $LONG_STATE

    if [ "$SHORT_STATE" = "running" ] ; then return 1 ; else return 0 ; fi
}

do_reload() {
    VM_STOP=powerbutton
    VM_STOP_CMD=acpipowerbutton
    do_stop && do_start
}

do_wait_for_online() {
    echo Waiting for \"$VM_LONG_NAME\" to come up on the network...
    while [ ! "$result" = "0" ] ; do

        sleep 1
        ping -c 1 $VM_HOSTNAME >/dev/null 2>/dev/null
        result=$?
    done

    echo Ready.
}


case "$1" in
  start)
    [ "$VERBOSE" != no ] && log_daemon_msg "Starting $DESC" "$NAME"
    do_start
    case "$?" in
        0|1) [ "$VERBOSE" != no ] && log_end_msg 0 ;;
        2) [ "$VERBOSE" != no ] && log_end_msg 1 ;;
    esac
    ;;
  start-wait)
    do_start && do_wait_for_online
    ;;
  stop)
    [ "$VERBOSE" != no ] && log_daemon_msg "Stopping $DESC" "$NAME"
    do_stop
    case "$?" in
        0|1) [ "$VERBOSE" != no ] && log_end_msg 0 ;;
        2) [ "$VERBOSE" != no ] && log_end_msg 1 ;;
    esac
    ;;
  status)
    do_status && exit 0 || exit $?
    ;;
  restart|force-reload)
    #
    # If the "reload" option is implemented then remove the
    # 'force-reload' alias
    #
    [ "$VERBOSE" != no ] && log_daemon_msg "Restarting $DESC" "$NAME"
    VM_STOP=powerbutton
    VM_STOP_CMD=acpipowerbutton
    do_stop
    case "$?" in
      0|1)
        do_start
        case "$?" in
            0) [ "$VERBOSE" != no ] && log_end_msg 0 ;;
            1) [ "$VERBOSE" != no ] && log_end_msg 1 ;; # Old process is still running
            *) [ "$VERBOSE" != no ] && log_end_msg 1 ;; # Failed to start
        esac
        ;;
      *)
        # Failed to stop
        [ "$VERBOSE" != no ] && log_end_msg 1
        ;;
    esac
    ;;
  restart-wait)
    VM_STOP=poweroff
    VM_STOP_CMD=acpipowerbutton
    do_stop
    do_start && do_wait_for_online
    ;;
  *)
    echo "Usage: $SCRIPTNAME {start|start-wait|stop|status|restart|restart-wait|force-reload}" >&2
    exit 3
    ;;
esac
