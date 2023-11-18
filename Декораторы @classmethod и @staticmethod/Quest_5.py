class StrExtension:
    @staticmethod
    def remove_vowels(s):
        vowels = 'aeiouyAEIOUY'
        new_s = ''.join(c for c in s if c not in vowels)
        return new_s

    @staticmethod
    def leave_alpha(s):
        latin = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return ''.join(c for c in s if c in latin)

    @staticmethod
    def replace_all(s, chars, char):
        new_s = ''
        for c in s:
            if c in chars:
                new_s += char
            else:
                new_s += c
        return new_s

print(StrExtension.remove_vowels('Python'))
print(StrExtension.remove_vowels('Stepik'))
print(StrExtension.leave_alpha('Python111'))
print(StrExtension.leave_alpha('__Stepik__()'))
print(StrExtension.replace_all('Python', 'Ptn', '-'))
print(StrExtension.replace_all('Stepik', 'stk', '#'))