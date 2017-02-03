"""
Suppose the cover price of book is $24.95, but book store gets 40% discount.
Shipping costs $3 for the first copy and 75 cents for each additional copy
what is the total wholesale cost of 60 copies?
"""

cost_per_book  = 24.95
discount_percentage = 40
final_cost_of_book = cost_per_book - (cost_per_book * discount_percentage/100)
total_num_books = 60.0
cost_of_first_shipment = 3.0
cost_of_other_shipment = 0.75 * (total_num_books - 1)

total_cost = (total_num_books * final_cost_of_book) + cost_of_first_shipment + cost_of_other_shipment

print "Total wholesale cost of 60 copies is %d" % total_cost
