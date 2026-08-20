# Computational Thinking Exercise
## [Smart School Canteen Queue]
**Name:** Franc Alexus G. Pan
**Section:** Platinum
**Last Name:** Pan
**Date:** August 20, 2026

---

## Step 1: Identify the Big Problem
### Main Problem

During lunch break, the canteen gets super crowded and the lines take way too long. Students waste almost their whole break just standing in line, which leaves them with barely any time to eat before their next class starts.

---

## Step 2: Identify the Sub-Problems

1. Everyone crowds around the counter at the exact same time, creating chaotic lines.

2. Paying with cash takes forever because workers have to manually count bills and hand out change.

3. Students wait in long lines only to find out the food they wanted sold out minutes ago.

4. The kitchen staff gets overwhelmed trying to prepare random orders as they come in.

---

## Step 3: Apply Computational Thinking Skills
| Sub-Problem | CT Skill | Proposed Solution |
|---|---|---|

| 1. Everyone crowds around the counter at the exact same time, creating chaotic lines. | **Decomposition**: Splitting the canteen rush into separate steps—ordering, paying, cooking, and pickup—so we can fix the crowd bottleneck at each step individually. | Set up a digital ordering system so students can order from their phones instead of crowding the counter. |

| 2. Paying with cash takes forever because workers have to manually count bills and hand out change. | **Pattern Recognition**: Spotting that cash transactions slow down every single order, while contactless payments take just a second. | Use student ID cards as RFID tap-to-pay cards so payment is instant. |

| 3. Students wait in long lines only to find out the food they wanted sold out minutes ago. | **Abstraction**: Ignoring extra details like exact ingredient counts and only showing students what actually matters: if an item is available or sold out. | Put up a live menu board (or app screen) that automatically updates when food runs out. |

| 4. The kitchen staff gets overwhelmed trying to prepare random orders as they come in. | **Algorithm Design**: Creating a simple step-by-step system for the kitchen to group similar food orders together so they can cook faster. | Send orders directly to a kitchen screen that groups identical meal orders together. |

---

## Step 4: Algorithmic Solution
### Selected Sub-Problem
Sub-Problem 1 & 2: Handling digital ordering, tap-to-pay processing, and queue numbers.

### Pseudocode
START
  SHOW available food items on screen
  GET food choice from student
  
  IF item is available THEN
    CALCULATE total price
    ASK student to tap student ID card
    
    IF card balance >= total price THEN
      SUBTRACT price from card balance
      GIVE student a queue number
      SEND order to kitchen screen
      SHOW "Order placed! Your number is #[Number]"
    ELSE
      SHOW "Not enough balance on card."
    ENDIF
  ELSE
    SHOW "Sorry, item is sold out."
  ENDIF
END