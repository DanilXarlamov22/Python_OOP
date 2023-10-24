
def is_correct_bracket(text):
    while '()' in text:
       text = text.replace('()', '')
    if len(text) == 0:
        return True
    return False

txt = input()

print(is_correct_bracket(txt))
