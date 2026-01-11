# Anastroph Limen Mathematics

## Introduction

**Anastroph Limen Mathematics (AL Mathematics)** is a standalone mathematical
system created to formalize a forbidden operation of classical mathematics:
**division by zero**.

In standard mathematics, dividing by zero produces an undefined result and
terminates computation. While this reflects physical reality, it also marks a
hard boundary of algebra itself.

Anastroph Limen Mathematics does not attempt to bypass this boundary using
infinity. Instead, it **redefines what exists beyond it**.

---

## The Core Problem of Division by Zero

In classical arithmetic, division is reversible:

x / y = z  
z × y = x  

This reversibility is essential.

However, when dividing by zero:

4 / 0 = ∞  
∞ × 0 ≠ 4  

The operation loses information. Worse:

4 / 0 = 7 / 0 = 12 / 0 = ∞  

Infinity is a **fixed constant**. Once reached, the original value is destroyed.
This is why infinity cannot serve as a valid result of division by zero.

---

## The Fundamental Inversion

Classical numbers progress as:

0 → 1 → 2 → … → ∞  

Anastroph Limen Mathematics inverts this axis conceptually:

∞ → … → 2 → 1 → 0  

Infinity is no longer the end — it is the **origin**.

From this perspective, dividing by zero does not send a value to infinity.
Instead, it sends it **into the Anastroph Limen domain**.

---

## The Fundamental Rule

In Anastroph Limen Mathematics:

x / 0 = ALx  

Not infinity.  
Not undefined.  
But a structured mathematical object.

---

## What Is an AL Number?

An **AL number** represents a value that has crossed the zero-division boundary
while retaining its identity.

Each AL number stores:

- The original magnitude (threshold)
- The operational intensity (density)
- The directional sign (positive, negative, or neutral)

This allows reversibility and algebraic consistency.

---

## AL Number Representations

### 1. Meaning Representation

The simplest form.

x / 0 = ALx  

Examples:

5 / 0 = AL5  
-5 / 0 = -AL5  

This representation shows **what value crossed zero**, but not its internal
state.

---

### 2. Density Representation

Density represents how many AL operations have accumulated.

All classical-to-AL transitions start with density = 1.

x / 0 = ALx¹  

Examples:

AL5¹  
-AL4²  

Density is required because AL numbers are **stateful**, unlike classical
numbers.

---

### 3. Functional Representation (Canonical Form)

This is the complete and exact form:

AL(threshold, density, sign)

Formal definition:

x / 0 = AL(x, 1, + / − / 0)

Examples:

AL(3, 1, +)  
AL(4, 2, −)  

This representation is the mathematical truth of an AL number.

---

## Measure

Every AL number has a **measure**, which is its projection back into classical
space.

Definition:

- Positive AL → +threshold
- Negative AL → −threshold
- Neutral AL → 0

Measure is **not** the AL number itself — it is only its classical value.

---

## Arithmetic in Anastroph Limen Mathematics

Unlike classical arithmetic, AL arithmetic is **state-aware**. Operations depend
on threshold, density, and sign.

Below, each operation is explained using explicit equations.

---

## Addition

Addition combines densities and compares directional dominance.

### Same Sign

AL(1,1,+) + AL(1,1,+)

- Threshold = max(1,1) = 1
- Density = 1 + 1 = 2
- Sign = +

Result:

AL(1,2,+)

---

### Opposite Signs

AL(1,1,+) + AL(1,1,-)

- Densities cancel
- No dominant direction

Result:

AL(0,1,0)  (neutral)

---

### Unequal Density

AL(2,3,+) + AL(1,1,-)

- Remaining density = 2
- Dominant sign = +

Result:

AL(2,2,+)

---

## Subtraction

Subtraction is defined as addition with inverted direction:

A − B = A + (−B)

Example:

AL(2,1,+) − AL(1,1,+)

→ AL(2,1,+) + AL(1,1,-)

Result:

AL(0,1,0)

---

## Multiplication

### AL × AL

AL multiplication combines structure:

AL(a,d₁,s₁) × AL(b,d₂,s₂)

