#Write a function to finad all words in a grid of letters, given a list of valid words.

def find_words_in_grid(grid, words):
    found_words = set()
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    def search_word(word, r, c, dr, dc):
        for i in range(len(word)):
            nr, nc = r + i * dr, c + i * dc
            if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] != word[i]:
                return False
        return True

    for word in words:
        for r in range(rows):
            for c in range(cols):
                # Check all 8 directions
                for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    if search_word(word, r, c, dr, dc):
                        found_words.add(word)
                        break

    return list(found_words)
