#change the value of a key 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict['year'] = 2018 
print(thisdict,'\n')
#update()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({'year': 2018})
print(thisdict)