import numpy as np

food = ["gummy bears","stroopwafels","doritos","chips","chocolate chip cookies","noodles","biscuits","raisins","waffles","tortila","sugar blocks","cream soup","m&m’s","popcorn","dates","pringles","mints","liquorish","oreos","mentos","donuts","chocolate","flour","baking soda","peanuts","frozen mango","frozen fries","frozen dough","frozen chicken in sate sauce","frozen pizza","fish sticks","chocolate ice cream","chocolate chips ice cream","strawberry ice cream","vanilla ice cream","frozen cake","frozen spinach","frozen bitterballen","ice tea","cola","chocolate milk","coffee","espresso","coffee milk","black tea","green tea","soda","orange juice","ginger ale","tonic","coffee pads","red bull","generic energy drink","cream cheese","gouda cheese","smoked ham","smoked chicken file","old cheese","goat cheese","applestroop","salami","peanut butter", "garlic spread","strawberry jam","roasted ham"," roast beef","raw salami","hummus","smoked sausage","canned  tomatoes","tomato paste","cocos milk","sunflower oil","green pesto","spaghetti","long rice","basmati rice","white rice","penne","mascarpone","egg noodles","green olives","black olives","tortillas","chilly peppers","cucumber","tangerines","bananas","bell peppers","grapes","broccoli","tomatoes","mango","avocado","apples","onions","cauliflower", "kiwis","spinach","carrots","lemon","green beans","kidney beans","spring onions","blueberries","iceberg salad","celery","beetroot","brussel sprouts","mushrooms","sauerkraut","cinnamon","oregano","salt","sea salt","strawberries","raspberries","corn","corn on the cob","chicken","salmon","beef","lamb","fish","salmon","cod","shrimps","calamari’s","schnitzel","turkey","bacon","prawns","minces meat","meat balls","tuna","pork","milk","yogurt","vla","butter","oil","olive oil","eggs","sour cream"]
print("Take a large pot. Add ", end = '')
n = len(food)
arr = np.random.randint(0, n, 5)
n = len(arr)
count = 0
for i in arr:
  count = count + 1;
  separator = ", "
  if count == n:
    separator = "."
  elif count == n - 1:
    separator = " and "
  print(food[i], separator, end = '' , sep = "")
t = np.random.randint(0, 45)
print(" Boil for", t, "minutes and serve. Lekker!")
