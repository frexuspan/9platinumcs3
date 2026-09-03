# SG4 - Understanding Classes and Objects
## Class Name
The class name is washing machine.
## Class Description
This class functions as a real-life washing machine. It is an electric-powered machine that washes clothing materials, such as underwear, shorts, pants, shirts, and handkerchieves.
## Properties
| Property | Data Type | Description |

| start | Boolean | This is needed to make the machine start |

| open | Boolean | This is needed to open the machine and input clothes |

| close | Boolean | This is needed to close the machine and start washing/get clothes out |

| wash | Boolean | This is needed to activate the machine and start washing |

| time | Integer | This is needed to set the time for how long the machine has to wash the clothes |

| stop | Boolean | This is needed to make the machine stop, automatically making the property start False |

## Methods
| Method | Description |

| ring_when_finished | Has a ring function that rings when the machine is done washing |

| beep_when_button_pressed | Has a beep function that beeps when the user presses a button on the machine |

| select_ringtone | Has a selction of built-in ringtones to choose for the first and second methods (needs either first or second method)|
## Class Diagram
[Class Diagram](images/classDiagram.png)
## Design Explanation
### Why did you choose this class?
I chose this class because i found it funny at first, but i realized that this is very flexible with many options to choose from. So i made a simplified version for my class.
### Which property is the most important? Why?
The property that is the most important is the start property, because all properties (except open, close) would not be able to function without the machine starting.
### Which method is the most useful? Why?
The method that is the most useful is ring_when_finished, because it lets the user know that the machine is done washing the clothes.