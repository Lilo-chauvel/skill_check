from User import User

jean = User("Jean",1)
paul = User("Paul",2)

print(
    f"{jean.name} have this id : {jean.id}" +
    "\n" + f"{paul.name} have this id : {paul.id}"
)