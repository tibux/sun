#!/bin/sh
# Start/stop/restart Slackware Update Notifier.

SERVICE=sun_daemon

case "$1" in
'start')
  /etc/rc.d/rc.sun start
  ;;
'stop')
  /etc/rc.d/rc.sun stop
  ;;
'restart')
  /etc/rc.d/rc.sun restart
  ;;
'status')
  if [ -z "$(ps ax | grep -v grep | grep $SERVICE)" ]; then
     echo "sun is not running"
  else
     echo "sun is running"
  fi
  ;;
*)
  echo "usage $0 start|stop|restart|status"
esac
