def grocery_budget(grocery_list, budget):

  #Base case 
  if budget < 0 :
    return []

  if not grocery_list:
    return [ [] ]

  current_item_name,current_item_price = grocery_list[0]
  remaining_items = grocery_list[1:]

  all_ways = []
  
  for way_with_current in grocery_budget(remaining_items,budget -  current_item_price):
    way_with_current.append(current_item_name)
    all_ways.append(way_with_current)
    
  all_ways+=grocery_budget(remaining_items,budget)

  return all_ways
    
  


  
    
  