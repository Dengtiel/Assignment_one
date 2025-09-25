
---

# Rwanda Data Structures – Stack & Queue Solutions

**Course**: Data Structures
**Institution**: University of Rwanda – Business Information Technology Department
**Author**: Deng Mayen Deng Akol

---

## 📘 Overview

This project provides a **Python implementation of Stack, Queue, and Circular Queue data structures**, enriched with **real-life Rwanda-based examples**.

The assignment demonstrates how these fundamental data structures can be applied in **practical scenarios**, such as:

* **Exam Systems** (stack storage of answers)
* **Mobile Money (MoMo) app navigation**
* **Balanced bracket checking in mathematics**
* **Nyabugogo bus terminal queuing system**
* **BK ATM customer service queues**
* **Kigali city bus efficiency with circular queues**
* **Hospital patient FIFO management**

---

## ⚙️ Implemented Data Structures

### 1. **Stack (LIFO – Last In, First Out)**

* Implemented using Python lists.
* Key operations: `push`, `pop`, `peek`, `is_empty`, `display`.
* Real-world applications: **UR exam answers, MoMo navigation, bracket balancing**.

### 2. **Queue (FIFO – First In, First Out)**

* Implemented using Python lists.
* Key operations: `enqueue`, `dequeue`, `front`, `is_empty`, `display`.
* Real-world applications: **Bus terminal, ATM customer service**.

### 3. **Circular Queue**

* Implemented with a **fixed-size array**.
* Key operations: `enqueue`, `dequeue` with circular indexing.
* Real-world applications: **Kigali bus rotations for efficiency**.

---

## 📝 Rwanda-Based Problem Scenarios

| **Question** | **Scenario**                             | **Data Structure**             | **Answer/Insight**                                     |
| ------------ | ---------------------------------------- | ------------------------------ | ------------------------------------------------------ |
| 1            | UR Exam System (answers pushed & popped) | Stack                          | After 2 pops → Remaining answers                       |
| 2            | MoMo App Navigation                      | Stack                          | "Confirm" step undone → Returned to "Enter Amount"     |
| 3            | Bracket Balancing                        | Stack                          | Expression `[ (2+3) – (4+5) ]` is **Balanced**         |
| 4            | Stack Reflection                         | Stack                          | LIFO suitable for **temporary storage** & backtracking |
| 5            | Nyabugogo Bus Terminal                   | Queue                          | After one bus departs, **Bus2** is at front            |
| 6            | BK ATM Queue                             | Queue                          | After one withdrawal, **Customer2** is next            |
| 7            | Kigali Bus Rotation                      | Circular Queue vs Linear Queue | Circular Queue is **more efficient**                   |
| 8            | Hospital FIFO Reflection                 | Queue                          | FIFO ensures **fairness, trust, and order**            |

---

## 🔑 Key Takeaways

1. **Stack Applications**

   * Temporary storage
   * Undo/redo functionality
   * Balanced bracket checking
   * Recursive operations

2. **Queue Applications**

   * Fair queuing (hospitals, ATMs, bus stations)
   * Real-world scheduling (transport, banking)
   * Ensures **FIFO fairness**

3. **Circular Queue Applications**

   * Efficient resource utilization
   * Ideal for **cyclic scheduling** (e.g., Kigali buses)
   * Prevents memory waste of linear queues

---

## 🚀 How to Run

### Prerequisites

* Python 3.x
* No external libraries required

### Run the Program

```bash
stack_queue_assignment.py
```

The program will:

* Demonstrate stack and queue operations step-by-step
* Print Rwanda-based examples with intermediate states
* Summarize results at the end

---

## 📚 Academic Value

This project demonstrates:

* **Strong grasp of core data structures** (Stack, Queue, Circular Queue).
* **Ability to connect theory with practice** using real Rwanda-based applications.
* **Step-by-step algorithmic reasoning** (pushing, popping, enqueuing, dequeuing).
* **Clear academic reflection** on why each data structure is suitable for its use case.

---

## ✅ Final Summary

* **Stacks** → Ideal for **temporary storage** and **backtracking**.
* **Queues (FIFO)** → Ensure **fairness and order** in services like hospitals and ATMs.
* **Circular Queues** → Provide **efficiency and continuous scheduling** for systems like Kigali buses.

This assignment merges **computer science theory** with **Rwanda’s practical scenarios**, making data structures both understandable and relatable.
