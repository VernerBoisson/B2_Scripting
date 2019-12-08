#!/usr/bin/env bash

hostname=$( { hostname; } )
ip=$( { ip route get 1 | awk '{print $((NF-2));exit}'; } )
os=$( { cat /etc/issue | tr -d '\\nl'; } )
kernel=$( { uname -sr; } )
log=$( { last -5; } )
python=$( { python --version; } )
ssh=$( { systemctl status ssh; } )
echo "$hostname $ip
$os
$kernel
$log
$python"