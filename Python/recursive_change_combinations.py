# returns unique combinations of change for a given value (in cents)
def changeComb(val):
    cents = {
        'Q':25,
        'D':10,
        'N':5,
        'P':1
        }
    
    results = []

    def helper(comb):
        # calculate remainder
        s = 0
        for c in comb:
            s += cents[c]
        rem = val - s

        # if remainder == 0, add combination to results
        if rem == 0:
            results.append(comb)

        # else for every coin value <= remainder and <= previous coin, add to string and run helper on it
        else:
            for c in cents:
                if cents[c] <= rem:
                    new_comb = comb + c
                    if len(comb) == 0:
                        helper(new_comb)
                    elif cents[c] <= cents[comb[-1]]:
                        helper(new_comb)

    helper('')

    #converts strings into dictionaries for easier reading
    combinations = []
    for string in results:
        d = {}
        for coin in cents:
            d[coin] = string.count(coin)
        print(d)
        combinations.append(d)
            
    return combinations

            
            
        
