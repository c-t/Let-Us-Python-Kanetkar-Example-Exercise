
tuples = [(), ('Jumper','15','8'), (), ('Joker', 'Batman'),  ('Spiderman', 'Venom', '45'), ('',''),()]
print(tuples)

tuples = [t for t in tuples if t]
print(tuples)