import markdown
md = markdown.Markdown(extensions = ['tables'])
head='''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8"/>
    <meta name="latexinput" content="mmd-tufte-handout-header"/>
    <title>Metadata</title>
    <meta name="author" content="Fletcher T. Penney"/>
    <meta name="version" content="5.1.0"/>
    <meta name="revised" content="2014-04-18"/>
    <link type="text/css" rel="stylesheet" href="css/document.css"/>
    <meta name="latexmode" content="memoir"/>
    <meta name="latexinput" content="mmd-tufte-handout-begin-doc"/>
    <meta name="latexfooter" content="mmd-tufte-footer"/>
</head>
<body>
{markdown}

</body>

</html>

'''

x1='''
<html>
<head>
<title>Collapsing Border Model</title>
<style type="text/css">
table {
  border-collapse:collapse;
  border:1px solid black;
}
th, td {
  border:1px solid black;
  padding:1ex;
}
</style>
</head>
<body id="www-meyerweb-com" class="css">
'''
tail='''
</body>
</html>
'''
with open('example.md','r') as f:
    m=md.convert(f.read())
    print '\n'.join(md.lines)
#~ print x1,m,tail
#~ print head.format(markdown=m)
