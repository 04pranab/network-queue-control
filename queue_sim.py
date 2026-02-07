import numpy as np
import matplotlib.pyplot as plt


T = 10.0            # time horizon
dt = 0.01           # time step
N = int(T / dt)     # number of steps

c = 1.0             # service rate (c)
beta = 0.5          # control penalty (β)
w = 8.0             # total work (∫ u(t) dt)



t = np.linspace(0, T, N)



q_opt = np.zeros(N)     # optimal queue trajectory q(t)
u_opt = np.zeros(N)     # optimal control u(t)

q_burst = np.zeros(N)   # bursty comparison queue
u_burst = np.zeros(N)   # bursty sending rate



q_opt[0] = 0.0
q_burst[0] = 0.0


# Theory gives:
#   u*(t) = -λ(t) / (2β)
#   λ'(t) = -2q(t)

#   u(t) = c - (1/β) q(t)


k = 1.0 / beta

total_sent = 0.0

for i in range(N - 1):
    u_opt[i] = max(c - k * q_opt[i], 0.0)
    q_opt[i + 1] = max(q_opt[i] + (u_opt[i] - c) * dt, 0.0)
    total_sent += u_opt[i] * dt


scale = w / total_sent
u_opt *= scale

q_opt[:] = 0.0
for i in range(N - 1):
    q_opt[i + 1] = max(q_opt[i] + (u_opt[i] - c) * dt, 0.0)



burst_rate = 4.0 * c
burst_time = w / burst_rate

for i in range(N - 1):
    if t[i] <= burst_time:
        u_burst[i] = burst_rate
    else:
        u_burst[i] = 0.0

    q_burst[i + 1] = max(q_burst[i] + (u_burst[i] - c) * dt, 0.0)



V_opt = q_opt ** 2
V_burst = q_burst ** 2



J_opt = np.sum((q_opt**2 + beta * u_opt**2) * dt)
J_burst = np.sum((q_burst**2 + beta * u_burst**2) * dt)



print("Optimal cost J_opt   =", J_opt)
print("Bursty cost  J_burst =", J_burst)

# --- Queue evolution ---
plt.figure()
plt.plot(t, q_opt, label="Optimal queue q(t)")
plt.plot(t, q_burst, label="Bursty queue q(t)")
plt.xlabel("time t")
plt.ylabel("queue length q(t)")
plt.title("Queue Evolution Comparison")
plt.legend()
plt.grid(True)
plt.show()


# --- Sending rate ---
plt.figure()
plt.plot(t, u_opt, label="Optimal u(t)")
plt.plot(t, u_burst, label="Bursty u(t)")
plt.xlabel("time t")
plt.ylabel("sending rate u(t)")
plt.title("Transmission Rate Comparison")
plt.legend()
plt.grid(True)
plt.show()

# --- Lyapunov function ---
plt.figure()
plt.plot(t, V_opt, label="V(q) = q(t)^2 (optimal)")
plt.plot(t, V_burst, label="V(q) = q(t)^2 (bursty)")
plt.xlabel("time t")
plt.ylabel("Lyapunov function V(q)")
plt.title("Lyapunov Stability Comparison")
plt.legend()
plt.grid(True)
plt.show()