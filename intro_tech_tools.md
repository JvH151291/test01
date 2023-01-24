# Technical Tools

We would like to help you establish (what we think) good practices in data management and programming/scripting. Therefore we use (and partially enforce the use) of the following tools in this exercise series:

- `git` version control and `GitLab` (to collaborate on code)
- `PostgreSQL` database management
- `Visual Studio Code` IDE (of course, you are free to use any editor you like - extra points for emacs or Vim users ;)
- `python`, `pip` and `venv` (virtual environments, you may also use conda if you prefer)

This document introduces these tools and hints to additional resources. We know, it is a lot to take in at once. But you can use this document as a reference for the course. Apart from the python code that you will have to write to conduct the analysis, you should find a simple example for every command (of the other tools) that we need in this course which you can slightly adjust to suit your needs.

## Motivation

Data and software literacy should be an integral part of any academic (hard science) education. We would like you to get acquainted with some of the most frequently used tools where you hopefully experience their power throughout the hands-on exercise series.

Let me explain to you why we need these tools in the context of this lecture: You will have to conduct simple data analysis and perform optimizations which requires you to code in [`python`](https://www.python.org/) (one of the most popular programming languages).

Python can be learned relatively easily (read the [docs](https://www.python.org/doc/)). As with any programming language, you should familiarize yourself with the basic building blocks of the programming language, which include:

- Data types (e.g. integer, string, Boolean)
- Variables
- Operators (e.g. arithmetic, comparison, logical)
- Control structures (e.g. if-else statements, loops)
- Functions or subroutines
- Input/output statements
- Comments

These building blocks can be combined to create statements and expressions, which are then used to write programs (I've asked [ChatGPT](https://chat.openai.com/chat) to write down these basic building blocks).

Anyways, understanding these blocks is relatively simple and the power of using a language usually comes from its package ecosystem. A `package` is a collection of code (usually functions or objects and methods) which provide domain functionality (e.g. the [`pandas`](https://pandas.pydata.org/) package which provides powerful data analyis tools such as the `pandas.DataFrame` object and its associated methods). When learning how to use that functionality, it is not so much about learning complicated coding but simply about reading the documentation and understanding what function/method accomplishes what and what arguments you need to feed (more on this in the [Getting help](#getting-help) section).

> A sidenote on packages: You should not feel intimidated to write your own packages. A package (in any programming language) is just a conveniently structured repository following given conventions. You are welcome to learn more by following this [simple tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/) on how to write a minimal package in python.

We will learn how to easily install packages with `pip` - the python package manger. Every analysis should be reproducable, i.e. anyone should be able to arrive at the same output given the input (i.e. raw data) preferably on any system (e.g. mac, windows, linux). Therefore we want to encapsulate our environment such that it is easily portable and can be shared with others (students, researchers, the public, etc.). For this purpose we install the packages into so-called *virtuel environments* (`venv`).

On the note of reproducibility: You yourself sometimes are not sure what your alter ego did. (Automatically) documenting the different stages of your development and project work therefore makes sense. Further, you sometimes do something wrong or want to revert your work to a previous state. Therefore a version control system (`git`) is a very powerful tool. It also allows you to collaborate effectively, without having to worry to overwrite your colleagues state of work!

[`GitLab`](https://about.gitlab.com/) is just the hosting platform where you can mirror your local project structure and share your work with the world (or with us for grading).

Sooner or later, you will realize that sharing and managing (raw) data with `.csv` files or other formats is very cumbersome. For example, a .csv file lives only on the local computer and if you want to share it you have to physically copy and share the file (that is the data gets duplicated). Or have you ever (tried) to open an excel spreadsheet containing some GB of data just to get a feel for what it actually contains? As you will individually collect your raw data for the analysis (through surveying bus users) and share it with the rest of the class, we will use `PostgreSQL`. The database will be hosted on a server and therefore we can easily pull/access the data in our python scripts with help of the `psycopg` python package.

> Of course you can also run a Postgres DB on your local computer and organize your personal data without the need of a server (a server is just a computer system attached to a network).

[`Visual Studio Code`](https://code.visualstudio.com/) is just an *Interactive Development Enviornment*, i.e. a text editor with superpowers such as syntax highlighting, autocompletions, syntax highlighting, signature help, integrated REPL, etc. You are free to use another one you like (for exmample PyCharm is another popular choice). While *Jupyter Notebooks* are very neat, they have some limitations in data analysis (for example code output and chronology of ran cells gets stored in the very file which makes it difficult to version control). Personally, I have a preference for general purpose tools such that you do not have to learn/use a new environment when you switch the language...

But let's get started!



## Getting on the same page

1. Fire up a terminal running `bash` or the `zsh` (on windows use [Git BASH](https://gitforwindows.org/))
2. Check that git is installed and see some of the commands that we will use later: `git --help`
3. Create a repository on your root and switch to it `cd ~ && mkdir gitlab && cd gitlab`
4. Get this PuvIntro repository (i.e. `clone` it from gitlab) `git clone git@gitlab.ethz.ch:daniehei/PuvIntro.git`
5. Open vscode (`code .`) and click on the README file.
6. Open up a terminal inside vscode with `Ctrl+Shift+P` (opens the command palette) and type terminal and hit `Enter`.
7. Create a virtual environment called *env* with `python3 -m venv env`.
8. Install the Python extension.
9. Tell vscode to use the newly created env when interpreting python code: `Ctrl+Shift+P`, type `Python: Select interpreter` and choose the before created `env`.
10. Make sure the env is activated `source env/bin/activate` (or open a new terminal as described above).

Your prompt should look something like this (note the `(env)` before `usr@hostname`):

```
(env) daniehei@ivt-thinkpd-85:~/Teaching/PuV/2023/PuvIntro$
```

By the way, the `PuvIntro` is structured as a python package:

```
.
├── LICENCE
├── pyproject.toml
├── README.ipynb
├── README.md
└── src
    └── greatest_package
        ├── greetings.py
        ├── __init__.py
```

11. Therefore we can install it locally with `pip install -e .`
12. The PuvIntro package provides a very useful functionality
    - Start the python interpreter `python`
    - `from greatest_package import greet`
    - `greet.daniehei_greets()`
13. For illustration, this project also uses some dependencies as listed in the `requirements.txt`
    - Install them with `pip install -r requirements.txt`
14. Open the file (module) `greetings.py` and extend it with a function that prints a greeting message (use your eth-username to name the function as otherwise we might end up with several functions having the same name).
15. Add your version of the script with `git add .`
16. Commit with a meaningful message `git commit -m "best commit ever"`.
17. Push the commit to the gitlab repository (to make it available to others) `git push`.
18. Pull the updated project `git pull`.
19. You can inspect all the great commits with `git log` (or tools such as `lazygit`).
20. Fire up a python interpreter and try out the different functions.

### Summary

We have cloned the repository `PuvIntro` which is hosted on my gitlab page (i.e. we made a local versioned copy of it). Subsequently, we've created a virtual environment and told our IDE to use it when interpreting python code. We could conveniently explore the functions by locally installing our package. We have installed all the dependencies that would be required to run our code from the `requirements.txt` file. That is, we are all on the same page: We all have the same version of the PuvIntro project and this project is evaluated in the exactly same environemnt (Sideremark: maybe you have a slightly different python3 version, but this does not matter for now). We then extended the project's functionality and made it publicly available on gitlab. This allows others to leverage the functionality and explore the project evolution and contribute to your code without messing it up with help of `git`. So the full cycle is (clone), pull, change a bit, commit meaningful chunks, push, restart the game, ...

This was a high level introduction of the basics. We now introduce each aspect in more detail as well as ellaborate a bit on PostgreSQL.

## python

This is not a language introduction. If you struggle with the language itself, please find a strategy to update your knowledge - there are tons of very good (and free) resources online.


### Getting help
<a id="getting-help"></a>

As already mentioned, the official documentation is always the best reference. However, there are additional tools to get the gist of a programme respectively its functionality. As you might have realized one of the dependencies that we've installed from the requirements was pandas. Here are some strategies to understand this library:

- `help(pandas)`
- `dir(pandas)` (if you don't understand what `dir` does then type `help(dir)`)
    - Ok, so there is a `DataFrame` object provided... What is it though? `help(pandas.DataFrame)`
        - Hint: You can scroll the document with the Vim-keys j and k and you can search for keywords like so `/keyword`.
        - Similarly: What can we do with the DataFrame? `dir(pandas.DataFrame)`
            - Aha, there is a filter `method`. But what can it do? `help(pandas.DataFrame.filter)`
            - Remark: Why is it not the same as simply typing `help(filter)`?

> This documentation is automatically generated because the maintainers of the code added `docstrings` to their code (which you definitively should do as well!) Also, it is good practice to add `type hints` (see greetings.py -> daniehei_greets for an example).

- Check out the file `ide_demo` which showcases the power of an IDE and allows you to jump directly to the definition in the source code.
- You can get pretty much the same experience by going to the reference section of the [official documentation](https://pandas.pydata.org/docs/). There you additionally a gettings started guide and some other stuff which might help you get started.
- We all heard of it: You might want to ask [ChatGPT](https://chat.openai.com/chat) for help. I strongly encourage you to try it out! The more precisely you can frame a question, the more helpful the answer. For example: *Mighty chatbot, how can I find out about implemented classes, methods and functions of a python package?*
- Google
- [stackoverflow](https://stackoverflow.com/). However, you should be critical with the snippets that users provide and not simply copy paste without understanding what the code does...
- Youtube (there it is important to find the right tutor: I find [Corey Schafer](https://www.youtube.com/@coreyms) very helpful. He also has a *Pandas Tutorials* and *Matplotlib Tutorials* playlist which you might find useful).


## venv

[venv](https://docs.python.org/3/library/venv.html) is just a python module (it comes shipped with your python installation) which allows you to create encapsulated (independent set python packages installed in their own directory). There are only three commands you should know:

```bash
# Init new venv
python3 -m venv /path/to/new/environment

# For example if you want to init a new venv called env at the current location
python3 -m venv env

# Activate the env (on Mac or Linux)
source env/bin/activate

# On Windows
...

# Deactivate
deactivate

# On Windows
...
```


## pip

[pip](https://pypi.org/project/pip/) is the python package manager. You can read throught the [Getting Started](https://pip.pypa.io/en/stable/getting-started/) guide at your leasure. I focus on the key commands that you should know. The basic usage is `pip install package`. However, this installs the package to the system's python site-packages directory (so globally). If you have several python versions installed (e.g. on linux you usually have both python2 and python3) then it is not clear to which python version the pip command installs to as pip as well as pip3 are associated with one particular python version. So therefore I would suggest that you call pip as a module starting with your preferred python version like so:

```python
python3.8 -m pip install package
```

Update a package (for example pip) with the following command:

```python
python3.8 -m pip install --upgrade pip
```

Once you have activated the virtual environment, there is no need to call pip as a module. You can simply use `pip install package`.

You can list installed packages with `pip list`. If you want to make your environment reproducable, you can write the current state to a `requirements.txt` file like so:

```bash
pip freeze > requirements.txt
```

Remark: The `>` operator pipes the output of the LHS into the file on the RHS.



## Git version control

> Please read the first three chapters of the [git Book](https://git-scm.com/book/en/v2). It takes maybe 30-60 minutes and I promise you, knowing a little about git will serve you well not only in this course!

Git knows the state of each file in your git repository! But not only that, it also remembers all the previously commited stages. It knows the differences of all these stages and they are easily recoverable. Let's explore and explain some of its core functionality:

```bash
# Change directory (~ stands for your home directory)
cd ~/gitlab

# Create an exmaple directory (. stands for the current directory (i.e. ~/gitlab))
mkdir ./test

# Init current directory (.) to be a git repository
git init .

# See: this added a hidden .git repository
ls -a

# Add a file (you can also use a text editor)
echo "hello git" > hello.txt

# Check the status
git status

# (if you are using a venv called env do not include the env repo in git tracking)
echo "env" > .gitignore

# Add


```

**check that you've pointed to valuable resource, such as git book**

# Exercise

1. Initialize a new empty repository in your `~/gitlab/` main repo.
2. Initialize the repository to be a git repository.
3. Write an sql script that initializes a new table called `<your eth-abbr>_message` containing only one column `message` and populate it with one secret message.
4. Commit the newly created script and add a meaningful commit message.
5. Try to implement the python package repository structure as in `PuvIntro` or follow this [tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/).
6. Write a function that queries the newly created table (with `psycopg`) and prints a message stored in the message table.
7. Commit your awesome package
8. Initilaize an new gitlab repository (hint: just navigate to *Create new project* https://gitlab.ethz.ch/projects/new and copy paste the code that pops up when you click *Show command* - you can paste the command into your terminal and execute it).
9. Share your code with the message recipient.
10. Clone someone elses awesome package and try to call the function printing the secret message.
