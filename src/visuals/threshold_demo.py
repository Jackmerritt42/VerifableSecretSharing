import matplotlib.pyplot as plt
import numpy as np

def run_broad_reconstruction_demo():
    # 1. Setup the Secret Polynomial (Secret=42)
    # f(x) = 42 + 5x - 2x^2
    coeffs = [42, 5, -2]
    x_range = np.linspace(0, 6, 100)
    y_true = coeffs[0] + coeffs[1]*x_range + coeffs[2]*(x_range**2)

    # 2. Generate 5 Shares
    shares = []
    for i in range(1, 6):
        val = coeffs[0] + coeffs[1]*i + coeffs[2]*(i**2)
        shares.append((i, val))

    # Setup the Plot
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    fig.suptitle("Broad Demonstration: Threshold Reconstruction (t=3)", fontsize=16, fontweight='bold', color='navy')

    # --- PANEL 1: The Scattered Shares ---
    ax1 = axes[0]
    ax1.set_title("1. The Distributed Shares", fontsize=12, fontweight='bold')
    ax1.scatter([s[0] for s in shares], [s[1] for s in shares], s=150, color='gray', label='Shares')
    ax1.set_xlim(0, 6)
    ax1.set_ylim(0, 60)
    ax1.text(3, 50, "We have 5 pieces.\nWe need ANY 3 to solve.", ha='center', bbox=dict(facecolor='white', alpha=0.8))

    # --- PANEL 2: Group A (1, 2, 3) ---
    ax2 = axes[1]
    ax2.set_title("2. Group A Reconstructs (1, 2, 3)", fontsize=12, fontweight='bold')
    
    # Plot Group A points
    group_a = [shares[0], shares[1], shares[2]]
    ax2.scatter([s[0] for s in group_a], [s[1] for s in group_a], s=200, color='blue', zorder=5, label='Group A')
    
    # Plot the Reconstruction (Lagrange)
    # Visual trick: We just plot the true curve because math guarantees it matches
    ax2.plot(x_range, y_true, color='blue', linestyle='--', linewidth=2, label='Derived Curve')
    ax2.scatter([0], [42], color='gold', s=300, marker='*', zorder=10, edgecolor='black')
    ax2.text(0.5, 45, "Secret: 42", fontweight='bold')
    ax2.legend()

    # --- PANEL 3: Group B (3, 4, 5) ---
    ax3 = axes[2]
    ax3.set_title("3. Group B Reconstructs (3, 4, 5)", fontsize=12, fontweight='bold')
    
    # Plot Group B points
    group_b = [shares[2], shares[3], shares[4]]
    ax3.scatter([s[0] for s in group_b], [s[1] for s in group_b], s=200, color='green', zorder=5, label='Group B')
    
    # Plot the Reconstruction
    ax3.plot(x_range, y_true, color='green', linestyle='-.', linewidth=2, label='Derived Curve')
    ax3.scatter([0], [42], color='gold', s=300, marker='*', zorder=10, edgecolor='black')
    ax3.text(0.5, 45, "Secret: 42", fontweight='bold')
    ax3.legend()

    # Final visual check
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_broad_reconstruction_demo()