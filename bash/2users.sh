#!/usr/bin/env bash

cat /etc/passwd | cut -d ":" -f 1,7 -
