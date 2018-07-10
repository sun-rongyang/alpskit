# 
#  Author: Rongyang Sun <sun-rongyang@outlook.com>
#  Creation Date: 2018-07-07 10:11
#  
#  Description: alpskit project. Module to assist lattice construction.
# 
import pyalps

import subprocess
import re
import os


def gen_sitediff_lattice(paras):
  """Generate site different lattice `GRAPH` for given `LATTICE`.

  :paras: dict
      Parameters dict contain `LATTICE` and its parameters.
  :returns: TODO

  """
  paras_ = dict(paras)   # get a copy.
  basename = '.for_get_graph'
  input_xml = pyalps.writeInputFiles(basename, [paras_])
  graph = _get_graph(input_xml)
  new_graph = _set_sitediff(graph)
  new_lattice_lib = _gen_new_lattice_lib(new_graph, paras_)
  paras['LATTICE_LIBRARY'] = new_lattice_lib
  os.system('rm -rf ' + basename + '*')
  return paras


def _get_graph(input_xml):
  input_xml_list = input_xml.split('.')
  input_xml_list.insert(2, 'task1')
  xml_for_get_graph = '.'.join(input_xml_list)
  graph = subprocess.check_output(['printgraph', xml_for_get_graph])
  return graph


def _set_sitediff(raw_graph):
  dim, verts, edges = _get_graph_paras(raw_graph)
  new_graph = str(raw_graph)
  for id_ in range(1, verts+1):
    vert_sub = '<VERTEX id="{0}" type="0">'.format(id_) 
    new_graph = new_graph.replace(
        vert_sub, vert_sub.replace('type="0"', 'type="{0}"'.format(id_)))
  return new_graph


def _gen_new_lattice_lib(graph, paras_):
  new_lattice_lib_name = './latticelib.xml' 
  graph = graph.replace('<GRAPH', '<GRAPH name="{0}"'.format(paras_['LATTICE']))
  new_lattice_lib = '<LATTICES>\n ' + graph + ' </LATTICES>\n'
  with open(new_lattice_lib_name, 'w') as fp:
    fp.write(new_lattice_lib)
  return new_lattice_lib_name


def _get_graph_paras(graph):
  pattern = r'<GRAPH dimension="(\d+)" vertices="(\d+)" edges="(\d+)">'
  regex = re.compile(pattern)
  mos = regex.search(graph)
  return tuple(int(item) for item in mos.groups())
