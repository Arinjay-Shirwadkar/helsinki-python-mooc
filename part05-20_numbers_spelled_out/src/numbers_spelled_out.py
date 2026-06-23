def dict_of_numbers():
    dic = {}
    
    # Numbers 0 through 19 are unique and best mapped explicitly
    words_0_to_19 = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
        11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
        15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
    }
    
    # Tens prefixes strictly for numbers >= 20
    tens_prefixes = {
        2: "twenty", 3: "thirty", 4: "forty", 5: "fifty",
        6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"
    }
    
    for i in range(0, 100):
        if i < 20:
            dic[i] = words_0_to_19[i]
        else:
            t = i // 10
            u = i % 10
            prefix = tens_prefixes[t]
            
            if u != 0:
                dic[i] = prefix + '-' + words_0_to_19[u]
            else:
                dic[i] = prefix
                
    return dic

if __name__ == "__main__":
    print(dict_of_numbers())