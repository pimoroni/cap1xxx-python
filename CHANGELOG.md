1.0.1
-----

* Fix listener polling stopping after one cycle
* Use gpiodevice.Watch/wait_for_edge for the wired ALERT pin
* Packaging: uv-dynamic-versioning, trusted publishing, boilerplate install.sh

1.0.0
-----

* BREAKING: Ported from RPi.GPIO to gpiod/gpiodevice
* BREAKING: Switched from smbus to smbus2
* Repackaged to pyproject.toml/hatch, library/ flattened to repo root
* Added set_sensitivity()/get_sensitivity()
* Fix sensitivity mappings
* Fix call to interrupt_status()

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
