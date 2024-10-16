# Virtual Environment Setup Guide

## 1. Create a Virtual Environment

To activate a virtual environment, execute the following command in PowerShell from the parent directory:
```powershell
python -m venv ./<venv_Name>
```


## 2. Activate a Virtual Environment

To activate a virtual environment, execute the following command in PowerShell from the path where the `venv` folder is located:
(Windows:)
```powershell
venv/Scripts/Activate.ps1
```


## 3. Install a Package within the Virtual Environment

Once the virtual environment is activated, you can install a package using `pip`:

```powershell
pip install <packageName>
```


## 4. Deactivate the Virtual Environment
To deactivate the virtual environment, execute the following command in the terminal:
```powershell
deactivate
```


