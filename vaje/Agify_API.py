import requests
# najdi najstarejse ime iz seznama imen
names = ["Andraž","Luka","Alen"]
biggest = 0
for name in names:
    age = requests.get(f"https://api.agify.io/?name={name}").json()["age"]
    if age > biggest:
        biggest = age
        biggest_name = name
print(biggest_name, "je najstarejši")



