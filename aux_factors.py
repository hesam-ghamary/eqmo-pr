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




def req_2(future_years,
          predicate_demand,
          predicate_material_2_prices,
          predicate_prices,
          model_material_1):
    future_costs = []
    future_revenues = []
    future_profits = []

    for i, year in enumerate(future_years.flatten()):
        demand = predicted_demand[i]
        material_2_price = discounted_price(demand, predicted_material_2_prices[i])
        total_material_2_cost = material_2_price * demand
        total_revenue = predicted_prices[i] * demand
        total_cost = total_material_2_cost + model_material_1.predict(np.array([[year]]))[0]
        profit = total_revenue - total_cost
        future_costs.append(total_cost)
        future_revenues.append(total_revenue)
        future_profits.append(profit)

    return future_costs , future_revenues, future_profits