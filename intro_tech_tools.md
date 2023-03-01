# Technical Tools

## Prerequisites

For this introduction you need the following software:

- [Python](https://www.python.org/) (python3)
- [Pycharm Professional](https://www.jetbrains.com/pycharm)
- [git](https://git-scm.com/)
- [PostgreSQL](https://www.postgresql.org/)

> For windows users: You might want to use [chocolatey](https://chocolatey.org/install)
> For mac users: You might want to use [brew](https://brew.sh/)
> These are package managers (allow you to install software easily!) similar to pip. However, pip is for python packages
> whereas the above tools are for OS software (e.g. pycharm, postgresql, etc.).

## Motivation

We would like to help you establish (what we think) good practices in data management and programming/scripting.
Therefore, we use (and partially enforce the use) of the following tools in this exercise series:

- `git` version control and `GitLab` (to collaborate on code)
- `PostgreSQL` database management
- `Pycharm Professional` IDE (of course, you are free to use any editor you like - extra points for emacs or Vim users ;)
- `Python`, `pip` and `venv` (virtual environments, you may also use conda if you prefer)
- `toolchain` a set of tools to efficiently handle tedious things like formatting etc.

This document introduces these tools and hints to additional resources. We know, it is a lot to take in at once. But you
can use this document as a reference for the course. Apart from the Python code that you will have to write to conduct
the analysis, you should find a simple example for every command (of the other tools) that we need in this course which
you can slightly adjust to suit your needs.

Data and software literacy should be an integral part of any academic (hard science) education. We would like you to get
acquainted with some of the most frequently used tools where you hopefully experience their power throughout the
hands-on exercise series.

Let me explain to you why we need these tools in the context of this lecture: You will have to conduct simple data
analysis and perform optimizations which requires you to code in [`Python`](https://www.python.org/) (one of the most
popular programming languages).

Python can be learned relatively easily (read the [docs](https://www.python.org/doc/)). As with any programming
language, you should familiarize yourself with the basic building blocks of the programming language, which include:

- Data types (e.g. integer, string, Boolean)
- Variables
- Operators (e.g. arithmetic, comparison, logical)
- Control structures (e.g. if-else statements, loops)
- Functions or subroutines
- Input/output statements
- Comments

These building blocks can be combined to create statements and expressions, which are then used to write programs (I've
asked [ChatGPT](https://chat.openai.com/chat) to write down these basic building blocks).

Anyway, understanding these blocks is relatively simple and the power of using a language usually comes from its package
ecosystem. A `package` is a collection of code (typically functions or classes and methods) which provide domain
functionality (e.g. the [`pandas`](https://pandas.pydata.org/) package which provides powerful data analysis tools such
as the `pandas.DataFrame` class and its associated methods). When learning how to use that functionality, it is not so
much about learning complicated coding but simply about reading the documentation and understanding what function/method
accomplishes what and what arguments you need to feed (more on this in the [Getting help](#getting-help) section).

> A side-note on packages: You should not feel intimidated to write your own packages. A package (in any programming
> language) is just a conveniently structured repository following given conventions. You are welcome to learn more by
> following this [simple tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/) on how to write
> a
> minimal package in Python.

We will learn how to easily install packages with `pip` - the Python package manager. Every analysis should be
reproducible, i.e. anyone should be able to arrive at the same output given the input (i.e. raw data) preferably on any
system (e.g. mac, windows, linux). Therefore, we want to encapsulate our environment such that it is easily portable and
can be shared with others (students, researchers, the public, etc.). For this purpose we install the packages into
so-called *virtuel environments* (`venv`).

On the note of reproducibility: You yourself sometimes are not sure what your alter ego did. (Automatically) documenting
the different stages of your development and project work therefore makes sense. Further, you sometimes do something
wrong or want to revert your work to a previous state. Therefore, a version control system (`git`) is a very powerful
tool. It also allows you to collaborate effectively, without having to worry to overwrite your colleagues state of work!

[`GitLab`](https://about.gitlab.com/) is just the hosting platform where you can mirror your local project structure and
share your work with the world (or with us for grading).

Sooner or later, you will realize that sharing and managing (raw) data with `.csv` files or other formats is very
cumbersome. For example, a .csv file lives only on the local computer and if you want to share it you have to physically
copy and share the file (that is the data gets duplicated). Or have you ever (tried) to open an Excel spreadsheet
containing some GB of data just to get a feel for what it actually contains? As you will individually collect your raw
data for the analysis (through surveying bus users) and share it with the rest of the class, we will use `PostgreSQL`.
The database will be hosted on a server, and therefore we can easily pull/access the data in our Python scripts with
help of the `psycopg2` Python package.

> Of course, you can also run a Postgres DB on your local computer and organize your personal data without the need of a
> server (a server is just a computer system attached to a network).

[Pycharm Professional](https://www.jetbrains.com/pycharm) is just an *Interactive Development Environment*, i.e. a text
editor with superpowers such as syntax highlighting, autocompletion, syntax highlighting, signature help, integrated
REPL, etc. You are free to use another one you like (for example PyCharm is another popular choice). While *Jupyter
Notebooks* are very neat, they have some limitations in data analysis (for example code output and chronology of ran
cells gets stored in the very file which makes it difficult to version control). Personally, I have a preference for
general purpose tools such that you do not have to learn/use a new environment when you switch the language...

But let's get started!

## Getting on the same page

> Potentially have to add ssh...

1. Fire up a terminal running `bash` or the `zsh` (on Windows use [Git BASH](https://gitforwindows.org/))
2. Check that git is installed and see some commands that we will use later: `git --help`
3. Create a repository on your root and switch to it `cd ~ && mkdir gitlab && cd gitlab`
4. Get this PuvIntro repository (i.e. `clone` it from gitlab) `git clone git@gitlab.ethz.ch:daniehei/PuvIntro.git`
5. Open vscode (`code .`) and click on the README file.
6. Open up a terminal inside vscode with `Ctrl+Shift+P` (opens the command palette) and type terminal and hit `Enter`.
7. Create a virtual environment called *env* with `python3 -m venv env`.
8. Install the Python extension.
9. Tell vscode to use the newly created env when interpreting Python code: `Ctrl+Shift+P`,
   type `Python: Select interpreter` and choose the before created `env`.
10. Make sure the env is activated `source env/bin/activate` (or open a new terminal as described above).

Your prompt should look something like this (note the `(env)` before `usr@hostname`):

```
(env) daniehei@ivt-thinkpd-85:~/Teaching/PuV/2023/PuvIntro$
```

By the way, the `PuvIntro` is structured as a Python package:

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
    - Start the Python interpreter `Python`
    - `from greatest_package import greetings`
    - `greetings.daniehei_greets()`
13. For illustration, this project also uses some dependencies as listed in the `requirements.txt`
    - Install them with `pip install -r requirements.txt`
14. Open the file (module) `greetings.py` and extend it with a function that prints a greeting message (use your
    eth-username to name the function as otherwise we might end up with several functions having the same name).
15. Add your version of the script with `git add .`
16. Commit with a meaningful message `git commit -m "best commit ever"`.
17. Push the commit to the gitlab repository (to make it available to others) `git push`.
18. Pull the updated project `git pull`.
19. You can inspect all the great commits with `git log` (or tools such as `lazygit`).
20. Fire up a Python interpreter and try out the different functions.

### Summary

We have cloned the repository `PuvIntro` which is hosted on my gitlab page (i.e. we made a local versioned copy of it).
Subsequently, we've created a virtual environment and told our IDE to use it when interpreting Python code. We could
conveniently explore the functions by locally installing our package. We have installed all the dependencies that would
be required to run our code from the `requirements.txt` file. That is, we are all on the same page: We all have the same
version of the PuvIntro project and this project is evaluated in the exactly same environemnt (Sideremark: maybe you
have a slightly different python3 version, but this does not matter for now). We then extended the project's
functionality and made it publicly available on gitlab. This allows others to leverage the functionality and explore the
project evolution and contribute to your code without messing it up with help of `git`. So the full cycle is (clone),
pull, change a bit, commit meaningful chunks, push, restart the game, ...

This was a high level introduction of the basics. We now introduce each aspect in more detail as well as elaborate a bit
on PostgreSQL.

## Python

This is not a language introduction. If you struggle with the language itself, please find a strategy to update your
knowledge - there are tons of very good (and free) resources online.

### Getting help

<a id="getting-help"></a>

As already mentioned, the official documentation is always the best reference. However, there are additional tools to
get the gist of a programme respectively its functionality. As you might have realized one of the dependencies that
we've installed from the requirements was pandas. Here are some strategies to understand this library:

- `help(pandas)`
- `dir(pandas)` (if you don't understand what `dir` does then type `help(dir)`)
    - Ok, so there is a `DataFrame` class provided... What is it though? `help(pandas.DataFrame)`
        - Hint: You can scroll the document with the Vim-keys j and k, and you can search for keywords like
          so `/keyword`.
        - Similarly: What can we do with the DataFrame? `dir(pandas.DataFrame)`
            - Aha, there is a filter `method`. But what can it do? `help(pandas.DataFrame.filter)`
            - Remark: Why is it not the same as simply typing `help(filter)`?

> This documentation is automatically generated because the maintainers of the code added `docstrings` to their code (
> which you definitively should do as well!) Also, it is good practice to add `type hints` (see greetings.py ->
> daniehei_greets for an example).

- Check out the file `ide_demo` which showcases the power of an IDE and allows you to jump directly to the definition in
  the source code.
- You can get pretty much the same experience by going to the reference section of
  the [official documentation](https://pandas.pydata.org/docs/). There you additionally find a getting started guide and
  some other stuff which might help you get started.
- We all heard of it: You might want to ask [ChatGPT](https://chat.openai.com/chat) for help. I strongly encourage you
  to try it out! The more precisely you can frame a question, the more helpful the answer. For example: *Mighty chatbot,
  how can I find out about implemented classes, methods and functions of a Python package?*
- Google
- [stackoverflow](https://stackoverflow.com/). However, you should be critical with the snippets that users provide and
  not simply copy and paste without understanding what the code does...
- Youtube (there it is important to find the right tutor: I find [Corey Schafer](https://www.youtube.com/@coreyms) very
  helpful. He also has a *Pandas Tutorials* and *Matplotlib Tutorials* playlist which you might find useful).

## venv

[venv](https://docs.python.org/3/library/venv.html) is just a Python module (it comes shipped with your Python
installation) which allows you to create encapsulated (independent set Python packages installed in their own directory)
. There are only three commands you should know:

```bash
# Init new venv
python3 -m venv /path/to/new/environment

# For example if you want to init a new venv called env at the current location
python3 -m venv env

# Activate the env (on Mac or Linux)
source env/bin/activate

# On Windows
source env/Scripts/activate

# Deactivate
deactivate

# On Windows
...
```

## pip

[pip](https://pypi.org/project/pip/) is the Python package manager. You can read through
the [Getting Started](https://pip.pypa.io/en/stable/getting-started/) guide at your leisure. I focus on the key commands
that you should know. The basic usage is `pip install package`. However, this installs the package to the system's
Python site-packages directory (so globally). If you have several Python versions installed (e.g. on linux you usually
have both python2 and python3) then it is not clear to which Python version the pip command installs to as pip as well
as pip3 are associated with one particular Python version. So therefore I would suggest that you call pip as a module
starting with your preferred Python version like so:

```Python
python3 - m
pip
install
package
```

Update a package (for example pip) with the following command:

```Python
python3 - m
pip
install - -upgrade
pip
```

Once you have activated the virtual environment, there is no need to call pip as a module. You can simply
use `pip install package`.

You can list installed packages with `pip list`. If you want to make your environment reproducible, you can write the
current state to a `requirements.txt` file like so:

```bash
pip freeze > requirements.txt
```

Remark: The `>` operator pipes the output of the LHS into the file on the RHS.

*<span style="color:red">However, this is bad practice, as it will just dump any installed python package into
requirements.txt [Here is even more background](https://towardsdatascience.com/stop-using-pip-freeze-for-your-python-projects-9c37181730f9)
.</span>*

Instead, install pipreqs into your venv:

```bash
pip install pipreqs
```

And then ask it to create a `requirements.txt` for you:

```bash
pipreqs --force
```

This will create a much smaller `requirements.txt`, as it only lists *primary* dependencies, which then in turn come
with their own, well-defined dependencies.

Remark: `--force` allows pipreqs to overwrite an existing `requirements.txt`.

## A poor humans build pipeline:

Code bases tend to grow quickly. In such a case, keeping it nice and tidy is very helpful,
since code that is *clean*, *understandable* and easy to *maintain* can save you a lot of time in your future.

Ideally, you should be able to pick up any of your projects after half a year or longer and with little setup time,
capable of expanding or adapting your previous work. To facilitate this, we provide you with some cool packages, that
allow you to keep your code on a constant high level of quality.

We cover the following steps:

* Reformatting (`isort black pipreqs`)
* Checking (`mypy pylint`)
* Scoring (`radon`)
* Building (`build`)
* Installing

### Pre-requisites and script:

Before going into detail, check out the scrip `toolchain.cmd`/`toolchain.sh`. As we will use all the above tools
frequently, we provide you with a script that does each of these steps mentioned for you, when you give it the
appropriate command. However, it requires two three things:

* A `venv` to create it's own `build_venv` from it.
* The `pyproject.toml` file, as many tools need to be configured. We provide you with an example `pyproject.toml` that,
  in our opinion already well configured.
* A project that is structured like the one here, such that code to be packaged resides in `.\\src`

### Formatting:

Formatting code is an art and can be highly subjective. However, if all people in a team were to format their code by
individual preference, the repository is getting messy. To use reformatting in our `toolchain.cmd`/`toolchain.sh`, run:

```bash
toolchain --reformat
```

This command will apply the three following tools, using the config in `pyproject.toml`

#### BLACK

Hence, we rely on `black`:

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Black is inspired by Henry Ford who is often quoted as *"you can have your car in any color you like, as long as its
black"*. 'black' follows the same philosophy, as it allows almost no customisation, leading to consistently formatted
code. Once installed, you can use it to format all the conde in your project at once:

```bash
black -l120 . --exclude=venv,assets
```

#### ISORT

The arguments mean the following: `-l120` restricts lines to be at max 120 characters long. `.` is telling it, that we
want it to reformat all code in this directory and its subdirectories. Finally, we `--exclude` `venv` and `assets`.

Similar to formatting, imports should be arranged and ordered consistently. Meet `isort`:

[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

Once installed, use it like that:

```bash
isort --profile black .\\src\\.
```

Here, we tell isort that we are also using black, which makes sense as otherwise the two tools might contradict each
other.

#### PIPREQS

Finally, last step of our reformatting effort is that we want to keep the `requirements.txt` up to date at all time.
Keeping the dependencies in check with what we actually use in our code is vital for reproducibility. Imagine forgetting
to list a package in the `requirements.txt`. This would make sharing your code a challenge. Install it, and then ask it
to create or update the `requirements.txt` for you:

```bash
isort pipreqs --force .\\src\\.
```

This will create a much smaller `requirements.txt`, as it only lists *primary* dependencies, which then in turn come
with their own, well-defined dependencies. Remark: `--force` allows pipreqs to overwrite an existing `requirements.txt`.

### Checking:

During the process of writing code, we will inevitably make mistakes. Ideally, we catch these as early as possible. We
can check two things without running the code: Validity of our type hints and if we violate some conventions.
To run these two checks sequentially, with `toolchain.cmd`/`toolchain.sh`, run:

```bash
toolchain --check
```

This command will apply the two following tools, using the config in `pyproject.toml`.

#### MYPY

`mypy` is a static type checker for Python. Type checkers help ensure that you’re using variables and functions in your
code correctly. With mypy, add type hints (PEP 484) to your Python programs, and mypy will warn you when you use those
types incorrectly. If you fix all of these warnings you can slap this badge on your readme.md:

[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

Usage is straightforward:

```bash
mypy .\\src\\.
```

#### PYLINT

Pylint is a static code analyser for Python 2 or 3. The latest version supports Python 3.7.2 and above.

Pylint analyses your code without actually running it. It checks for errors, enforces a coding standard, looks for code
smells, and can make suggestions about how the code could be refactored. Pylint can infer actual values from your code
using its internal code representation (astroid). If your code is import logging as argparse, Pylint will know that
argparse.error(...) is in fact a logging call and not an argparse call. Usage:

```bash
pylint .\\src\\.
```

**Note that ideally, you always fix all issues that mypy or pylint report!! This keeps your code clean and tidy**

### Scoring

Ok, we have formatted and *clean* code, but what about its complexity and maintainability?
Use the script to see it:

```bash
toolchain --score
```

#### Radon:

We use `radon` to score the code we have written. It provides metrics for complexity (McCabe’s complexity, i.e.
cyclomatic complexity) and maintainability (Maintainability Index (the one used in Visual Studio)). Assume you have it
installed you can calculate the two as follows:

```bash
radon cc .\\src\\.
```

```bash
radon mi .\\src\\.
```

In the output, you see grades for each evaluated component. Ideally all your grades are A, some B is acceptable, but you
should aim for A in general.

### Building:

Once our code is of high quality, we want to build the package, such that we can ship it. As a part of this process, we
also
run all the tests, that we have available. To do that, run:

```bash
toolchain --build
```

#### BUILD

The `build` package allows us to build a package with the code in `.\\src`. As a result, we find a `.whl` file in
the `.\\dist` folder. This file is our package, and we can install it with

```bash
pip install <yourpackagename>.whl
```

#### UNITTEST

Once we have built our package, we proceed to install it in the `build_venv`, such that we can run all the (unit-)
tests. If the tests pass, we have some certainty that everything went well. To run the tests, we use:

```bash
python -m unittest --autodiscover
```

The unittest package is part of the standard Python library and is the simplest (least fancy) test library. However, for
most purposes, it does the job well, and we can mitigate another dependency. Using `autodiscover` tells the `unittest`
module to discover all unittests automatically. General convention for that is that we have the tests somewhere outside
of `.\\src`. In our case, it is `test_greatest_package`, where we have one unittest-case.

### Installation

The last command,

```bash
toolchain --install
```

is a pure convenience feature, as it allows us to install the latest `.whl` file that is our current package in the
original `venv`. Once it's installed, we can use it like any other package.

## Git version control

> Please read the first three chapters of the [git Book](https://git-scm.com/book/en/v2). It takes maybe 30-60 minutes,
> and I promise you, knowing a little about git will serve you well not only in this course!

Git knows the state of each file in your git repository! But not only that, it also remembers all the previously
committed stages. It knows the differences of all these stages, and they are easily recoverable. Let's explore and
explain some of its core functionality:

```bash
# Change directory (~ stands for your home directory)
cd ~/gitlab

# Create an exmaple directory
mkdir hello_git && cd hello_git

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

# Add the newly hello.txt file to be tracked (i.e. versioned)
git add hello.txt

# Check what happened - read the output!
git status

# Commit with a meaningful message
git commit -m "just testing"
```

So far in this example, we've only worked on our local machine. What if we want to collaborate and share our code? We
first have to initialize a (remote) gitlab repository.

1. Navigate to https://gitlab.ethz.ch/projects/new
2. Click *Show command* and copy it
3. Go back to your terminal and paste it (make sure to be in the `hello_git` repository) and execute
4. See: your local repository has been mirrored on gitlab: https://gitlab.ethz.ch/daniehei/hello_git (replace daniehei
   with your username)

Now the git cycle starts from before. Let's say we want to append a line in hello.txt

```bash
# >> appends whereas > would overwrite
echo "git is awesome" >> hello.txt

# Print file to standard output (i.e. to your console)
cat hello.txt

# Again check the current status
git status

# Ok, hello.txt was modified. But what did we actually do?
git diff

# Great, we want to commit this change
git add hello.txt
git commit -m "important line added"

# Let's broadcast this to the world
git push
```

Check your gitlab repository and explore the GUI (graphical user interface) functionality! For example, navigate to *
Commits* and click on *important line added*.

![important_line](assets/important_line.png)

if you want to share your repository you need to navigate to clone and copy the link (e.g. git@gitlab.ethz.ch:
daniehei/hello_git.git):

![share_repo](assets/share_repo.png)

```bash
# Let's remove our local repository (assume your computer caught fire)
cd ~/gitlab
rm -rf hello_git

# And clone the remote repository
git clone git@gitlab.ethz.ch:daniehei/hello_git.git

# See it is here again
ls
```

In the meantime, your colleague might change something and push it to the gitlab repository. Before you start working on
your local machine, check whether there have been any updates! Do so by `git pull`.

### Summary

- This seems like a lot to remember... `git --help` might help
- The most important commands are:
    - `git init`: Initialize a git repository
    - `git status`: Check the current status
    - `git add file` or `git add .`: Add files or changes to files (the latter adds everything in the current (`.`)
      directory)
    - `git commit -m "message"`: Commit the changes with a meaningful message (it's an art to write meaningful commit
      messages, just write what you did and avoid messages like *changed stuff*)
    - `git push`: Push changes to remote (in our case gitlab)
    - `git clone link`: Clone remote repository
    - `git pull`: Pull potential changes from remote
- Please read the first three chapters of the [git Book](https://git-scm.com/book/en/v2).

> If you are overwhelmed with all this command line awesomeness you may want to use a GUI tool
> such [GitHub Desktop](https://desktop.github.com/). However, I would encourage you to embrace the command line! :) The
> commands discussed so far, can take you very far! If you would like to learn more this might be a
> good [starting point](https://www.learnshell.org/). The terminal is just an interface to interact with our computer.
> Inside the terminal you can run different shells: This is usually `bash` or `zsh` (which are very similar at our level
> of understanding)... If you are a Mac user, you might want to explore the [brew](https://brew.sh/) package manager to
> install and manage software (for example try to install lazygit). On Windows there is a similar package manager such
> as [chocolatey](https://chocolatey.org/). Linux uses `apt` or similar tools.

## PostgreSQL

Fed up with duplicating `.csv` files and send data via mail attachments and wait for large spreadsheets to load in
Excel? Then it is time to learn a little about [PostgreSQL](https://www.postgresql.org/). We are here only touching on
the bare minimum to accomplish our task. So what are we going to do?

You will collect customer survey data on different bus lines in Winterthur (an Origin-Destination survey: Who does
travel with a particular bus from where to where and why?). Each group will ride on a different bus line (potentially on
different days). However, every group will have to analyse all the bus lines. So how will we do it? One strategy would
be that each of the groups digitizes the data collected by paper and pencil. One poor soul (= one of us research
assistants) would then have to collect these individual spreadsheets and consolidate the data into one master file. This
file would then be distributed to the students, that is each student would have a copy of it on their local machines (
all the data is multiplied). Oh no, I've made a mistake in the consolidation: Resend the corrected master file to all
the students... We can do better than this and host the data at a generally (by you students) accessible server.

> As already mentioned, you can of course also run a postgres server on your local machine. You are encouraged to try
> setting a DB up on your local computer.

Check out the following `sql` script (you find it under `PuvIntro/sql/example.sql`).

```sql
-- Fresh start
DROP TABLE IF EXISTS daniehei;

-- Init table
CREATE TABLE daniehei
(
    NAME varchar PRIMARY KEY,
    AGE  smallint
);

-- Copy from file
\
copy daniehei( NAME, AGE ) FROM '~/gitlab/PuvIntro/sql/daniehei.csv' delimiter ';' CSV HEADER;
```

You literally understand what it does from the syntax: It drops the table *daniehei* if it already exists and then
creates (re-initializes) the table *daniehei* which has two columns *name* and *age*. The *name* column is of
type `varchar` and is our primary key (every table should have a primary key) and the *age* column is of type `smallint`
. You can read all about the available data types in the official
documentation [here](https://www.postgresql.org/docs/current/datatype.html). Finally, we populate the data by copying it
from the `daniehei.csv` which is just a plain .csv looking like this:

```csv
name;age
Daniel;30
```

But how do we actually execute the script? For this, I have written a simple bash script that helps you run it. Don't
worry, all you have to do in the exercise is specifying the sql script, and I will show you how to run it.

> Remark: You could also achieve the same thing (i.e. initialize and populate the table) all from within Python with
> the `psycopg2` package. But we thought it would be illustrative to use the actual sql syntax to do it. If you want to
> follow the pythonic way, [this]([psycopg2](https://www.psycopg.org/psycopg3/docs/basic/usage.html) link gets you
> started.

To run the script you can issue the following command:

```bash
cd sql

# Enter your pw when prompted
sh run_sql.sh username example.sql
```

> Each of you gets a username (guest_x) with a password which you are required to substitute, resp. enter when prompted.

If you are interested please try to understand the `run_sql.sh` script.

### psycopg2

Now we can easily communicate with the DB from our Python scripts with help
of [psycopg2](https://www.psycopg.org/psycopg3/docs/basic/usage.html). See the `query_example` from
the `greatest_package.postgres` module for an example. Make sure to understand it!

```python
from greatest_package import postgres as pg

# Check out the documentation of the function to pass the appropriate arguments
pg.query_example()
```

## Exercise

1. Initialize a new empty repository in your `~/gitlab/` main repo (hint: `mkdir`).
2. Initialize the repository to be a git repository (hint: `git init .`).
3. Write an sql script that initializes a new table called `<your eth-abbr>_message` containing only one
   column `message` and populate it with one secret message.
4. Commit the newly created script and add a meaningful commit message (
   hint: `git add . && git commit -m "your message"`).
5. Try to implement the Python package repository structure as in `PuvIntro` or follow
   this [tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/).
6. Initialize a virtual environment as well as make sure to add a `.gitignore` with the environments name.
7. Write a function that queries the newly created table (with `psycopg2`) and prints a message stored in the message
   table (hint: see `src/greatest_package/postgres.py`).
8. Save the dependencies to a `requirements.txt` file (hint: do not
   use `pip freeze > requirements.txt` [why](https://towardsdatascience.com/stop-using-pip-freeze-for-your-python-projects-9c37181730f9)
   .
7. Commit your awesome package.
8. Initialize a new gitlab repository (hint: just navigate to *Create new project* https://gitlab.ethz.ch/projects/new
   and copy and paste the code that pops up when you click *Show command* - you can paste the command into your terminal
   and execute it).
9. Share your code with the message recipient (hint: See picture above where to find the link).
10. Clone someone else's awesome package and try to call the function printing the secret message (hint: Don't forget to
    install the dependencies with `python3 -m pip install -r requirement.txt`).
