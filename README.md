# Overview

This project's goal is to set up a CI/CD pipeline for a Flask web service which computes prices for houses in Boston based on a number of features. 

## Project Plan


* [Link to Trello board for the project](https://trello.com/b/dKbbZzsg/devops-project)
* [Link to the project plan spreadsheet](https://docs.google.com/spreadsheets/d/1AzvBUGSu-URpM0XsHgL2tsENGYB3ROJ0uO799wWlHSs/edit?usp=sharing)

## Instructions

### Architectural Diagram 
![Architecture](/images/Azure_CI_CD_Architecture.jpg)


### Basic instructions to setup & run the project

1. Checkout the code (`git clone`) and create an environment in the root
2. To try locally that everything's OK, run
```
python3 -m venv .VENV
source VENV/bin/activate
make all
export FLASK_APP=app.py
flask run
```
3. On GitHub, check everything integrates properly under GitHub actions.
4. Run `az webapp up -sku F1 -n Flask-ML-App` to create the AppService instance.
5. Go to `https://dev.azure.com`, create a new project, then create a new Pipeline and follow the simple steps in the wizard to connect the GitHub repo to the AppService instance.

* Project running on Azure App Service
![Project Running On Azure AppService](/images/App_running_Apservice.png)

* Project cloned into Azure Cloud Shell
![Project Cloned in Azure Cloud Shell](/images/GitHub_Repo_Azure_Cloud_Shell.png)

* Passing tests that are displayed after running the `make all` command from the `Makefile`
![Tests passing](/images/Make_all.png)

* Output of a test run
![Test output]()

* Successful deploy of the project in Azure Pipelines.
![Test output](/images/Pipeline_Successful_Deploy.png)

* Running Azure App Service from Azure Pipelines automatic deployment
![Pipelines Running](/images/App_Deployed_Pipelines_Automatically.png)

* Successful prediction from deployed flask app in Azure Cloud Shell. 
![Successful Prediction]()

* Output of streamed log files from deployed application
![Log streams](/images/App_Running_Logs.png)


## Enhancements

An important thing would be to upgrade libraries' versions. I had to downgrade versions and pin those downgraded ones in order to get the project running. Also having up to date versions would improve security.

## Demo 

<TODO: Add link Screencast on YouTube>


