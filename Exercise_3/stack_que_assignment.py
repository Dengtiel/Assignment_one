"""
RWANDA DATA STRUCTURES - STACK & QUEUE SOLUTIONS
Assignment: Stack and Queue Implementation with Rwanda Examples
Author: Deng Mayen Deng Akol | Course: Data Structures | University of Rwanda
"""

import time

def print_question_header(question_num, title):
    print("\n" + "="*60)
    print(f"QUESTION {question_num}: {title}")
    print("="*60)

def print_answer_header(title):
    print(f"\n>>> ANSWER: {title}")
    print("-" * 40)

# ================== STACK IMPLEMENTATION ==================
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
        print(f"PUSH '{item}' → Stack: {self.items}")
        
    def pop(self):
        if not self.is_empty():
            removed = self.items.pop()
            print(f"POP '{removed}' → Stack: {self.items}")
            return removed
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def display(self):
        return self.items.copy()

# ================== QUEUE IMPLEMENTATION ==================
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
        print(f"ENQUEUE '{item}' → Queue: {self.items}")
    
    def dequeue(self):
        if not self.is_empty():
            removed = self.items.pop(0)
            print(f"DEQUEUE '{removed}' → Queue: {self.items}")
            return removed
        return None
    
    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def display(self):
        return self.items.copy()

# ================== CIRCULAR QUEUE IMPLEMENTATION ==================
class CircularQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.items = [None] * max_size
        self.front_idx = -1
        self.rear_idx = -1
        self.count = 0
    
    def enqueue(self, item):
        if self.count >= self.max_size:
            return False
        
        if self.front_idx == -1:
            self.front_idx = 0
            self.rear_idx = 0
        else:
            self.rear_idx = (self.rear_idx + 1) % self.max_size
        
        self.items[self.rear_idx] = item
        self.count += 1
        return True
    
    def dequeue(self):
        if self.count == 0:
            return None
        
        item = self.items[self.front_idx]
        self.items[self.front_idx] = None
        
        if self.count == 1:
            self.front_idx = -1
            self.rear_idx = -1
        else:
            self.front_idx = (self.front_idx + 1) % self.max_size
        
        self.count -= 1
        return item

print("*"*70)
print("RWANDA DATA STRUCTURES ASSIGNMENT - STACK & QUEUE SOLUTIONS")
print("University of Rwanda - Computer Science Department")
print("*"*70)

# ================== STACK QUESTIONS ==================

print_question_header("1", "UR EXAM SYSTEM - STACK OPERATIONS")
print("UR exam system pushes answers ['Answer1', 'Answer2', 'Answer3'].")
print("After 2 pops, what is left?")

print_answer_header("UR Exam System Implementation")
ur_stack = Stack()
answers = ["Answer1", "Answer2", "Answer3"]

print("Initial setup - pushing answers:")
for answer in answers:
    ur_stack.push(answer)
    time.sleep(0.8)

print(f"\nStack before pops: {ur_stack.display()}")
print("\nPerforming 2 pop operations:")

# First pop
first_pop = ur_stack.pop()
time.sleep(0.8)

# Second pop  
second_pop = ur_stack.pop()
time.sleep(0.8)

print(f"\n✓ FINAL ANSWER: After 2 pops, what is left? → {ur_stack.display()}")
stack_answer_1 = ur_stack.display()

# ==================

print_question_header("2", "MOMO APP NAVIGATION - STACK OPERATIONS")
print("MoMo app pushes ['Select Service', 'Enter Amount', 'Confirm'].")
print("Pop once. Which is undone?")

print_answer_header("MoMo App Stack Implementation")
momo_stack = Stack()
momo_steps = ["Select Service", "Enter Amount", "Confirm"]

print("User navigation - pushing steps:")
for step in momo_steps:
    momo_stack.push(step)
    time.sleep(0.8)

print(f"\nStack before pop: {momo_stack.display()}")
print(f"Top of stack (current step): '{momo_stack.peek()}'")

print("\nUser presses BACK (pop operation):")
undone_step = momo_stack.pop()
time.sleep(0.8)

print(f"\n✓ FINAL ANSWER: Which is undone? → '{undone_step}'")
print(f"User returned to: '{momo_stack.peek()}'")
stack_answer_2 = undone_step

# ==================

print_question_header("3", "BRACKET BALANCING - STACK ALGORITHM")
print("Use stack operations to check if [ (2+3) – (4+5) ] is balanced.")

