#TODO: Function to check if domain supports HTTPS

import os.path, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from errormanager.errormanager import ErrorManager

class URLCompleter:
  def __init__(self):
    self.em = ErrorManager()

  def __CheckVals__(self, *vals):
    for val in vals:
      if not type(val) == type('abc'):
        raise ValueError('Could not complete URL with values "' + str(val) + '".')

  def complete(self, domain, *paths):
    self.__CheckVals__(domain, *paths)

    protocol = '//'
    comp = ''

    paths_ = []
    for path in paths:
      paths_.append(path.lstrip('/'))

    comp = protocol + os.path.join(domain, *paths_)

    return comp