"""
Create a list of tuples. Each tuple should contain an item and its price in float. WAP to sort the tuples in descending order by price
"""
pricelist = (
    (45, 'Bat'),
    (20, 'Wicket'),
    (15, 'Gloves'),
    (10, 'Guard'),
    (60, 'Helmet')
)

sorted_pricelist  = sorted(pricelist)
print(sorted_pricelist)