print_answer_header("Balanced Brackets Checker")
def check_balanced_brackets(expression):
    bracket_stack = Stack()
    opening = "([{"
    closing = ")]}"
    pairs = {"(": ")", "[": "]", "{": "}"}
    
    print(f"Checking expression: {expression}")
    print("\nStep-by-step analysis:")
    
    for i, char in enumerate(expression):
        if char in opening:
            bracket_stack.push(char)
            print(f"Step {i+1}: Found opening '{char}' - pushed to stack")
            time.sleep(0.6)
        elif char in closing:
            if bracket_stack.is_empty():
                print(f"Step {i+1}: Found closing '{char}' but stack is empty - NOT BALANCED")
                return False
            
            top = bracket_stack.pop()
            if pairs[top] == char:
                print(f"Step {i+1}: Found closing '{char}' - matches '{top}' ✓")
            else:
                print(f"Step {i+1}: Found closing '{char}' - doesn't match '{top}' ✗")
                return False
            time.sleep(0.6)
    
    is_balanced = bracket_stack.is_empty()
    print(f"\nFinal stack state: {bracket_stack.display()}")
    return is_balanced

expression = "[ (2+3) – (4+5) ]"
result = check_balanced_brackets(expression)
print(f"\n✓ FINAL ANSWER: Expression is {'BALANCED' if result else 'NOT BALANCED'} → {result}")
stack_answer_3 = result

# ==================

print_question_header("4", "STACK REFLECTION")
print("Why is stack suitable for temporary storage in problem-solving?")

print_answer_header("Stack Suitability Analysis")
print("Stack is suitable for temporary storage because:")
print("\n1. LIFO Principle (Last In, First Out):")
print("   - Matches natural problem-solving approach")
print("   - Solve innermost/most recent problems first")
print("   - Perfect for nested operations")

print("\n2. Automatic Backtracking:")
print("   - Easy undo operations (like MoMo app)")
print("   - Natural reversal of operations")
print("   - Efficient memory management")

print("\n3. Recursive Problem Handling:")
print("   - Function call management")
print("   - Nested bracket checking")
print("   - Expression evaluation")

print("\n4. Memory Efficiency:")
print("   - O(1) access to most recent data")
print("   - No need to search through all data")
print("   - Automatic cleanup of temporary data")

print("\n✓ FINAL ANSWER: Stack's LIFO nature makes it perfect for temporary")
print("  storage where the most recent data needs to be processed first.")

# ================== QUEUE QUESTIONS ==================

print_question_header("5", "NYABUGOGO TERMINAL - QUEUE OPERATIONS")
print("In Nyabugogo terminal, 5 buses line up. After 1 departs, which is at front?")

print_answer_header("Nyabugogo Bus Terminal Queue")
nyabugogo_queue = Queue()
buses = ["Bus1", "Bus2", "Bus3", "Bus4", "Bus5"]

print("Buses lining up at terminal:")
for bus in buses:
    nyabugogo_queue.enqueue(bus)
    time.sleep(0.6)

print(f"\nQueue before departure: {nyabugogo_queue.display()}")
print(f"Front bus: '{nyabugogo_queue.front()}'")

print("\nOne bus departs (FIFO - First In, First Out):")
departed_bus = nyabugogo_queue.dequeue()
time.sleep(0.8)

print(f"\n✓ FINAL ANSWER: Which is at front? → '{nyabugogo_queue.front()}'")
queue_answer_1 = nyabugogo_queue.front()

# ==================

print_question_header("6", "BK ATM QUEUE - QUEUE OPERATIONS")
print("At BK ATM, 3 customers join queue. After 1 withdrawal, who is next?")

print_answer_header("BK ATM Customer Queue")
bk_queue = Queue()
customers = ["Customer1", "Customer2", "Customer3"]

print("Customers joining ATM queue:")
for customer in customers:
    bk_queue.enqueue(customer)
    time.sleep(0.6)

print(f"\nQueue before withdrawal: {bk_queue.display()}")
print(f"Currently being served: '{bk_queue.front()}'")

print("\nOne customer completes withdrawal:")
served_customer = bk_queue.dequeue()
time.sleep(0.8)

print(f"\n✓ FINAL ANSWER: Who is next? → '{bk_queue.front()}'")
queue_answer_2 = bk_queue.front()

# ==================

print_question_header("7", "KIGALI BUS EFFICIENCY - QUEUE COMPARISON")
print("Compare efficiency of linear vs circular queue for rotating buses in Kigali.")

