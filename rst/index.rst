.. impress::
   :func: linear

========================
Nuka
========================

.. slide::
  :class: first

Libérez le devops qui est en vous

.. image:: ./images/pycon.svg
  :align: center

A propos
========

- Je suis Gael « `@gawel_ <https://twitter.com/gawel_>`_ » Pasgrimaud

- Je geek `@bearstech <https://twitter.com/bearstech_>`_

Histoire
========

.. slide::
  :class: bigs

- Hébergement et Infogérance libres depuis 2004

- script à la papa; svn...

- pussh https://github.com/bearstech/pussh

- choix d'outil de déploiement

Existant
========

.. slide::
  :class: bigs

- puppet

- chef

- salt

- ansible

- fabric

Le choix
========

.. image:: ./images/choice.jpg
  :align: center



Photo by `Martin Fisch  <https://www.flickr.com/photos/marfis75/8031936764>`_, CC via Flickr

La douleur
===========

.. image:: ./images/pain.jpg
  :align: center


Photo by `Thomas Hawk <https://www.flickr.com/photos/thomashawk/6247423737/>`_, CC via Flickr

Le bricolage
============

.. image:: ./images/repair.jpg
  :align: center


Photo by `(Mick Baker)rooster  <https://flic.kr/p/foN1Ku>`_, CC via Flickr

You see the light
=================

.. image:: ./images/light.jpg
  :align: center

Photo by `Stuart Williams  <https://flic.kr/p/5JcGgf>`_, CC via Flickr

DIY!
====

- python3

- asyncio

- ssh-agent && ssh

POC
======

- bas niveau (code) mais pas trop

- extensible

- builtin graphs

- testé

- 300 lignes de code


How it works (1/2)
==================

- Host

- Task

- coroutines

How it works (1/2)
==================

- setup: upload de base de code et récupération d'inventaire

- run

- teardown: nétoyage, rendu de graphs

Hosts
=====

- Host

- DockerContainer

- cloud (libcloud / openstack)

A task
=======

.. literalinclude:: ../tasks/__init__.py

Task
=====

- inspection de la stack

- class locale != class distante

- appels shell

- héritage possible

- une tache == une session


Use it (1/2)
============

.. literalinclude:: ../do_tasks.py

Use it (1/2)
============

::

    $ pip install nuka
    $ pip install nuka[full]
    $ pip install \
      -e git+git@github.com:bearstech/nuka.git#egg=nuka[full]

    $ python do_task.py -h

Gantt
=====

.. image:: ./images/gantt.png
  :align: center

Use cases
=========

- Déploiement initial

- Détection de paquet à mettre à jour (~300 machines)

Pourquoi c'est lent ?
=====================

.. image:: ./images/why.jpg
  :align: center

Photo by `Tintin44 <https://flic.kr/p/5JcGgf>`_, CC via Flickr


Perfs
=====

::

    % ./list_hosts | ./benches.py -q -d .01

    Got 296 valid results for 296 hosts in 15.19s

                     min       max       avg     count
    connect     0.000009  0.000057  0.000012       296
    auth_time   0.185978  9.049197  7.170807       296
    timeouts    0.000000  0.000000  0.000000       296

Status
======

- taches de bases (apt, file, shell, user)

- support gpg

Known issues
============

- support debian. autres distro incertaines

- flood de ssh-agent. timeout sur un grand nombre de connections (> 150) en
  fonction du CPU/Net

- docker + systemd

Links
=====

- https://pypi.python.org/pypi/nuka

- https://doc.bearstech.com/nuka/
