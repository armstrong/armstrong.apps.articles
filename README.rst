armstrong.apps.articles
=======================
Provides a basic Article model for Armstrong


Usage
-----
You can use the ``Article`` model from within any project you like.  It's
available to import like this:

::

	from armstrong.apps.articles.models import Article

You have access to both traditional ``Manager`` via the ``objects`` property
as well as a ``PublishedManager`` from `armstrong.core.arm_content`_ via the
``published`` property.

.. _armstrong.core.arm_content: https://github.com/armstrong/armstrong.core.arm_content


Installation & Configuration
----------------------------
You can install the latest release of ``armstrong.apps.articles`` using `pip`_:

::

    pip install armstrong.apps.articles

Make sure to add ``armstrong.apps.articles`` and ``armstrong.apps.content`` to
your ``INSTALLED_APPS``.  You can add this however you like.  This works as a
copy-and-paste solution:

::

	INSTALLED_APPS += ["armstrong.apps.articles", "armstrong.apps.content", ]

``armstrong.apps.content`` is required because ``Article`` extends from the
``Content`` model inside ``apps.content``.

Once installed, you have to run either ``syncdb``, or ``migrate`` if you are
using `South`_.

.. _pip: http://www.pip-installer.org/
.. _South: http://south.aeracode.org/


Contributing
------------

* Create something awesome -- make the code better, add some functionality,
  whatever (this is the hardest part).
* `Fork it`_
* Create a topic branch to house your changes
* Get all of your commits in the new topic branch
* Submit a `pull request`_

.. _pull request: http://help.github.com/pull-requests/
.. _Fork it: http://help.github.com/forking/


State of Project
----------------
Armstrong is an open-source news platform that is freely available to any
organization.  It is the result of a collaboration between the `Texas Tribune`_
and `Bay Citizen`_, and a grant from the `John S. and James L. Knight
Foundation`_.  The first release is scheduled for June, 2011.

To follow development, be sure to join the `Google Group`_.

``armstrong.apps.articles`` is part of the `Armstrong`_ project.  You're
probably looking for that.

.. _Texas Tribune: http://www.texastribune.org/
.. _Bay Citizen: http://www.baycitizen.org/
.. _John S. and James L. Knight Foundation: http://www.knightfoundation.org/
.. _Google Group: http://groups.google.com/group/armstrongcms
.. _Armstrong: http://www.armstrongcms.org/


License
-------
Copyright 2011-2012 Bay Citizen and Texas Tribune

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
