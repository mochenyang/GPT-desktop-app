# GPT-desktop-app

**Update 5/17/2024**: now use Assistant API v2, with streaming

Create a desktop executable that converse with you using GPT:
- Assumes a python environment with ```openai``` package installed and OPENAI_API_KEY registered;
- Replace ```assistant_id``` with your own assistant's asset ID;
- To create a desktop executable in windows, create a shortcut with the following powershell command:

```shell
powershell.exe -command "PATH-TO-ENV/python.exe PATH-TO-REPO/GPT.py"
```

or

```shell
powershell.exe -command "conda activate ENV_NAME python PATH-TO-REPO/GPT.py"
```