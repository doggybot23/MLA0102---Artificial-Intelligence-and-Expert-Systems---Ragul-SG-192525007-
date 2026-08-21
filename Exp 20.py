dob = {
    "ravi": "15-08-2003",
    "rahul": "20-03-2002",
    "anitha": "10-12-2004",
    "priya": "25-06-2003"
}

person = input("Enter person name: ").lower()

if person in dob:
    print("Date of Birth:", dob[person])
else:
    print("Person not found")
