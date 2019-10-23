# voy_dev_track
Voyance Device Tracking Application

***** To run as a script *****

REQUIRES Python 3.7.5

Open a terminal windows and CD into the directory where you downloaded/unpacked this script.

Create a VENV and ensure it is activated.

Do a 'pip install -r requirements.txt'

Copy the config_sample.yaml and rename it config.yaml

Update the config.yaml with the information for your instance. 

run the script with 'python3 main.py --cfgfile config.yaml --savefile dev_info.yaml'

config.yaml and dev_info.yaml should be full paths if they aren't in the same directory as the main.py file



***** To run in Docker *****

Create a folder to hold the savefile and config file.

Copy the config_sample.yaml into the folder you created from github and rename it config.yaml 

Update the config.yaml with the information for your instance. 

'docker run -v <path on your machine to the directory with the savefile and config file>:/config'

