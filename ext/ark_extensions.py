import ark

@ark.renderers.register('md')
def render_markdown(text):
    #the two extras below are here to support syntax highlighting
    #code-friendly: https://github.com/trentm/python-markdown2/wiki/code-friendly
    #fenced-code-blocks: https://github.com/trentm/python-markdown2/wiki/fenced-code-blocks
    import markdown2
    return markdown2.markdown(text,extras=["code-friendly","fenced-code-blocks"])
