#!/bin/bash
### BEGIN INIT INFO
# Provides:          suelliton 2
# Required-Start:    $local_fs $network
# Required-Stop:     $local_fs
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: suelliton sir
# Description:       suelliton sir
### END INIT INFO
python /home/suelliton/sir-app/sir2.py