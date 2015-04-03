Passwdk
=======

Passwdk is simple console password manager that uses single json file as it's backend.

Usage
-----

Start passwdk using:

.. code-block:: bash

	$ passwdk --help
	usage: passwdk [-h] {add,get}

	positional arguments:
	  {add,get}   action to take

	optional arguments:
	  -h, --help  show this help message and exit

Add password
~~~~~~~~~~~~

Add new password to password file using:

.. code-block:: bash

	$ passwdk add --help
	usage: passwdk add arguments

	optional arguments:
	  -h, --help          show this help message and exit
	  -n NAME             password name
	  -u USER             user name
	  -e EMAIL            email
	  -o NAME VALUE       other informations
	  -t TAGS [TAGS ...]  password tags

Only name is required. Other information may be provided multiple times to store whatever information on password entry. You will be prompted for password. If you want to generate that use application designed to do that, e.g. `pwgen <http://sourceforge.net/projects/pwgen/>`_.

After saving changes to password file POST_ADD_HOOK is executed (if defined). It can be used to e.g. commit changes to git repository storing password file (see passwdkrc.sample). NEW_PASSWORD_NAME and PASSWD_FILE env variable can be used in that hook.

Get password entries
~~~~~~~~~~~~~~~~~~~~

Find password entries by search terms using:

.. code-block:: bash

	$ passwdk get --help
	usage: passwdk get search terms

	positional arguments:
	  search      search terms

	optional arguments:
	  -h, --help  show this help message and exit
	  -p          only password without ending new-line

At least one search term is required. It will print either entries with name equal to one of the search terms or with tags including all search terms.

Configuration
~~~~~~~~~~~~~

Passwdk configuration is stored in $HOME/.passwdkrc file. See `sample configuration file <https://github.com/lkrotowski/passwdk/blob/master/passwdkrc.sample>`_.

Requirements
------------

Passwdk currently is developed and tested on Linux using Python 2.7.

Installation
------------

The latest version is available to install using `pip <http://www.pip-installer.org/>`_:

.. code-block:: bash

	$ pip install https://github.com/lkrotowski/passwdk/zipball/master

Zsh completion
~~~~~~~~~~~~~~

To install Zsh completion copy `_passwdk <https://github.com/lkrotowski/passwdk/blob/master/_passwdk>`_ file to directory listed in $fpath (see `zsh-completions-howto <https://github.com/zsh-users/zsh-completions/blob/master/zsh-completions-howto.org>`_).
