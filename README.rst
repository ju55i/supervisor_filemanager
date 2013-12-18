Filemanager for Supervisor
==========================

Install::

  python setup.py install

Add to your supervisor.conf::

  [rpcinterface:filemanager]
  supervisor.rpcinterface_factory = supervisor_filemanager:make_filemanager_rpcinterface
  path = /etc/supervisor/conf.d

Test from Python::

  >>> s = Server("http://admin:admin@localhost:18200/RPC2")
  >>> s.filemanager.listFiles()
