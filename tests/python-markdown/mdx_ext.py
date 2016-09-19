from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension
import markdown
class MyPreprocessor(Preprocessor):
    def run(self, lines):
        new_lines = []
        for line in lines:
            print '#'*3,line,'#'*3
            #~ m = MYREGEX.match(line)
            #~ if m:
                #~ # do stuff
            #~ else:
                #~ new_lines.append(line)
        return lines
class MetaExtension (Extension):
    """ Meta-Data extension for Python-Markdown. """

    def extendMarkdown(self, md, md_globals):
        """ Add MetaPreprocessor to Markdown instance. """
        md.preprocessors.add("myprep",
                             MyPreprocessor(md),
                             ">normalize_whitespace")
def makeExtension(*args, **kwargs):
    return MetaExtension(*args, **kwargs)
