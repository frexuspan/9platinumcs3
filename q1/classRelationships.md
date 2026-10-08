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
## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)
## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](images/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)
## Analysis
### What is the association between your two classes?
The washing machine has only one model, in where and what it is registered on. The association between the two is that the model is the branding, and structure of the washing machine.
### What multiplicity did you choose and why?
One-To-One, because a washing machine can and only will have one model.
### How did you implement the relationship in Python?

### Why did you store an object reference instead of copying its data?

### If your relationship uses many, why is a list appropriate?
