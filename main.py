from stats import get_num_words, character_count, dict_sort
import sys
    
def main():    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys._ExitCode(1)
    
    add = sys.argv[1]
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {add}...")
    
    temp = get_num_words(add)
    temp2 = temp.split()
    
    print("----------- Word Count ----------")
    print(f"Found {len(temp2)} total words")
    
    print("--------- Character Count -------")
    
    dict = character_count(temp)
    sorted_dict = dict_sort(dict)
    
    for d in sorted_dict:
        for key, value in d.items():
            if key.isalpha():
                print(f"{key}: {value}")
    
    print("============= END ===============")

main()