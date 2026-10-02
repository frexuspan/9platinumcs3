# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)
## Existing Class
Class: Washing Machine
Description: Functions like a real-life washing machine, which washes clothes and other fabric-related objects.
## New Related Class
Class: Model
Description: This explores the different models of the washing machine, be it Samsung, Sony, or Panasonic.
## Association
Relationship: includes
Explanation: Because a washing machine will always include its model.
## Multiplicity

Multiplicity: One-To-One
Explanation: Because a washing machine can only have one model, a machine cannot have a Samsung-Sony collaboration.

## Analysis

### What is the association between your two classes?
The association between my classes is that a WashingMachine "includes" a Model. The Model class holds the brand details, such as Samsung, Sony, or Panasonic, and the WashingMachine uses that information as part of the machine itself. I connected them because a real washing machine always comes from a specific model, so the two classes belong together in my system. In the UML diagram this is a solid line labeled "includes" between the two classes.

### What multiplicity did you choose and why?
I chose one-to-one (1:1). A washing machine can only have one model, and I decided a model object belongs to exactly one machine in my system, so there is no Samsung-Sony mix. This keeps the design simple and matches how a real machine works. That's why both ends of my association line are labeled 1.

### How did you implement the relationship in Python?
I implemented it by storing a Model object inside the WashingMachine object. The WashingMachine has an attribute `self.model`, which starts as `None`. The method `assign_model(model)` sets it to the actual Model object I pass in. After assigning, I can reach the model's data through the machine, like `machine1.model.brand`.

### Why did you store an object reference instead of copying its data?
I stored the whole Model object so the machine and its model stay connected instead of becoming two separate pieces of data. For example, if I only copied the string "Samsung" into the machine, the machine would not know anything else about its model. With the reference, `machine1.model.brand` always reads the current value from the real Model object. This also shows the relationship is between objects, not just duplicated text.

### If your relationship uses many, why is a list appropriate?
My relationship is one-to-one, so I did not use a list. A single attribute, `self.model`, is enough because a machine only ever has one model. If I changed it to one-to-many, for example one Model used by many machines, a list of WashingMachine objects would be appropriate. Each item in that list would be an actual WashingMachine object, not just a name or number.