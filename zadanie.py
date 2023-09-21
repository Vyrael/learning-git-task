print("Lista zakupów")
shopping_list = {
    "Piekarnia": ["Chleb", "Pączek", "Bułki"],
    "Warzywniak": ['Marchew', 'Seler', 'Rukola']
}
for sklep, rzeczy in shopping_list.items():
  print(f"Idę do {sklep} i kupuję tam: {rzeczy}.")
for rzeczy in shopping_list.values():
  print(f"W sumie kupuję {(len(rzeczy)*(len(shopping_list)))} produktów.")
  break

print('commit1')

print("specjalne pozdrowienia dla mentora")
