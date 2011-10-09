#!/usr/bin/env python
#encoding=utf-8 
import sys
import getopt
import codecs
from xml.dom import minidom
from types import *

INPUTFILE = 'chinese.xml'
OUTFILE = "chinese.sql"
PREFIX = "INSERT INTO pre_common_district (`id`, `name`, `level`, `upid`, `usetype`) VALUES ("
POSTFIX = ");\n"
SP = ", "
gid = 0
f = None

def find_parent(child):
    parent = child.parentNode
    if parent is None:
        return None
    elif hasattr(parent, 'hasAttribute') and callable(getattr(parent, 'hasAttribute')) and parent.hasAttribute('Code'):
        return parent
    else:
        return find_parent(parent)



def process_node(node):
    global gid
    global f
    level = 0
    try:
        tagName = node.tagName
    except AttributeError:
        tagName = ''
    name = None
    code = None
    if tagName == u'CountryRegion':
        level = 1
    elif tagName == u'State':
        level = 2
    elif tagName == u'City':
        level = 3

    if hasattr(node, 'hasAttribute') and callable(getattr(node, 'hasAttribute')) and node.hasAttribute('Name'):
        name = node.getAttribute('Name')

    if hasattr(node, 'hasAttribute') and callable(getattr(node, 'hasAttribute')) and node.hasAttribute('Code'):
        code = node.getAttribute('Code')

    if name:
        gid += 1
        node.setAttribute('db_id', str(gid))

        db_level = str(level)
        pn = find_parent(node)
        if pn and hasattr(pn, 'hasAttribute') and callable(getattr(pn, 'hasAttribute')) and pn.hasAttribute('db_level'):
            db_level = str(int(pn.getAttribute('db_level')) + 1)
            node.setAttribute('db_upid', pn.getAttribute('db_id'))
        else:
            node.setAttribute('db_upid', '0')
        node.setAttribute('db_level', db_level)
        #node.setAttribute('usetype', '3')
        outline = PREFIX + node.getAttribute('db_id') + SP + "'" + name + "'" + SP + node.getAttribute('db_level') + SP + node.getAttribute('db_upid') + SP + "3" + POSTFIX
        f.write(outline)

    if node.hasChildNodes():
        # process child nodes, recursively
        for n in node.childNodes:
            process_node(n)
    else:
        return
    

def main():
    global f
    xmldoc = minidom.parse(INPUTFILE)
#    print '=========================='
#    print xmldoc.firstChild.childNodes[1].getAttribute('Name') == u'中国'
    f = codecs.open(OUTFILE, "w", "utf-8")
    process_node(xmldoc.firstChild)
    f.close()

if __name__ == '__main__':
    main()
