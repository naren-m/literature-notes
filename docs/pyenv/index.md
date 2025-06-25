---
layout: "default"
title: "pyenv"
word_count: 371
created: "2024-11-28T18:24:53.213351"
modified: "2024-11-28T18:24:53.213351"
---
# pyenv

Installing and Managing Python Versions with pyenv on Mac

Python is a popular programming language that is widely used for various applications. However, different projects may require different versions of Python, and managing these versions can be a challenge. pyenv is a tool that allows you to easily install and manage different versions of Python on your system. This tutorial will show you how to install and use pyenv on a Mac.

Step 1: Install Homebrew

The first step is to install Homebrew, a package manager for Mac. Open the terminal and run the following command:

```s
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

Step 2: Install pyenv

Once Homebrew is installed, use it to install pyenv by running the following command in the terminal:

brew install pyenv

Step 3: Configure pyenv

Add the following lines to your shell profile file (e.g. ~/.bash_profile or ~/.zshrc)

```s
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
```

Reload your shell profile file by running the following command in the terminal:

```s
source ~/.zshrc # or ~/.bash_profile
```

Step 4: Verify pyenv installation

Verify that pyenv is installed and working by running the following command in the terminal:

```s
pyenv --version
```

Step 5: Optional: Install pyenv-virtualenv

pyenv-virtualenv is a good plugin to install with pyenv it will allow you to create virtual environments and manage them easily. You can install it by running the command:

```s
brew install pyenv-virtualenv
```

and append the following line to your shell profile file:

```s
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
```

and reload your shell profile file again.

Now, you can use pyenv to install and manage different versions of Python on your Mac. To install a new version of Python, use the following command:

```s
pyenv install <version>
```

To switch to a specific version of Python, use the following command:

```s
pyenv global <version>
```

To see all available versions of Python on your system, use the following command:

```s
pyenv versions
```

`pyenv` makes it easy to switch between different versions of Python and manage them on your Mac. This is particularly useful for working on multiple projects that require different versions of the language.
