#! /bin/sh

# Check if the port 5000 is already in use. 
# If YES, stop the process."
port=8080

if lsof -Pi :$port -sTCP:LISTEN -t >/dev/null ; then
    echo "Something is already running on port $port."
    kill -9 $( lsof -nP -iTCP -sTCP:LISTEN | grep $port  |  awk '{print $2}' )
    sleep 1

    if lsof -Pi :$port -sTCP:LISTEN -t >/dev/null ; then
        echo "Error: Process on the port $port cannot be stopped."
    else
        echo "The process on port $port has been stopped."
    fi
    
else
    echo "No process is running on the port $port."
fi