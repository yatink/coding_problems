from collections import defaultdict

def build_trie(words):
    trie = {}
    curr = trie
    for word in words:
        for ch in word:
            if ch not in trie:
                trie[ch] = {}
                curr = trie[ch]
        curr['end'] = word 
    return trie


def check_position(board, trie, words):
    board_height = 0
    board_width = 0
    for x in board_width:
        for y in board_height:
            _check_position(board, (x,y), trie, words)
    return words


def _check_position(board, position, trie, words):
    # Check the elements in the trie and whether the (next) positions have them
    next_positions = defaultdict(list)
    for ch, (x,y) in next_positions:
        next_positions[ch].append((x,y))
    next_positions = [(x,y, ch)]
    if 'end' in trie:
        words.append(trie['end'])
    
    candidates = trie.keys() & next_positions.keys()
    for candidate in candidates:
        for np in next_positions[candidate]:
            check_position(board, np, trie[candidate], words)
    



['abc', 'bac', 'abcd', 'abv']
{'a':{'b': {'c': {'end': True, 'd': {'end': True}}, 'v': {'end': True}}}, 'b': {'a': {'c': {'end': True}}}}