- Threshold = a + b
- Density = d₁ × d₂
- Sign follows sign multiplication rules

Example:

AL(1,1,+) × AL(2,1,+)

Result:

AL(3,1,+)

---

### The Critical Rule: AL × 0

This is a **core axiom** of Anastroph Limen Mathematics:

ALx × 0 = x  

Not AL(x).  
Not 0.  
The **original classical value**.

Example:

AL(5,1,+) × 0 = 5  
AL(3,2,-) × 0 = -3  

This rule restores reversibility and is fundamental to the system.

---

## Division

### Number ÷ 0

x / 0 = ALx  

Example:

7 / 0 = AL7

---

### AL ÷ 0

AL(x) / 0 = AL(x)

The AL number remains in AL space.

---

### AL ÷ Number

AL(4,2,+) / 2

- Density reduces
- Sign adjusts if needed

Result:

AL(4,1,+)

---

## Modulo

Modulo preserves AL structure:

AL(5,2,+) % 3

Result:

AL(2,2,+)

Division by zero in modulo also returns an AL number.

---

## Power

Exponentiation scales both threshold and density.

Example:

(AL(2,1,+))²

Result:

AL(4,1,+)

Mixed-sign exponentiation resolves to neutral if undefined.

---

## Neutral AL Numbers

Neutral AL numbers represent **perfect cancellation**.

They carry no directional force and act as equilibrium states in AL arithmetic.

---

## Why Anastroph Limen Works

Anastroph Limen Mathematics works because:

- It rejects infinity as a terminal constant
- It preserves reversibility
- It encodes information instead of destroying it
- It treats division by zero as a **state transition**

---

## What This Is

- A new number system
- A reversible algebra beyond zero
- A formal model for division-by-zero states

---

## What This Is Not

- Not infinity arithmetic
- Not symbolic math
- Not a numerical hack
- Not classical algebra

---

## Note on Arithmetic

Anastroph Limen (AL) arithmetic is **not equivalent to classical arithmetic**.  
Although the syntax may appear similar, the underlying semantics and results are fundamentally different.

### Examples

In AL arithmetic:

AL1 + AL1 = AL1²

but

AL1 * AL2 = AL3¹

These two results are **not equal** and must not be interpreted using classical arithmetic rules.

In classical arithmetic, addition and multiplication can sometimes produce the same result  
(e.g. `1 + 1 = 2` and `1 * 2 = 2`).  
This equivalence **does not apply** in the Anastroph Limen system.

### Mixing AL and Classical Numbers

If equivalence is required, multiplication must be performed between an **AL value and a classical number**,  
not between two AL values.

In the classical number system, multiplying by `2` means *taking two times the same quantity*.  
Applying this interpretation:

AL1 + AL1 = AL²
AL1 * 2   = AL²

Here, the results match because `2` follows **classical arithmetic semantics**, not AL semantics.

### Underlying Reason

AL values do **not** scale from `0` to `∞` like classical numbers.

Instead, they are defined on an **inverse scale**:

Classical numbers: 0 → ∞
AL numbers:        ∞ → 0

Because of this inverted structure, AL–AL operations represent  
**structural or directional interactions**, rather than linear magnitude scaling.

### Important Notes

- Anastroph Limen is **not part of classical mathematics**
- It is **non-standard** and **metamathematical**
- Its arithmetic behavior is **intentional and foundational** to the system

AL should always be treated as its **own algebraic domain**,  
not as a variant or extension of classical arithmetic.

## Final Statement

Classical mathematics ends at division by zero.

Anastroph Limen Mathematics **begins there**.

Where numbers lose meaning,
Anastroph Limen gives them structure.

---

### Final Note

Anastroph Limen is not part of classical mathematics and is not a standard arithmetic system.
It belongs to metamathematics, aiming to model and reason about situations that lie outside conventional mathematical axioms.

The entire system, including all definitions, rules, and operational logic, is implemented functionally inside the math.py file.
Anyone interested can directly inspect the source code to understand how the rules are applied.

Therefore, Anastroph Limen is not presented as a claim, but as an inspectable and formalized structure.
