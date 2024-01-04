# GPT-desktop-app
Create a desktop executable that converse with you using GPT:
- Assumes a python environment with ```openai``` package installed and OPENAI_API_KEY registered
- To create a desktop executable in windows, create a shortcut with the following powershell command:

```shell
powershell.exe -command "PATH-TO-ENV/python.exe PATH-TO-REPO/GPT.py"
```

or

```shell
powershell.exe -command "conda activate ENV_NAME python PATH-TO-REPO/GPT.py"
```