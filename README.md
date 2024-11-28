# Caboodle DEV Install Script Synchronization

The following document describes how this project works and is intended to be setup 

## Prerequisites
1. A Python 3.10 installation, with `python` and `pip` available on the `$PATH` environment variable. This can be installed from the software shop ("Softwareshoppen")

2. The scripts needs the packages listed in `requirements.txt` to be installed. To do this, run the following command on the command line:
```powershell
pip install -r requirements.txt
```
though this should probably be changed to using a virtual environment, to avoid polluting the main Python environment.


### Future Improvements
- [ ] Write documentation
- [ ] Add project to VDI Windows Task Scheduler for recurrent automatic executions.
- [ ] Add functionality to log results, e.g. in a `.txt` file
- [ ] Add requirement to only push deployment scripts if source version is <4 versions older than target. Requires a way to fetch current target version however.