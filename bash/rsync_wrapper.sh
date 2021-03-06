#!/usr/bin/env bash
USER=$(whoami)
RSYNC=$(which rsync)
LOGGER_TAG="rsync_wrapper"
LOGGER="$(which logger) -t $LOGGER_TAG -i"

echo "starting rsync backup for $USER" | $LOGGER -p user.err
if [ -f /home/$USER/.env_vars ]; then
    source /home/$USER/.env_vars
else
    echo "env_vars not found" | $LOGGER -p user.err
    exit 1;
fi

if [ -f /home/$USER/.ssh/config ]; then
    $RSYNC -rl --exclude-from=/etc/turbo_happiness/rsync_exclude.conf $HOME -e ssh $USER.$BACKUP_SERVER:$BACKUP_PATH/$USER/rsync
    rsync_status="$?"
    if [ "$rsync_status" = "0" ]; then
        echo "complete for $USER" | $LOGGER -p user.err
        exit $rsync_status
    else
        echo "failed for $USER with exit status $rsync_status" | $LOGGER -p user.err
        exit $rsync_status
    fi
fi
echo "CONFIG: rsync wrapper fails config test." | $LOGGER -p user.err

