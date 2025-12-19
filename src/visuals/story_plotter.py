import matplotlib.pyplot as plt
import numpy as np

class StoryVisualizer:
    def __init__(self):
        self.fig = None
        self.ax = None

    def _setup_figure(self, title):
        if self.fig:
            plt.close(self.fig)
        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        self.fig.canvas.manager.set_window_title(title)
        self.ax.set_title(title, fontsize=18, fontweight='bold', color='navy', pad=20)
        self.ax.axis('off')

    def plot_stage_1_the_secret(self, secret, coefficients):
        """STAGE 1: The Polynomial (Shamir)"""
        self._setup_figure("Stage 1: The Hidden World (The Polynomial)")
        self.ax.axis('on')
        
        x = np.linspace(0, 5, 100)
        y = coefficients[0] + coefficients[1]*x + coefficients[2]*(x**2)
        self.ax.plot(x, y, color='purple', linewidth=3, label='f(x) = Secret + ...')
        
        self.ax.scatter([0], [coefficients[0]], color='red', s=300, zorder=5, edgecolor='black')
        self.ax.text(0.1, coefficients[0], "The Secret\n(y-intercept)", fontsize=12, fontweight='bold', color='darkred')

        user_x = 2
        user_y = coefficients[0] + coefficients[1]*user_x + coefficients[2]*(user_x**2)
        self.ax.scatter([user_x], [user_y], color='cyan', s=200, edgecolor='black', zorder=5, label='Your Share')
        self.ax.text(user_x+0.2, user_y, f"Your Private Share\n(2, {int(user_y)})", fontsize=11)

        self.ax.text(2.5, coefficients[0]-2, 
                     "THE PROBLEM:\nYou have a point (Blue).\nBut how do you know it's on the real line?", 
                     bbox=dict(facecolor='white', alpha=0.9, boxstyle='round'), fontsize=12)
        
        self.ax.legend(loc='upper right')
        self.ax.grid(True, alpha=0.3)
        plt.show()

    def plot_stage_2_the_oneway_mirror(self):
        """STAGE 2: The One-Way Mirror (Discrete Log)"""
        self._setup_figure("Stage 2: The One-Way Mirror (Elliptic Curve)")
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 10)

        self.ax.axvline(x=5, color='black', linewidth=5, linestyle='--')
        
        self.ax.text(2.5, 9, "PRIVATE WORLD\n(Integers)", ha='center', fontsize=16, fontweight='bold', color='darkred')
        self.ax.scatter([2.5], [6], s=600, color='red')
        self.ax.text(2.5, 5, "Secret 'a'", ha='center', fontsize=14, fontweight='bold')

        self.ax.arrow(3, 6, 3.5, 0, head_width=0.3, color='black', length_includes_head=True)
        self.ax.text(5, 6.5, "Multiply by G", ha='center', fontsize=10, bbox=dict(facecolor='white', edgecolor='none'))

        self.ax.text(7.5, 9, "PUBLIC WORLD\n(Curve Points)", ha='center', fontsize=16, fontweight='bold', color='green')
        self.ax.scatter([7.5], [6], s=600, marker='P', color='green')
        self.ax.text(7.5, 5, "Commitment 'C'", ha='center', fontsize=14, fontweight='bold')

        self.ax.text(5, 3.5, "[X] CANNOT GO BACK", ha='center', fontsize=16, fontweight='bold', 
                     bbox=dict(facecolor='mistyrose', edgecolor='red', boxstyle='round'))
        plt.show()

    def plot_stage_3_the_equation(self):
        """STAGE 3: The Equation"""
        self._setup_figure("Stage 3: The Verification Equation")
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 10)

        self.ax.text(5, 9, "How do we prove the Blue Dot matches the Green Cross?", ha='center', fontsize=16, fontstyle='italic')

        self.ax.text(2, 6, r"$s_i \cdot G$", fontsize=40, color='blue', ha='center')
        self.ax.text(2, 4.5, "Your Share \n projected to curve", ha='center', color='blue', fontsize=12)

        self.ax.text(5, 6, r"$=$", fontsize=40, color='black', ha='center')
        self.ax.text(5, 4.5, "Must\nMatch", ha='center', fontsize=12)

        self.ax.text(8, 6, r"$\sum C_j \cdot i^j$", fontsize=40, color='green', ha='center')
        self.ax.text(8, 4.5, "Combination of \n Public Commitments", ha='center', color='green', fontsize=12)
        plt.show()

    def plot_stage_4_the_proof(self):
        """STAGE 4: Valid Proof"""
        self._setup_figure("Stage 4: SUCCESS - Valid Share")
        
        categories = ['My Calc (LHS)', 'Public Ledger (RHS)']
        values = [10, 10]
        colors = ['blue', 'green']
        
        self.ax.axis('on')
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        
        self.ax.bar(categories, values, color=colors, alpha=0.7, width=0.5)
        self.ax.plot([-0.5, 1.5], [10, 10], color='black', linestyle='--', linewidth=2)
        
        self.ax.text(0.5, 10.5, "MATCH CONFIRMED", ha='center', fontsize=16, fontweight='bold', color='green', bbox=dict(facecolor='white', edgecolor='green'))
        self.ax.text(0.5, 5, "Share is Authentic", ha='center', color='white', fontsize=14, fontweight='bold')
        
        self.ax.set_ylim(0, 13)
        self.ax.set_yticks([]) 
        plt.show()

    def plot_stage_5_the_attack(self):
        """STAGE 5: The Attack Simulation (Tampered Share)"""
        self._setup_figure("Stage 5: ATTACK DETECTED - Tampered Share")
        
        categories = ['My Calc (LHS)', 'Public Ledger (RHS)']
        values = [12, 10] # MISMATCH!
        colors = ['red', 'green']
        
        self.ax.axis('on')
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        
        self.ax.bar(categories, values, color=colors, alpha=0.7, width=0.5)
        
        # Mismatch lines
        self.ax.plot([-0.5, 0.5], [12, 12], color='red', linestyle='--', linewidth=2)
        self.ax.plot([0.5, 1.5], [10, 10], color='green', linestyle='--', linewidth=2)
        
        self.ax.text(0.5, 11, "MISMATCH!", ha='center', fontsize=20, fontweight='bold', color='red', bbox=dict(facecolor='white', edgecolor='red'))
        
        # Narrative
        desc = (
            "FRAUD ALERT:\n"
            "The Dealer tried to give me a fake share (Red Bar).\n"
            "It does not match the Public Commitment (Green Bar).\n"
            "I reject this key immediately!"
        )
        self.ax.text(0.5, 6, desc, ha='center', fontsize=12, bbox=dict(facecolor='mistyrose', alpha=1))
        
        self.ax.set_ylim(0, 14)
        self.ax.set_yticks([]) 
        plt.show()

    def plot_stage_6_threshold(self, secret, coefficients):
        """STAGE 6: Threshold Cryptography (Reconstruction)"""
        self._setup_figure("Stage 6: Threshold Reconstruction (t=3)")
        self.ax.axis('on')
        
        # 1. Plot Ghost Curve
        x = np.linspace(0, 5, 100)
        y = coefficients[0] + coefficients[1]*x + coefficients[2]*(x**2)
        self.ax.plot(x, y, color='lightgray', linewidth=2, linestyle='--')
        
        # 2. Plot 3 specific shares (Threshold)
        share_ids = [1, 3, 4]
        for i in share_ids:
            sy = coefficients[0] + coefficients[1]*i + coefficients[2]*(i**2)
            self.ax.scatter([i], [sy], color='blue', s=200, zorder=5)
            self.ax.text(i, sy+0.5, f"Share {i}", ha='center')

        # 3. Connection Lines (Interpolation Visual)
        # Draw lines from shares converging to the secret
        for i in share_ids:
            sy = coefficients[0] + coefficients[1]*i + coefficients[2]*(i**2)
            self.ax.plot([i, 0], [sy, coefficients[0]], color='gold', alpha=0.6, linewidth=2)

        # 4. The Secret Revealed
        self.ax.scatter([0], [coefficients[0]], color='gold', marker='*', s=500, zorder=10, edgecolor='black')
        self.ax.text(0.2, coefficients[0], "SECRET\nUNLOCKED", fontsize=12, fontweight='bold', color='orange')

        self.ax.text(2.5, coefficients[0]-2, 
                     "THRESHOLD CRYPTOGRAPHY:\nWe combined 3 valid shares.\nLagrange Interpolation rebuilds the curve.\nThe Secret is recovered!", 
                     bbox=dict(facecolor='lightyellow', boxstyle='round'), fontsize=12)
        
        self.ax.grid(True, alpha=0.2)
        plt.show()