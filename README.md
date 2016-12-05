plone-buildout
==============

Standard plone buildout implementing extended best practises.

How to use the buildout
=======================

Create it with the zitelab_plone_buildout mr.bob template.

See more info in bobtemplates.zitelab

* cd your-project-name
* python bootstrap_virtualenv.py .
* ./bin/buildout
* This should install standard buildout

How to add your development product in buildout:
================================================
* Go to profiles/project.cfg
* Add your development eggs there
* go to development.cfg
* inside section [sources] add your source of product for example:
* zitelab.helloworld = git git@gitlab.zitelab.eu:documentation/zitelab.helloworld.git


Start on NSK laptop (or any laptop)
================================================

* git pull
* (git checkout file that was changed local)
* . bin/activate #(activate virtual env)
* bin/buildout
* grunt serveTheme #start grunt - a custom sune start grunt script
* bin/zeo start # start zeo
* bin/instance fg #start plone
