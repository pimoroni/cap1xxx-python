2.0.0
-----

* Enhancement: Repackage to the uv/hatchling method, with PyPI trusted publishing
* Enhancement: Version is derived from the git tag, __version__ from package metadata
* Bugfix: Listener polling no longer stops after one cycle
* Python 3.9 or later, 3.7 and 3.8 support dropped

0.1.4
-----

* Shim Thread.isAlive() for Python >=3.9
* Fix R_INPUT_4_THRESH constant

0.1.3
-----

* Fixed LED rise/fall rate method

0.1.2
-----

* Initial commit to Raspbian apt repository

0.1.1
-----

* Increased delay in polling loop to avoid CPU hogging

0.0.2
-----

* Many little bugfixes, for an actually working library
