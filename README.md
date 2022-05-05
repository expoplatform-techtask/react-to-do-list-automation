# PLEASE READ BEFORE INSTALL #


### What is this repository for? ###

* This is automation test coverage for REACT-TO-DO-LIST regression suite. It is fully integrated with TestRail and all results will appear in test cycle of existing project.

### How do I get set up? ###

* Download the latest version of Python https://www.python.org/downloads
* Clone this repository to your local machine
* Install all packages ```pip3 install -r requirements.txt```
* Run ```python3 -m pytest tests --testrail --tr-config=testrail.cfg --stand=prod``` in terminal to get execution result for **UI coverage** on PROD environment
* Find the latest test run in TestRail project to see results
----------
* **NOTE:** text after ```--stand``` is variable to identify what environment should be used for execution. For example: command ```python3 -m pytest tests --testrail --tr-config=testrail.cfg --stand=dev``` will run autotests on **DEV** environment.
* Available values to identify environment: dev, preprod, prod