def reverse_lookup(rev1,rev2):
  for key, value in phonebook.items():
      if value == rev2:
        return key
    


phonebook = {
  'Joe': '702-555-6495',
  'Silvio': '504-555-3234',
  'Greta': '213-555-4364',
  'Jill': '415-555-5864'
}

print(reverse_lookup(phonebook, '504-555-3234'))  #--> Silvio's number
print(reverse_lookup(phonebook, '213-555-4364'))  #--> Greta's number
print(reverse_lookup(phonebook, '111-222-3333'))  #--> Nobody's number
