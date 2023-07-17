import heapq
from collections import defaultdict

def ladderLength(beginWord, endWord, wordList):
    int_words = defaultdict(list)
    rev_int_words = defaultdict(list)
    for word in wordList:
        for ix in range(len(word)):
            globby = word[:ix]+ "*" + word[ix+1:]
            int_words[globby].append(word)
            rev_int_words[word].append(globby)
    begin_word_globs = [beginWord[:ix]+ "*" + beginWord[ix+1:] for ix in range(len(beginWord))]

    visited = set()
    distances = {}

    unvisited_heap = []
    # Check all neighbours of the beginWord
    for glob in begin_word_globs:
        for word in int_words[glob]:
            distances[word] = 1
            heapq.heappush(unvisited_heap, (distances[word], word))
    visited.add(beginWord)
    while unvisited_heap:
        (dist, word) = heapq.heappop(unvisited_heap)
        if word == endWord:
            return dist
        if word in visited:
            continue
        for glob in rev_int_words[word]:
            for neighbour in int_words[glob]:
                if neighbour in visited:
                    continue
                next_d = dist + 1
                if distances.get(neighbour, float('inf')) > next_d:
                    distances[neighbour] = next_d
                    heapq.heappush(unvisited_heap, (distances[neighbour], neighbour))               
    return 0

if __name__ == '__main__':
    assert ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"]) == 5