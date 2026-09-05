🐐🎲 Generalized Monty Hall

A simulation of the **Monty Hall problem**, extended to multiple doors and multiple phases of door openings.

### Features

- 🚪 Arbitrary number of doors
- 🔄 Multiple phases of door openings
- 🎯 Switch/stay decisions after each phase
- 📊 Monte Carlo estimation of winning probabilities

### Example

A 10-door game can be configured as:

```text
10 doors
   ↓
Monty opens 3
   ↓
Monty opens 3
   ↓
Monty opens 2
   ↓
2 doors remain
```

The player's strategy can be represented as:

```python
[True, False, True]
```

where `True` means **switch** after that phase.

The simulation can then be used to compare different strategies and visualize how their empirical winning probabilities converge as the number of trials increases.

## The Question

The classical Monty Hall problem asks:

> **Should you switch?**

This generalized version asks:

> **When should you switch?**

---

**Simulation • Probability • Monte Carlo • Python**
