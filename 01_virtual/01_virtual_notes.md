# Virtual Environment 
- useful for isolating dependency from the machine
- it creats a space for our app to install its own version dependency.
- avoids dependency version conflicts
- we can install third party software using it
> Note: Always work in venv!
- we delete the .venv before shipping the prj, jst src & requirement is deployed.

## venv cmd (Traditional Approach)
### creating virtual env
`python -m venv .venv`

- `python`: Invokes the Python interpreter.
- `-m`:
    - stands for find the follwoing module name    
    - Instructs Python to look into its libraries for the module name that follows.
- `venv`: 
    - The name of the standard Python module used to create ⁠isolated virtual environments.
- `.venv` : 
    - is the custom name(industry recommended) 
    - using .evnv as dir name makes it hidden.It's also helpful when we use .gitignore.

### activating virtual env
`.\.venv\Scripts\activate`

### deactivating virtual env
`deactivate`


## installing third party software/prg
1. using `pip `
    - `pip install flask`

2. using `requirements.txt`
    - create requirements.txt file 
    - list all packages in it with desired version u want to install(default latest)
    - then run 
    - `pip install -r requirements.txt`



## UV (modern approach)
1. installation With pip
    `pip install uv`
2. [offical uv repo doc](https://github.com/astral-sh/uv)

3. `uv` workflow sample

    ```bash
    $uv init example #Initialize project directory and files
    Initialized project `example` at `/home/user/example`

    $ cd example

    $ uv add ruff #Add a dependency (automatically creates .venv)
    Creating virtual environment at: .venv
    Resolved 2 packages in 170ms
    Built example @ file:///home/user/example
    Prepared 2 packages in 627ms
    Installed 2 packages in 1ms
    + example==0.1.0 (from file:///home/user/example)
    + ruff==0.5.0

    $ uv run ruff check #Run a tool inside the environment without activation
    All checks passed!

    $ uv lock #Generate the exact lockfile
    Resolved 2 packages in 0.33ms

    $ uv sync #Sync the environment to match the lockfile state
    Resolved 2 packages in 0.70ms
    Checked 1 package in 0.02ms
    ```

### Environment Management
1. `uv venv`: 
    - Creates a blank `.venv` folder in the current directory.
2. `uv add <pkg>`: 
    - Automatically creates `.venv` if it does not exist.
3. `uv venv --python 3.12`: 
    - Creates environment with a specific Python version.
4. `uv python install 3.13`: 
    - Downloads and installs a specific Python version globally.

### Activation (Optional)
1. `source .venv/bin/activate`: Activates environment on macOS / Linux.
2. `.venv\Scripts\activate`: Activates environment on Windows (CMD / PowerShell).

> *Note*: **Activation is optional**. `uv run <cmd>` bypasses the need to activate.

### Dependency Management
1. `uv add <pkg>`: Installs package and updates `pyproject.toml`.
2. `uv add --dev <pkg>`: Adds package as a development-only dependency.
3. `uv remove <pkg>`: Uninstalls package and removes it from `pyproject.toml`.

### Environment Synchronization
1. `uv lock`: 
    - Generates/updates lockfile (`uv.lock`) with exact versions.
2. `uv sync`: 
    - Forces `.venv` to perfectly match the lockfile state.

### Execution & Tools
1. `uv run <cmd>`: 
    - Executes command inside `.venv` without activation.
2. `uv tool run <cmd>` or `uvx <cmd>`: 
    - Runs a global CLI tool instantly without installing it to the project (exactly like React's `npx`).


# Oragnise python
- Directory structure
    ```py 
        chai_shop/
            run.py -> #starts the app(main,app etc)
            chai.py -> #a prg
            processing/ -> #dir
            utils/ #packages
                __init__.py  
    ```
- modules -> any prg files 
- pacakages -> any dir which contains __init__.py file



# PEP8 and zen of python
1. PEP 8 – Style Guide for writting 
    - Python Enhancement Proposal 8
    - the official style guide that defines the rules for writing clean, readable Python cod
    - always use 4 spaces, never tabs (tab default is 4 space but sometimes its configured differently)
    - use better meaningful name
    -  use formatter(black,rough,placate) , it aligns with pep8 way
    - [more info about pep8](https://peps.python.org/pep-0008/)

## Zen of python

- **The Zen of Python, by Tim Peters**
    - In Python, running import this triggers a famous built-in Easter egg that prints The Zen of Python, a collection of 19 guiding principles for writing clean, readable, and elegant code.
    - Written by long-time Python contributor Tim Peters, these aphorisms outline the core philosophy of the language.


- inside the Python environment
    - ```bash
        python #opens python env
            import this #run inside the env
        ```
    - u will get poem with whole point say write code as simple as possible

### The Zen of Python
*By Tim Peters*

* **Beautiful** is better than ugly.
* **Explicit** is better than implicit.
* **Simple** is better than complex.
* **Complex** is better than complicated.
* **Flat** is better than nested.
* **Sparse** is better than dense.
* **Readability** counts.
* **Special cases** aren't special enough to break the rules.
* Although **practicality** beats purity.
* **Errors** should never pass silently.
* **Unless** explicitly silenced.
* In the face of **ambiguity**, refuse the temptation to guess.
* There should be **one-- and preferably only one --obvious way** to do it.
* Although that way may not be obvious at first **unless you're Dutch**.
* **Now** is better than never.
* Although **never** is often better than *right* now.
* If the implementation is **hard to explain**, it's a bad idea.
* If the implementation is **easy to explain**, it may be a good idea.
* **Namespaces** are one honking great idea -- let's do more of those!

