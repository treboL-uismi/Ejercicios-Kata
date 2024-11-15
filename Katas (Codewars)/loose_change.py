def loose_change(cents: int) -> dict:
    
    list_cents = [25, 10, 5, 1]
    change_dict = {'Quarters': 0, 'Dimes': 0, 'Nickels': 0, 'Pennies': 0}
    entries = list(change_dict.keys())
    
    if cents < 0:
        return change_dict
    
    i = 0
    for coin in list_cents:
        change_dict[entries[i]] = cents // coin
        cents = cents % coin
        
        if cents == 0:
            break
        else:
            i += 1
    V = [x for x in change_dict.values()]
    RV = V[::-1]
    L = [x for x in change_dict]
    RL = L[::-1]
    
    return dict(zip(RL, RV))
        

if __name__ == "__main__":
    assert loose_change(29) == {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1}
    
    assert loose_change(91) == {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3}
    
    assert loose_change(0) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    
    assert loose_change(-2) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    
    assert loose_change(3.9) == {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0}