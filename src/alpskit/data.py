# 
#  Author: Rongyang Sun <sun-rongyang@outlook.com>
#  Creation Date: 2018-07-08 21:01
#  
#  Description: alpskit project. Module for data collection and
#               format conversion.
# 
from ._strtool import basename2dict, get_folder

import os
import json
import subprocess

import numpy as np


class MeasuData(object):
  """ A class initialize to contain measurement data, ref ALPS pyalps.DataSet """

  def __init__(self, x=None, y=None, props=None):
    """ use x, y, props data to initialize a MeasuData instance

        :x: x domain data, any object
        :y: y domain data, any object
        :props: properties dict

        """
    self.x = x
    self.y = y
    if props == None:
      self.props = {}
    else:
      self.props = props

  # Use a pyalps.DataSet instance to initialize a MeasuData instance.
  # Usage: measu_data = MeasuData.from_DataSet(data_set)
  @classmethod
  def from_DataSet(cls, data_set):
    x = data_set.x
    y = data_set.y
    props = data_set.props
    return cls(x, y, props)


def measu_data_to_jss(data_set):
  """Convert MeasuData obj to a json string.

  :data_set: MeasuData
  :returns: str
      JSON object string.

  """
  return json.dumps(data_set, cls=MeasuDataJSONEncoder, indent=2)


def jss_to_measu_data(jss):
  """Convert js string to a MeasuData obj.

  :jss: str
      JSON formatted string.
  :returns: MeasuData

  """
  return json.loads(jss, cls=MeasuDataJSONDecoder)


def measu_data_to_js(measu_data, js):
  """Convert MeasuData obj to a json string and save to json file.

  :measu_data: MeasuData
  :js: str
      JSON file name.
  :returns: int
      0

  """
  jss = measu_data_to_jss(measu_data)
  with open(js, 'w') as fp:
    fp.write(jss)
  return 0


def js_to_measu_data(js):
  """Load JSON file and convert to MeasuData obj if possible.

  :js: str
      JSON file name.
  :returns: MeasuData

  """
  with open(js, 'r') as fp:
    jss = fp.read()
  return jss_to_measu_data(jss)
  
  
def get_props(case_dir):
  """Get props dict for given simulation case results.

  :case_dir: str
      Simulation case directory.
  :returns: dict
      props dict.

  """
  try:
    with open(case_dir+'/props.json', 'r') as fp:
      props_dict = json.load(fp)
      return props_dict['props']
  except IOError:
    return basename2dict(os.path.basename(case_dir))


def get_chkp_dirs(case_dir):
  """Get *.chkp diectories from simulation case path.

  :case_dir: str
      Simulation case directory.
  :returns: list
      Each item is a chkp directory in the given simulation case.

  """
  cmd = ['ls', case_dir]
  stdout = subprocess.check_output(cmd)
  try:
    contents = stdout.split('\n')
  except TypeError:
    contents = (stdout.decode('utf-8')).split('\n')
  return list(case_dir +'/'+ item
              for item in contents if item.endswith('.chkp'))



class MeasuDataJSONEncoder(json.JSONEncoder):
  # Override the default method to encode MeasuData obj.
  def default(self, obj):
    if isinstance(obj, MeasuData):
      x = obj.x
      y = obj.y
      props = obj.props
      if isinstance(x, np.ndarray): x = x.tolist()
      if isinstance(y, np.ndarray): y = y.tolist()
      return {'MeasuData': [{'x': x},
                            {'y': y},
                            {'props': props}]}
    else:
      return super().default(self, obj)


class MeasuDataJSONDecoder(json.JSONDecoder):
  def __init__(self, *args, **kwargs):
    # create object_hook method to decode DataSet object.
    json.JSONDecoder.__init__(self,
                              object_hook = self.object_hook,
                              *args,
                              **kwargs)

  def object_hook(self, obj):
    if 'MeasuData' not in obj:
      return obj
    data_set_list = obj['MeasuData']
    return MeasuData(x=np.array(data_set_list[0]['x']),
                     y=np.array(data_set_list[1]['y']),
                     props=data_set_list[2]['props'])
