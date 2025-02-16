thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict["brand"] = "Lord"
print(thisdict)

modelValue = thisdict.get("modl",0)
print(modelValue)
