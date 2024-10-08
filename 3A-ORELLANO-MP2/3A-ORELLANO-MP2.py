# -*- coding: utf-8 -*-
"""3A-ORELLANO-MP2.ipynb
# **Machine Problem No.2: Implementing a Logic-Based Model in Python**

## **1. Propositional Logic Operations:**
"""

def and_operation(p, q):
    return p and q #Logical conjunction (AND)

def or_operation(p, q):
    return p or q #Logical disjunction (OR)

def not_operation(p):
    return not p #Logical negation (NOT)

def implies_operation(p, q):
    return (not p) or q #Logical implication (IMPLIES)

"""## **2. Evaluate Logical Statements:**"""

print(and_operation(True, False)) # Output: False
print(or_operation(True, False))  # Output: True
print(not_operation(True))        # Output: False
print(implies_operation(True, False)) # Output: False

"""## **3. Extend to Predicate Logic:**"""

def evaluate(statement, values):
    # Replace logical operators with Python equivalents
    statement = statement.replace('and', ' and ').replace('or', ' or ').replace('not', ' not ').replace('=>', ' or not ')
    # Substitute variables with their truth values
    for var, val in values.items():
        statement = statement.replace(var, str(val))
    return eval(statement)

# Evaluating logical statements
print(evaluate('A and B', {'A': True, 'B': False})) # Output: False
print(evaluate('A or B', {'A': True, 'B': False})) # Output: True
print(evaluate('not A', {'A': True})) # Output: False
print(evaluate('A => B', {'A': True, 'B': False})) # Output: False

"""## **4. AI Agent Development:**"""

def forall(predicate, domain):
#Evaluate the universal quantifier (FOR ALL).
    return all(predicate(x) for x in domain)

#Evaluate the existential quantifier (EXISTS).
def exists(predicate, domain):
    return any(predicate(x) for x in domain)

# Define a predicate and a domain
predicate = lambda x: x > 0
domain = [1, 2, 3, -1, -2]

# Evaluate quantifiers
print(forall(predicate, domain))
print(exists(predicate, domain))

class SimpleAIAgent:
    def __init__(self):
        self.condition = True

#Make a decision based on logical conditions.
    def make_decision(self):
        if and_operation(self.condition, True):
            return 'Take action A'
        else:
            return 'Take action B'

# Create an instance of the AI agent
agent = SimpleAIAgent()
print(agent.make_decision())
