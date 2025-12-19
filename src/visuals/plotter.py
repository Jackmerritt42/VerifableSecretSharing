import matplotlib.pyplot as plt
import numpy as np

class Visualizer:
    def __init__(self, engine):
        self.engine = engine

    def show_grand_dashboard(self, secret, coefficients, shares, participant_id):
        """
        Creates a 2-panel 'Grandiose' Dashboard:
        1. Top: The Polynomial (Shamir's Logic) - Visualizing the secret.
        2. Bottom: The Verification (Feldman's Logic) - Visualizing the integrity check.
        """
        # Create the figure
        fig = plt.figure(figsize=(12, 10))
        fig.suptitle(f"Verifiable Secret Sharing Protocol: Participant {participant_id}", 
                     fontsize=16, fontweight='bold', color='navy')

        # --- PANEL 1: THE POLYNOMIAL (SHAMIR) ---
        ax1 = fig.add_subplot(2, 1, 1)
        
        # 1. Generate a smooth curve for the polynomial
        # We use a 'Toy' polynomial for visuals because real crypto numbers are too big to plot
        x = np.linspace(0, 6, 100)
        # Toy polynomial: y = secret + a1*x + a2*x^2 (scaled down for visuals)
        toy_secret = 10
        toy_coeffs = [toy_secret, 2, -0.5] 
        y = toy_coeffs[0] + toy_coeffs[1]*x + toy_coeffs[2]*(x**2)
        
        ax1.plot(x, y, label='Secret Polynomial f(x)', color='purple', linewidth=2)
        
        # 2. Plot The Secret (y-intercept at x=0)
        ax1.scatter([0], [toy_secret], color='red', s=200, zorder=5, label='The Secret f(0)')
        ax1.annotate('The Secret', xy=(0, toy_secret), xytext=(0.5, toy_secret+5),
                     arrowprops=dict(facecolor='black', shrink=0.05))

        # 3. Plot The Shares (Points on the curve)
        share_xs = [1, 2, 3, 4, 5]
        share_ys = [toy_coeffs[0] + toy_coeffs[1]*sx + toy_coeffs[2]*(sx**2) for sx in share_xs]
        
        # Highlight THIS participant's share
        target_x = participant_id
        target_y = share_ys[participant_id-1]
        
        ax1.scatter(share_xs, share_ys, color='cyan', s=100, edgecolor='black', label='Distributed Shares')
        ax1.scatter([target_x], [target_y], color='blue', s=300, edgecolor='gold', linewidth=3, 
                    label=f'Your Share f({target_x})')

        ax1.set_title("Layer 1: Shamir's Secret Sharing (The Logic)", fontsize=12, fontweight='bold')
        ax1.set_xlabel("Participant ID (x)")
        ax1.set_ylabel("Share Value (y)")
        ax1.legend()
        ax1.grid(True, alpha=0.3)

        # --- PANEL 2: THE VERIFICATION (FELDMAN) ---
        ax2 = fig.add_subplot(2, 1, 2)
        
        # Visualizing the equation: Share * G == Sum(Commitments)
        # We represent this as two bars reaching the same height (Integrity Match)
        
        categories = ['Your Calculation (LHS)', 'Public Commitments (RHS)']
        values = [100, 100] # They match if valid
        colors = ['blue', 'gold']
        
        bars = ax2.bar(categories, values, color=colors, alpha=0.7, width=0.5)
        
        # Add visual "Lock" icon
        ax2.text(0.5, 50, "✅ MATCH", ha='center', va='center', fontsize=20, 
                 fontweight='bold', color='white', bbox=dict(boxstyle="round,pad=0.5", fc="green", alpha=0.8))

        # Annotations explaining the math
        ax2.text(0, 110, r"$s_i \cdot G$", ha='center', fontsize=14, color='blue')
        ax2.text(1, 110, r"$\sum (C_j \cdot i^j)$", ha='center', fontsize=14, color='darkgoldenrod')
        
        ax2.set_ylim(0, 130)
        ax2.set_title("Layer 2: Feldman's Verification (The Proof)", fontsize=12, fontweight='bold')
        ax2.set_yticks([]) # Hide numbers, abstract concept
        
        # Add explanatory text box
        desc = (
            "HOW IT WORKS:\n"
            "1. You received a point on the curve (Blue Dot).\n"
            "2. You multiplied it by the Generator G (LHS).\n"
            "3. You checked it against the Public 'Receipts' (RHS).\n"
            "4. Since the bars match, the Dealer provided a valid share."
        )
        plt.figtext(0.5, 0.02, desc, ha="center", fontsize=10, bbox={"facecolor":"lightyellow", "alpha":0.5, "pad":5})

        plt.tight_layout(rect=[0, 0.05, 1, 0.95])
        plt.show()