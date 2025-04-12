.. Lumache documentation master file, created by
   sphinx-quickstart on Thu Apr  3 17:09:22 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _lumache-library:

===============
Lumache Library
===============

**Lumache** (/lu'make/) is a Python library for cooks and food lovers that
creates recipes mixing random ingredients.  It pulls data from the `Open Food
Facts database <https://world.openfoodfacts.org/>`_ and offers a *simple* and
*intuitive* API.

Check out the :ref:`Usage <usage>` section how to install the project and the :ref:`API <api>` section for further information.

.. note::

   This project is under active development.

.. _usage:

Usage
=====

Installation
------------

To use Lumache, first install it using pip:

.. code-block:: console

   (.venv) $ pip install lumache

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

.. _api:

API
===

.. autosummary::
  :toctree: generated

  lumache