# exam_app_smartcontract
An exam app built using Django and Solidity. Teachers and professors can use this to generate random question to a student from a set of question bank.

## Installation
1)clone the repo on your system.

2)Install python3 on your system from https://www.python.org/downloads/

3)install pip3 from https://pip.pypa.io/en/stable/installation/

4)install django from https://docs.djangoproject.com/en/4.1/topics/install/

If other things are installed correctly , you just have to run 
```
$ python3 -m pip install Django
```
in terminal.

5)install web3.py using

```
$ pip3 install web3
```

or

```
$ pip install web3
```

Detailed documentation is available at: https://web3py.readthedocs.io/en/stable/quickstart.html

### note: 
These are some modules which you might need to install after these. Install all of them using
```pip3 install <module name> ``` or ```pip install <module name> ```
If you still are not ale to run the project , simply google up the necessary module and install it. 
Contact me if you are not able to run the app even after googling.

6)cd exam_app

7)run ``` python3 manage.py runserver ``` in terminal after all necessary modules and libraries are installed. 

### Troubleshoot:

If it gives port error , change the ```ganache_url``` in the ```exam_app/authentication/smart_contract_integration.py``` file to your ganache port. 

Download ganache from https://trufflesuite.com/ganache/ , if it is not installed

Copy the code from "exam_app/smart_contract" and deploy it on the local blockchain created using ganache.

Steps:
1)Open remix IDE. Copy the code from "exam_app/smart_contract". Deploy it with external http provider. Your http provider is given in Ganache app installed on your system as "RPC SERVER" at second top bar.

2)copy the smart contract address and abi and change the one in  ```exam_app/authentication/smart_contract_integration.py``` to your address and abi.
Now run ``` python3 manage.py runserver ``` in terminal again.

