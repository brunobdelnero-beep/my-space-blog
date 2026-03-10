import matplotlib
matplotlib.use('Agg')  # Non-interactive backend - no display needed
import matplotlib.pyplot as plt

# 1. Precise Data Extraction
# Time points (x-axis)
time = [0, 20, 40, 60, 80, 100, 120, 140]

# "Wt" Series Data (Approximated from visual inspection)
# Characteristics: Sharp peak at 60, drops below Krall at 100-120
wt_y = [2, 1, 3, 86, 40, 14, 4, 1]

# "Krall" Series Data (Approximated from visual inspection)
# Characteristics: Rises earlier at 40, lower peak at 60, higher tail at 100-120
krall_y = [5, 2, 12, 66, 38, 22, 12, 4]

# 2. Setup Plot
plt.figure(figsize=(6, 4.5)) # Aspect ratio similar to screenshot

# 3. Plotting the Lines
# Wt: Solid line, filled diamond markers (looks like rotated square), dark grey/black
plt.plot(time, wt_y, color='k', linestyle='-', linewidth=1,
         marker='d', markersize=5, markerfacecolor='k', label='Wt')

# Krall: Solid line, open square markers
plt.plot(time, krall_y, color='k', linestyle='-', linewidth=1,
         marker='s', markersize=5, markerfacecolor='w', markeredgecolor='k', label='Krall')

# 4. Styling the Axes
# Set limits to match the image exactly
plt.xlim(0, 145)
plt.ylim(0, 100)

# Set ticks to match the image (0, 20...140 and 0, 50, 100)
plt.xticks(range(0, 141, 20), fontsize=9)
plt.yticks([0, 50, 100], fontsize=9)

# Labels (Font weight bold to match typical academic graphs)
plt.xlabel("TIME AFTER G1 ARREST (MIN)", fontsize=9, fontweight='bold')
plt.ylabel("% OF LARGE BUDDED CELLS", fontsize=9, fontweight='bold')

# 5. Clean up the box (Remove top and right borders)
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 6. Legend (Top right, no frame)
plt.legend(loc='upper right', frameon=False, ncol=2, fontsize=9)

# Save the plot
plt.tight_layout()
plt.savefig('graph.pdf', bbox_inches='tight')
plt.savefig('graph.png', bbox_inches='tight')
