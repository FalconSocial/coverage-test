coverage-test
=============

Test Coverage.py. Requires docker-compose.

Meant to test coverage paths, and how you get it to re-write the sources path in the coverage files generated.

.. code:: bash

    [coverage:paths]
    source =
        /app/app
        /c/Users/username/Desktop/Workspace/coverage-test/app

Where I want the :code:`/app/app` to be replaced with :code:`/c/Users/username/Desktop/Workspace/coverage-test/app`.

So to go from this:

.. code::

    !coverage.py: This is a private format, don't read it directly!{"lines":{"/app/app/__init__.py":[1],"/app/app/helpers.py":[1,4,9,11,6]}}

To this:

.. code::

    !coverage.py: This is a private format, don't read it directly!{"lines":{"/c/Users/username/Desktop/Workspace/coverage-test/app/__init__.py":[1],"/c/Users/username/Desktop/Workspace/coverage-test/app/helpers.py":[1,4,9,11,6]}}


Use
---

Call

.. code:: bash

  docker-compose up

And inspect generated coverage files. Change settings in :code:`tox.ini`.
