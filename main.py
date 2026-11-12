def is_palindrome(text):
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    word = input('Введите слово или фразу: ')
    if is_palindrome(word):
        print('Это палиндром!')
    else:
        print('Это не палиндром.')