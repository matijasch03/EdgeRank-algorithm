from parse_files import load_statuses

class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.appearance_list = []

class Trie():
    def __init__(self):
        self.root = TrieNode()
        self.text_number = 0

    # METODE DODAVANJA I PRETRAGE
    def insert(self, text):
        words = text.split(' ')
        for word in words:

            current_node = self.root
            for char in word:

                if not char.isalpha():
                    continue

                char = char.lower()

                if char not in current_node.children:
                    current_node.children[char] = TrieNode()
                current_node = current_node.children[char]

            current_node.is_end_of_word = True
            current_node.appearance_list.append(self.text_number)
        self.text_number += 1

    def read(self, current):
        if current == -1:
            current = self.root
        for child in current.children:
            print(child, end='')
            if current.is_end_of_word:
                print(' ', end='')
            else:
                self.read(current.children[child])

    def search(self, word):
        word = word.lower()
        current = self.root
        for char in word:
            if char not in current.children:
                return []
            current = current.children[char]
        return current.appearance_list
        
    def starts_with(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
	    return True


trie = Trie()
status_dict = load_statuses('dataset/original_statuses.csv')

for key in status_dict:
    trie.insert(status_dict[key][5] + '\n' + status_dict[key][1])

input_text = input('Please enter the text: ')
appearance_list = trie.search(input_text)

for i in appearance_list[:11]:
    print('\n' + status_dict[i][5])
    print(status_dict[i][1])

if not appearance_list:
    print("There aren't any posts.")
    
# Example usage
#trie = Trie()
#trie.insert("apple")
#trie.insert("banana")
#trie.insert("app")
#trie.insert("ape")
#
#print(trie.search("apple"))  # True
#print(trie.search("banana"))  # True
#print(trie.search("app"))  # True
#print(trie.search("ape"))  # True
#print(trie.search("orange"))  # False
#
#print(trie.starts_with("app"))  # True
#print(trie.starts_with("ban"))  # True
#print(trie.starts_with("ora"))  # False


