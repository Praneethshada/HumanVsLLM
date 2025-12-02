from buggy_function import replace_specialchar

def test_basic_examples():
    assert replace_specialchar('Python language, Programming language.') == 'Python:language::Programming:language:'

def test_mixed_chars():
    assert replace_specialchar('a b c,d e f') == 'a:b:c:d:e:f'

def test_commas_only():
    assert replace_specialchar('ram reshma,ram rahim') == 'ram:reshma:ram:rahim'
