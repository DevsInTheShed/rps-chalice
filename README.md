# Rock Paper Scissors App 
## Using AWS Chalice for Python Serverless

### Prerequsites:
* Python 3.8 installed
* IDE / Text Editor of your choosing
* Terminal / Command Prompt / Powershell

* Boto3 or AWS CLI installed
* Run ```aws configure``` within your terminal of choice and completed the asked steps


### To install:
* Download this repository and navigate to the downloaded project folder within your terminal of choice.
* Run the following command in terminal to download the Chalice CLI (note some systems you'll need to use pip3 instead):
``` bash
pip install chalice
```
* Create a virtual environment within your project folder (note some systems you'll need to use python3 instead):
``` bash
python -m venv venv
. venv/bin/activate
```
* Install any extra dependancies (note again some systems you'll need to use pip3 instead):
``` bash
pip install -r requirements.txt
```

### Now you can run locally or on AWS!
* Run the following command in terminal to deploy locally on your computer: 
``` bash
chalice local
```

* Run the following command in terminal to deploy on AWS: 
``` bash
chalice deploy
```