print_answer_header("Linear vs Circular Queue Efficiency Analysis")

print("SCENARIO: Kigali city buses rotating through routes")
print("Routes: Nyabugogo → Kimisagara → Town → Airport → (repeat)")

print("\n1. LINEAR QUEUE ANALYSIS:")
print("   Structure: [Route1, Route2, Route3, Route4]")
print("   Problem after dequeue: [_, _, _, _] ← Empty spaces")
print("   Memory Usage: WASTEFUL - unused array positions")
print("   Reset Required: YES - need to shift or recreate array")
print("   Time Complexity: O(n) for reset operations")
print("   Space Efficiency: LOW - memory fragmentation")

print("\n2. CIRCULAR QUEUE ANALYSIS:")
print("   Structure: Circular array with front/rear pointers")
print("   After operations: Continuous rotation without waste")
print("   Memory Usage: OPTIMAL - reuses all positions")
print("   Reset Required: NO - automatic wraparound")
print("   Time Complexity: O(1) for all operations")
print("   Space Efficiency: HIGH - 100% memory utilization")

print("\n3. PRACTICAL KIGALI IMPLEMENTATION:")
print("   ✓ 24/7 bus operations: Circular queue handles continuous rotation")
print("   ✓ Memory efficiency: Critical for embedded bus systems")
print("   ✓ Predictable performance: O(1) operations for real-time scheduling")
print("   ✓ No downtime: No need to reset/reorganize queue")

print("\n✓ FINAL ANSWER: Circular queue is MORE EFFICIENT for rotating")
print("  Kigali buses due to O(1) operations and zero memory waste.")

# ==================

print_question_header("8", "HOSPITAL FIFO REFLECTION")
print("Why is FIFO critical in hospitals for non-emergency patients?")

print_answer_header("FIFO Importance in Rwanda Hospitals")
print("FIFO (First In, First Out) is critical because:")

print("\n1. FAIRNESS & EQUITY:")
print("   - First-come, first-served principle")
print("   - No discrimination based on status/wealth")
print("   - Upholds constitutional right to healthcare")
print("   - Reflects Ubuntu values of equality")

print("\n2. PATIENT TRUST & SATISFACTION:")
print("   - Predictable waiting times")
print("   - Transparent, fair system")
print("   - Reduces patient anxiety and frustration")
print("   - Builds confidence in healthcare system")

print("\n3. LEGAL & ETHICAL COMPLIANCE:")
print("   - Prevents favoritism and corruption")
print("   - Meets international healthcare standards")
print("   - Ensures professional medical ethics")
print("   - Avoids discrimination lawsuits")

print("\n4. OPERATIONAL EFFICIENCY:")
print("   - Organized patient flow")
print("   - Prevents conflicts and chaos")
print("   - Easier staff management")
print("   - Better resource allocation")

print("\n5. SOCIAL ORDER:")
print("   - Maintains peace in waiting areas")
print("   - Prevents queue jumping disputes")
print("   - Ensures orderly healthcare delivery")
print("   - Supports community harmony")

print("\n✓ FINAL ANSWER: FIFO ensures fairness, builds trust, maintains")
print("  order, and upholds ethical healthcare delivery in Rwanda.")

# ================== FINAL SUMMARY ==================

print("\n" + "="*70)
print("ASSIGNMENT SUMMARY - ALL ANSWERS")
print("="*70)

print(f"\nSTACK QUESTIONS:")
print(f"1. UR Exam - After 2 pops: {stack_answer_1}")
print(f"2. MoMo App - Step undone: '{stack_answer_2}'")
print(f"3. Bracket Check - Is balanced: {stack_answer_3}")
print(f"4. Stack Reflection: LIFO perfect for temporary storage & backtracking")

print(f"\nQUEUE QUESTIONS:")
print(f"5. Nyabugogo - Bus at front: '{queue_answer_1}'")
print(f"6. BK ATM - Next customer: '{queue_answer_2}'")
print(f"7. Efficiency - Circular queue MORE efficient for Kigali buses")
print(f"8. Hospital FIFO - Critical for fairness, trust, and social order")

print("\n" + "="*70)
print("✓ ALL QUESTIONS ANSWERED WITH PRACTICAL RWANDA IMPLEMENTATIONS")
print("✓ CODE DEMONSTRATES UNDERSTANDING OF DATA STRUCTURES")
print("✓ REAL-WORLD APPLICATIONS SHOW PRACTICAL KNOWLEDGE")
print("="*70)