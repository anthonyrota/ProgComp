import string
import sys


def is_trivial(word):
    return len(word) <= 2 or word[0] in 'aeiou' or word in ["for", "has", "have", "she", "that", "the", "this", "will", "with"]


def get_prefix_len(word):
    if word[:2] == 'qu':
        return 2

    return next(i for i, l in enumerate(word) if l in 'aeiou')


def transform(phrase):
    split = phrase.split(' ')
    new_phrase = split.copy()
    special_word_idxs = []
    for i, word in enumerate(split):
        if not is_trivial(word):
            special_word_idxs.append(i)
    if len(special_word_idxs) < 2:
        return phrase
    for i, idx in enumerate(special_word_idxs):
        j = special_word_idxs[(i-1+len(special_word_idxs)) %
                              len(special_word_idxs)]
        p1l = get_prefix_len(split[idx])
        p2l = get_prefix_len(split[j])
        new_phrase[idx] = split[j][:p2l] + split[idx][p1l:]
    return ' '.join(new_phrase)


n = int(sys.stdin.readline())
for _ in range(n):
    print(transform(sys.stdin.readline().strip()))
