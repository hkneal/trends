Generate a chart of the top 5 positive trends over the timeframe of provided data.

1) Create a python virtual environment.
	- In a terminal window issue the command "pip3 install virtualenv" if using a mac otherwise please refer to the link below for install instructions:
	https://www.google.com/search?q=install+virtualenv&oq=install+virt&gs_lcrp=EgZjaHJvbWUqBwgCEAAYgAQyBwgAEAAYgAQyBggBEEUYOTIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCDQyMjBqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8

	- create the environment by issuing the command: "virtualenv <environment_name>" eg. "virtualenv venv" where "venv" is the name of my virtual envrionment.

2) Active the environment
	- Issue the command "source venv/bin/activate"  syntax: source <environment_name>/bin/activate

3) Install requirements
	- issue the command "pip3 install -r requirements.txt"

4) Run the command to generate the charts
	- issue "python3 chart_top_5_positive_trends.py" to get the top 5 trends charted
 	- issue "python3 chart_top_5_trends_over_time.py" to get the top 5 trends over the duration of time charted.
	
