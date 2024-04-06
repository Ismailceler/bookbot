def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = word_count(text)
    count2 = letter_count(text)
    report(count2, book_path, count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def letter_count(text):
    low_text = text.lower()
    words = low_text.split()
    count = {}
    for word in words:
        for char in word:
            if count.get(char) is None:
                new_value = 0
            else:
                new_value = count[char]
            count[char] = new_value + 1 
    return count

def sort_on(dict):
    return dict["num"]
    
def report(dic, path, count):
    list_of_dic = []
    for key in dic:
        new_dic = {}
        new_dic['char'] = key
        new_dic['num'] = dic[key]
        list_of_dic.append(new_dic)

    list_of_dic.sort(reverse=True, key=sort_on)
    print('--- Begin report of {0} ---'.format(path))
    print('{0} words found in the document'.format(count))
    for dic in list_of_dic:
        if dic['char'].isalpha():
            print('The {0} character was found {1} times'.format(dic['char'], dic['num']))

    print('--- End report ---')
        
main()