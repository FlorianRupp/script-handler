# script-handler

This is a small django based web server. It is made to run on localhost to
trigger the execution of scripts by external applications.

## Usage

Just do a post to e.g. ```http://localhost:8765``` with parameter ``command``. The value
of command will be executed on command line. This may a high security risk, so only run it on localhost!


## Quick start
1. Clone this repository.
2. Run: ```nohup python script_server/manage.py runserver 127.0.0.1:8765 &```