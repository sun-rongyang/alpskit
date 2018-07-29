# 
#  Author: Rongyang Sun <sun-rongyang@outlook.com>
#  Creation Date: 2018-07-07 22:06
#  
#  Description: alpskit project. Private module to manipulate strings.
# 
from collections import OrderedDict
import json


def gen_basename(paras, keys=[],  suffix=''):
  """Generate basename from parameters dict.

  :paras: dict
      Parameters dict for the simulation case.
  :keys: list
      Search these keys in parameters dict to create the basename string.
  :suffix: str
      Any string as suffix term.
  :returns: str
      Basename string.

  """
  paras_ = dict(paras)
  basename_snippets = []
  for key in keys:
    basename_snippets.append(_get_name_snippet(paras_, key))
  if suffix != '': basename_snippets.append(suffix)
  basename = '_'.join(basename_snippets)
  return basename


def get_basename(name_str, suffixs=1):
  """Get basename from a name string

  :name_str: str
      A name string.
  :suffixs: int
      The number of suffix parts. Eg. for foo.bar.baz, suffixs = 2
  :returns: str
      The basename string.

  """
  ns = str(name_str)
  rightmost = ns.split('/')[-1] 
  file_name_parts = rightmost.split('.')
  return '.'.join(file_name_parts[:-suffixs])


def get_folder(name_str):
  """Get related folder string from a path name.

  :name_str: str
      A name string.
  :returns: str
      The folder name string.

  """
  ns = str(name_str)
  if '/' not in ns: return '.'
  folder_levels = ns.split('/')[:-1]
  return '/'.join(folder_levels)


def getlabel(measu_data, keys):
  """Get label string from a MeasuData obj with format:
     'key1=val1 key2=val2 key3=val3'

    :measu_data: MeasuData obj
        Contain measurement data.
    :keys: str or list
        A (list of ) str, each one is an item of the label.
    :returns: str
        The label string.

    """
  if not isinstance(keys, list):
    keys = [keys]
  label = ''
  for key in keys:
    try:
      label += key + '=' + str(measu_data.props[key]) + ' '
    except KeyError:
      label += key + '=' + 'None' + ' '

  return label


def get_fig_name(measu_data, keys):
  """Get figure name string from MeasuData obj(s) with the format:
     'key1=val1_key2=val21-val22_key3=val3'
     '_' and '-' in val# are removed.
     '.' in the final fig name string are also removed.

    :measu_data: alpskit.data.MeasuData
    :keys: list
        A list of keys to generate figure name.
    :returns: str
        Figure name string.

    """
  if not isinstance(measu_data, list): measu_data = [measu_data]
  if not isinstance(keys, list): keys = [keys]
  paras_dict = OrderedDict()
  for key in keys:
    paras_dict[key] = []
    for case in measu_data:
      paras_dict[key].append(
          _get_shrunken_name_snippet_val(str(case.props[key]))
          .replace('_', '').replace('-', ''))
  for key, value in paras_dict.items():
    if value[1:] == value[:-1]:
      paras_dict[key] = [value[0]]
  fig_name_list = []
  for key, value in paras_dict.items():
    para_item = '-'.join(value)
    fig_name_list.append(key + '=' + para_item)

  return ('_'.join(fig_name_list)).replace('.', '_')


def basename2dict(bn):
  """Switch formatted basename like 'key1=val1_key2=val2' to a dict:
     {'key1':val1, 'key2':val2}

  :bn: str
      Formatted basename string.
  :returns: dict
      The switched dict.

  """
  tmp_list = bn.split('_')
  nokey_num = 0   # Initialize non-key item number.
  key_val_dict = {}
  for key_val in tmp_list:
    if '=' not in key_val:
      key_val = '#{0}'.format(nokey_num) +'='+ key_val
      nokey_num += 1
    key_val_list = key_val.split('=')
    key = key_val_list[0]
    val = key_val_list[1]
    try:
      val = int(val)
    except ValueError:
      try:
        val = float(val)
      except ValueError:
        val = str(val)
    key_val_dict[key] = val
  return key_val_dict


def basename2jss(bn, key):
  """Switch a formatted basename like 'key1=val1_key2=val2' to a JSON string
     with 2 spaces indent:

        {
          key: {
            "key1": val1,
            "key2": val2
          }
        }

  :bn: str
      Formatted basename string.
  :key: The leader key.
  :returns: TODO

  """
  bn_dict = basename2dict(bn)
  return json.dumps({key: bn_dict}, indent=2)


def _get_name_snippet(paras, key):
  name_snippet_key = key.replace('_', '')
  try:
    val = _get_shrunken_name_snippet_val(str(paras[key]))
    return name_snippet_key +'='+ val
  except KeyError:
    return name_snippet_key +'='+ 'TBA'


def _get_shrunken_name_snippet_val(raw_str, max_len=7):
  if ' ' in raw_str:
    snips = raw_str.split(' ')
    if len(raw_str.replace(' ', '')) > max_len:
      shrunken_snips = []
      for snip in snips:
        if len(snip) > 3:
          shrunken_snips.append(snip[0:3])
        else:
          shrunken_snips.append(snip)
      return ''.join(shrunken_snips)
    return ''.join(snips)
  else:
    return raw_str.replace('_', '')
