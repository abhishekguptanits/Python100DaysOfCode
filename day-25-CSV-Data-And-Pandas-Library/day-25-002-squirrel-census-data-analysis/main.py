import pandas

data = pandas.read_csv("Squirrel_Data.csv")

gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
gray_squirrels_count = len(gray_squirrels)
print(f"Gray Squirrels Count: {gray_squirrels_count}")

cinnamon_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
cinnamon_squirrels_count = len(cinnamon_squirrels)
print(f"Cinnamon Squirrels Count: {cinnamon_squirrels_count}")

black_squirrels = data[data["Primary Fur Color"] == "Black"]
black_squirrels_count = len(black_squirrels)
print(f"Black Squirrels Count: {black_squirrels_count}")

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
