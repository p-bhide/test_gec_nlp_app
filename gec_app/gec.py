import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

def correct_text(input_text):
    return tool.correct(input_text)