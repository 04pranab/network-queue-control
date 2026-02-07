# Plot Explanations
## Interpretation of Stability, Control, and Queue Behavior

This file explains the **three plots only**.
Each section answers one question:

What is plotted?  
What does it show?  
Why does it matter?

No equations are derived here.
The focus is **reading the plots correctly**.

---

## 1. Lyapunov Stability Comparison
### File: `lyapunov_comparison.png`

### What Is Plotted

The Lyapunov function:

V(q) = q(t)²

for two transmission strategies:
- optimal smooth control
- bursty transmission

---

### What the Plot Shows

The optimal curve remains close to zero for all time.

The bursty curve rises sharply, reaches a large peak,
and then slowly decays back to zero.

Both curves eventually return to zero.

---

### Interpretation

The Lyapunov function measures **stored instability** in the system.

A small value of V(q) means:
- little congestion
- low delay
- stable operation

A large value of V(q) means:
- heavy backlog
- accumulated delay
- temporary instability

The bursty policy injects too much traffic too quickly,
causing instability to build up before it can be removed.

The optimal policy avoids creating instability at all.

---

### Key Insight

Stability is not just about convergence.
It is about **how much instability is created along the way**.

---

## 2. Transmission Rate Comparison
### File: `control_comparison.png`

### What Is Plotted

The sending rate u(t) over time for:
- optimal control
- bursty control

---

### What the Plot Shows

The optimal sending rate is:
- smooth
- continuous
- slowly varying

The bursty sending rate is:
- very high initially
- abruptly cut to zero
- discontinuous

---

### Interpretation

Sudden changes in sending rate correspond to aggressive behavior.

Aggressive behavior causes:
- queue buildup
- oscillations
- inefficiency

The optimal curve spreads transmission over time,
reducing stress on the network.

Smoothness is not imposed manually.
It appears naturally when congestion is penalized.

---

### Key Insight

Burstiness is fast in the short term,
but expensive in the long term.

---

## 3. Queue Evolution Comparison
### File: `queue_comparison.png`

### What Is Plotted

Queue length q(t) over time for:
- optimal control
- bursty control

---

### What the Plot Shows

Under optimal control:
- the queue stays near zero
- backlog is minimal
- delay remains low

Under bursty control:
- the queue grows rapidly
- reaches a large peak
- drains slowly over time

---

### Interpretation

Queues represent **unserved work**.

Once a queue is created, it cannot disappear instantly.
It must be drained at the service rate.

The bursty policy creates backlog early
and pays for it later.

The optimal policy prevents backlog from forming.

---

### Key Insight

Queues have memory.
Avoiding queue creation is better than draining queues later.

---

## 4. Overall Interpretation

The three plots describe a single story:

1. Bursty transmission creates queues
2. Queues create instability
3. Instability increases system cost

Optimal control avoids all three by shaping traffic over time.

---

## Final Takeaway

Smooth congestion control is not conservative.

It is **optimal**.
