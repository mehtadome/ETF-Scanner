# Backend

# Configure Development Environment

Follow these steps to correctly configure the development environment for the backend.

## Run individual scripts

Python treats modules as packages. Because of such, importing different files to use their functions becomes much more complex for testing.

To correctly import files from other parts of the app, _relative imports_ are used.

```
from ...exports import init_table
```

- Each dot signifies one level of the directory.
- - 1: Current, 2: Parent: 3: Parent's Parent, etc.

To run an individual file using relative imports, you have to use a special command which indicates to Python that the file is using a relative import.

- See more [here](https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time) why it is necessary.

The following needs to be run in the root folder of the project (in this case, "`./ETF-Scanner/`").

```
python -m backend.modules.calcs.ETFs.annual_return
```

The `-m` indicates to the Python interpreter to treat the file as within a package. You then provide the path to the file. Notice the `.py` is ommitted because it is now being considered as a _package module_ and not an individual script.
