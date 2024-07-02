def P_to_F(df, price_list, from_t, to_t, i_f):
    for year in range(len(df), to_t - from_t + 1):
        last_price = price_list[-1]
        new_price = last_price * (1 + i_f)
        price_list.append(new_price)


def single_payment_compund_amount_factor(i, years, start_year):
    return (1 + i) ** (years - start_year)


def pf(price, factor):
    return price*factor




def discounted_price(demand, price):
    if demand > 60:
        return price * 0.82 
    elif demand > 40:
        return price * 0.90 
    elif demand > 20:
        return price * 0.95
    else:
        return price 

