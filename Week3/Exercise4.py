import re


def clean_word(word):
    clean = re.sub(r'\W+', '', word.lower())
    if not clean:
        return None
    return clean


class TrieNode:
    def __init__(self, e = None, n = 0):
        self.element = e
        self.count = n

    def __repr__(self, n = ''):
        result = ''

        if self.count > 0:
            result += n + ": " + str(self.count) + '\n'

        if self.element is not None:
            for key in sorted(self.element):
                result += self.element[key].__repr__(n + key)

        return result

    def insert(self, e):
        if e:
            if self.element:
                if e[0] in self.element.keys():
                    self.element[e[0]].insert(e[1:])
                else:
                    self.element[e[0]] = TrieNode()
                    self.element[e[0]].insert(e[1:])
            else:
                self.element = {e[0]: TrieNode()}
                self.element[e[0]].insert(e[1:])
        else:
            self.count += 1


class Trie:
    def __init__(self, words):
        self.root = None

        for word in words:
            self.insert(word)

    def __repr__(self):
        if self.root:
            return self.root.__repr__()

        return 'Empty trie'

    def insert(self, e):
        if self.root:
            self.root.insert(e)
        else:
            self.root = TrieNode()
            self.root.insert(e)


def frequentietabel1(lst):
    tbl = {}
    for word in lst:
        if word in tbl:
            tbl[word] += 1
        else:
            tbl[word] = 1

    return tbl


def dict_to_file(d, filename):
    file = open(filename, 'w')
    for key in sorted(d):
        # if key:
        file.write(key + ": " + str(d[key]) + '\n')

    file.close()


def trie_to_file(t, filename):
    file = open(filename, 'w')
    file.write(t.__repr__())

    file.close()

words = [clean_word(word) for line in open('grote_file.txt', 'r') for word in line.split() if clean_word(word)]
frequentietabel = frequentietabel1(words)

dict_file = 'grote_file.frequentie.txt'
dict_to_file(frequentietabel, dict_file)

trie = Trie(words)
trie_file = 'grote_file.trie.txt'
trie_to_file(trie, trie_file)

import filecmp
print(filecmp.cmp(dict_file, trie_file))

