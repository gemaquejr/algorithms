def is_palindrome_iterative(word):
    """Faça o código aqui."""
    if not word:
        return False
    lengh_of_word = len(word)
    start = 0
    end = lengh_of_word - 1
    while start < end:
        if word[start] != word[end]:
            return False
        start += 1
        end -= 1

    return True
