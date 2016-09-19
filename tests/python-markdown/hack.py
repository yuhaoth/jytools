import sys
sys.path.insert(0,'.')
from markdown.postprocessors import Postprocessor
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension
from markdown.util import etree
from xml.etree import ElementTree
def pretty_print(ele):
    import xml.dom.minidom
    s=[i.strip() for i in ElementTree.tostring(ele).decode('utf-8').splitlines()]

    xml=xml.dom.minidom.parseString(''.join(s))
    return xml.toprettyxml(indent=' '*4)
def indent(elem, level=0):
    i = "\n" + level*"  "
    j = "\n" + (level-1)*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = j
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = j
    return elem
class MyTreeprocessor(Treeprocessor):
    def run(self, root):
        #~ import xml.etree.ElementTree as etree
        #~ print(type(root))
        import copy
        newroot=etree.Element('div')

        e=root.find('div[@class="toc"]')
        if e is not None:
            newroot.append(e)
            root.remove(e)

        body_top=etree.Element('div',attrib={'class':'container'})
        body_top.append(root)
        root.attrib['class']='markdown-body'
        newroot.append(body_top)
        print('=+'*20,'NEW')
        #~ e=indent(copy.deepcopy(newroot))
        #~ print(etree.tostring(e).decode('utf-8'))
        print(str(pretty_print(newroot)))
        #~ print('=+'*20,'OLD')
        #~ print(etree.tostring(root).decode('utf-8'))
        print('=+'*20)
        return newroot #tree won't be modified
class MyExtension (Extension):
    """ Meta-Data extension for Python-Markdown. """

    def extendMarkdown(self, md, md_globals):
        """ Add MetaPreprocessor to Markdown instance. """
        md.treeprocessors.add("mmm", MyTreeprocessor(), "_end")
        #~ md.postprocesser.add("myprep",
                             #~ MyTreeprocessor(md),
                             #~ ">normalize_whitespace")
import markdown

markdown_str='''
[TOC]
#Head1
##Head2

'''
print(markdown.__file__)
print(markdown.markdown(markdown_str,extensions=['markdown.extensions.toc',MyExtension()]))
