import matplotlib.pyplot as plt

# Data from the table
cycle_length = [10, 20, 30]
waiting_time_fc = [3.80, 3.39, 3.59]
waiting_time_lqf = [3.46, 3.23, 3.49]
collision_rate_fc = [0.05, 0.11, 0.04]
collision_rate_lqf = [0.05, 0.08, 0.02]

# Plot Waiting Time
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(cycle_length, waiting_time_fc, marker='o', label='FC - Waiting Time')
plt.plot(cycle_length, waiting_time_lqf, marker='s', label='LQF - Waiting Time')
plt.title('Waiting Time vs Cycle Length')
plt.xlabel('Cycle Length')
plt.ylabel('Waiting Time')
plt.legend()
plt.grid(True)

# Plot Collision Rate
plt.subplot(1, 2, 2)
plt.plot(cycle_length, collision_rate_fc, marker='o', label='FC - Collision Rate')
plt.plot(cycle_length, collision_rate_lqf, marker='s', label='LQF - Collision Rate')
plt.title('Collision Rate vs Cycle Length')
plt.xlabel('Cycle Length')
plt.ylabel('Collision Rate')
plt.legend()
plt.grid(True)

# Show plots
plt.tight_layout()
plt.show()
