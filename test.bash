#!bin/bash
if curl http://127.0.0.1:6060/ | grep "You are calling me from 127.0.0.1"; then
 exit 0
else
 exit 1
fi