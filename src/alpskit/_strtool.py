# 
#  Author: Rongyang Sun <sun-rongyang@outlook.com>
#  Creation Date: 2018-07-07 22:06
#  
#  Description: alpskit project. Private module to manipulate strings.
# 


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

def _get_name_snippet(paras, key):
  name_snippet = key.replace('_', '')
  try:
    val_pre = str(paras[key])
    if ' ' in val_pre:
      val_split = val_pre.split(' ')
      if len(val_pre.replace(' ', '')) > 7:
        snips = []
        for snip in val_split:
          if len(snip) > 3:
            snips.append(snip[0:3])
          else:
            snips.append(snip)
      val = ''.join(snips)
    else:
      val = val_pre.replace('_', '')
    return name_snippet +'='+ val
  except KeyError:
    return name_snippet +'='+ 'TBA'
