# Virtual Environment 
- useful for isolating dependency from the machine
- it creats a spaace for our app to install its own version dependency.
- avoids dependency version conflicts
- we can install third party software using it
> Always work in venv!
- we delete the .venv before shipping the prj, jst src & requirement is deployed

## venv cmd (Traditional Approach)
### creating virtual env
`python -m venv .venv`
- .venv is the custom name(industry recommeded) 
- using .evnv makes it hidden also helpful when we use in .gitignore

### activating virtual env
`.\.venv\Scripts\activate`

### deactivating virtual env
`deactivate`


## installing third party software/prg
1. using pip 
- pip install flask

2. using requirements.txt
- create requirements.txt file 
- list all packages in it with desired version u want to install(default latest)
- then run 
> pip install -r requirements.txt



## UV (modern approach)
1.
2.
3.




# Oragnise python 
chai_shop/
    run.py -> #starts the app(main,app etc)
    chai.py -> #a prg
    processing/ -> #dir
    utils/ #packages
        __init__.py  

1. modules -> any prg files 
2. pacakages -> any dir which contains __init__.py file



# PEP8 and zen of python
1. PEP 8 – Style Guide for writting 
    a. always use 4 spaces, never tabs(default 4 space but sometimes its configured differently)
2. use better meaningful name
3. use formatter(black,rough,placate) , it aligns with pep8 way

Python Code
https://peps.python.org/pep-0008/
- ala

## Zen of python
Type `python` and press Enter.
Type `import this` inside the Python environment

u will get poem with whole point say write code as simple as possible


**The Zen of Python, by Tim Peters**

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

In Python, running import this triggers a famous built-in Easter egg that prints The Zen of Python, a collection of 19 guiding principles for writing clean, readable, and elegant code. Written by long-time Python contributor Tim Peters, these aphorisms outline the core philosophy of the language.
