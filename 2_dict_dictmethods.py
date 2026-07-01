marks = {
     "harry": 90,
     "ron": 85,
     "sezume" : 100,
     0 : "abc"
}
print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"harry":95})
print(marks)

print(marks.get("harry"))
