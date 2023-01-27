# Referência:Course-Dia 3: Algoritmos que usam dividir e conquistar(quick sort)
def quick_sort(word, start, end):
    if start < end:
        p = partition(word, start, end)
        quick_sort(word, start, p - 1)
        quick_sort(word, p + 1, end)


def partition(word, start, end):
    pivot = word[end]
    delimiter = start - 1

    for index in range(start, end):
        if word[index] <= pivot:
            delimiter = delimiter + 1
            word[index], word[delimiter] = word[delimiter], word[index]

    word[delimiter + 1], word[end] = word[end], word[delimiter + 1]

    return delimiter + 1


def is_anagram(first_string, second_string):
    first_word = list(first_string.casefold())
    quick_sort(first_word, 0, len(first_word) - 1)

    second_word = list(second_string.casefold())
    quick_sort(second_word, 0, len(second_word) - 1)

    first_tuple = "".join(first_word)
    second_tuple = "".join(second_word)

    if not first_string or not second_string:
        return (first_tuple, second_tuple, False)

    return (first_tuple, second_tuple, first_word == second_word)
