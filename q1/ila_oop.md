# Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation is all about bundling a product's data—like its `name`, `price`, and `stock` count—inside a single `Product` object while keeping those details protected from direct edits. Instead of letting any part of the program manually overwrite stock numbers, we use specific functions like `update_stock()` or `set_price()` that check for errors first. This stops bad data from messing up the inventory, like accidentally setting a negative stock amount or typing in a price below zero.

### 2. Abstraction
Abstraction means hiding all the messy backend calculations and showing only the simple actions you actually need to use. For example, when a cashier clicks a `buy_product()` button, the system handles the receipt math, updates the stock count, and logs the sale in the background. The user doesn't need to see or worry about all those underlying steps; they just call one simple function, which keeps the main program clean and easy to work with.

### 3. Inheritance
Inheritance lets us build specialized product types using a main `Product` blueprint as a starting point. A base `Product` class can pass down shared traits like `name` and `price` to child classes like `PerishableProduct` (which adds an `expiration_date`) or `ColdDrink` (which adds a `temperature` setting). This saves a ton of time because we don't have to retype the basic code for every new type of item we bring into the store.

### 4. Polymorphism
Polymorphism allows different types of products to handle the exact same action in their own unique way. If we run a `display_info()` command, a standard item like a notebook might just output its name and price, while a `PerishableProduct` will use its own version of that command to also print its expiration date. This keeps the program super flexible, since the store system can loop through a single list of all items and call `display_info()` without needing messy `if/else` checks for every category.

---

## Reflection
Out of the four pillars, Encapsulation is definitely the most useful for a sari-sari store system. When running a small business, keeping accurate track of money and stock is everything, and one tiny bug that accidentally wipes out stock numbers or changes a price can mess up the whole inventory. By wrapping product properties up tightly and controlling how they get updated, Encapsulation makes sure the store data stays safe, accurate, and protected from human or coding mistakes.