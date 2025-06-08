## ▶️ How to Run the Inventory

1. Make sure you have **Python 3** installed.  
2. Run the file:

```bash
python exercise_1_inventory.py
```

3. Use the terminal prompts to interact with the inventory like the examples:
- As costumer:
```python
-=-=-=-=-=-=-=-=-=-=-=-=
Welcome to Inventory 1.0!
-=-=-=-=-=-=-=-=-=-=-=-=
Customer [C]
Staff [S]
Exit [E]
: c
dict_keys(['iphone', 'ipad', 'airpods'])
Enter the product name to check its price: iphone
O valor do iphone 5000
Would you like to check another product? [y/n]: n
```

- As staff:
```python
ustomer [C]
Staff [S]
Exit [E]
: s
Enter the product name: macbook
Enter its price: 12000
Product successfully added!

Would you like to add another product? [y/n]: n
{'iphone': 5000, 'ipad': 7000, 'airpods': 1500, 'macbook': 12000}
```

- To exit:
  
```python
-=-=-=-=-=-=-=-=-=-=-=-=
Welcome to Inventory 1.0!
-=-=-=-=-=-=-=-=-=-=-=-=
Customer [C]
Staff [S]
Exit [E]
: e
Thanks for using Inventory 1.0. See you next time!
```
