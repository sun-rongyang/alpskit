# 
#  Author: Rongyang Sun <sun-rongyang@outlook.com>
#  Creation Date: 2018-07-08 21:01
#  
#  Description: alpskit project. Module for data collection and
#               format conversion.
# 
import pyalps

import json

import numpy as np

def data_set_to_jss(data_set):
  """Convert DataSet obj to a json string.

  :data_set: pyalps.DataSet
  :returns: str
      JSON object string.

  """
  return json.dumps(data_set, cls=DataSetJSONEncoder, indent=2)


def jss_to_data_set(jss):
  """Convert js string to a DataSet obj.

  :jss: str
      JSON formatted string.
  :returns: pyals.DataSet

  """
  return json.loads(jss, cls=DataSetJSONDecoder)


def data_set_to_js(data_set, js):
  """Convert DataSet obj to a json string and save to json file.

  :data_set: pyalps.DataSet
  :js: str
      JSON file name.
  :returns: int
      0

  """
  jss = data_set_to_jss(data_set)
  with open(js, 'w') as fp:
    fp.write(jss)
  return 0


def js_to_data_set(js):
  """TODO: Docstring for js_to_data_set.

  :js: str
      JSON file name.
  :returns: TODO

  """
  with open(js, 'r') as fp:
    jss = fp.read()
  return jss_to_data_set(jss)
  
  


class DataSetJSONEncoder(json.JSONEncoder):
  # Override the default method to encode DataSet obj.
  def default(self, obj):
    if isinstance(obj, pyalps.DataSet):
      x = obj.x
      y = obj.y
      props = obj.props
      if isinstance(x, np.ndarray): x = x.tolist()
      if isinstance(y, np.ndarray): y = y.tolist()
      return {'DataSet': [{'x': x},
                          {'y': y},
                          {'props': props}]}
    else:
      return super().default(self, obj)


class DataSetJSONDecoder(json.JSONDecoder):
  def __init__(self, *args, **kwargs):
    # create object_hook method to decode DataSet object.
    json.JSONDecoder.__init__(self,
                              object_hook = self.object_hook,
                              *args,
                              **kwargs)

  def object_hook(self, obj):
    if 'DataSet' not in obj:
      return obj
    data_set_list = obj['DataSet']
    return pyalps.DataSet(x=np.array(data_set_list[0]['x']),
                          y=np.array(data_set_list[1]['y']),
                          props=data_set_list[2]['props'])
