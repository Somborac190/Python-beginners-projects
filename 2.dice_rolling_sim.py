import random

x = "y"

while x == "y":
  num_Of_Roll = random.randint(1, 6)

  if num_Of_Roll == 1:
    print("[-----]")
    print("[     ]")
    print("[  0  ]")
    print("[     ]")
    print("[-----]")
  if num_Of_Roll == 2:
    print("[-----]")
    print("[ 0   ]")
    print("[     ]")
    print("[   0 ]")
    print("[-----]")
  if num_Of_Roll == 3:
    print("[-----]")
    print("[     ]")
    print("[0 0 0]")
    print("[     ]")
    print("[-----]")
  if num_Of_Roll == 4:
    print("[-----]")
    print("[0   0]")
    print("[     ]")
    print("[0   0]")
    print("[-----]")
  if num_Of_Roll == 5:
    print("[-----]")
    print("[0   0]")
    print("[  0  ]")
    print("[0   0]")
    print("[-----]")
  if num_Of_Roll == 6:
    print("[-----]")
    print("[0 0 0]")
    print("[     ]")
    print("[0 0 0]")
    print("[-----]")
  x = input("Press y to roll again, n to exit:")
  print("\n")

