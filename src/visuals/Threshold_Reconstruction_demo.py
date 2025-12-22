import matplotlib.pyplot as plt
import numpy as np
import random

class SecurityVisualizer:
    def __init__(self):
        self.fig = None
        self.ax = None

    def _setup_figure(self, title):
        if self.fig:
            plt.close(self.fig)
        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        self.fig.canvas.manager.set_window_title(title)
        self.ax.set_title(title, fontsize=16, fontweight='bold', color='navy', pad=20)
        
        # Standard Grid Setup
        self.ax.set_xlim(-1, 7)
        self.ax.set_ylim(0, 50)
        self.ax.grid(True, alpha=0.3, linestyle='--')
        self.ax.set_xlabel("Participant ID")
        self.ax.set_ylabel("Share Value")

    def fit_and_plot_quadratic(self, x_points, y_points, style, label=None, secret_marker=False):
        """Fits a quadratic (degree 2) to given points and plots it."""
        # Fit polynomial of degree 2
        coeffs = np.polyfit(x_points, y_points, 2)
        poly = np.poly1d(coeffs)
        
        # Generate smooth line
        x_line = np.linspace(-1, 7, 200)
        y_line = poly(x_line)
        
        self.ax.plot(x_line, y_line, **style, label=label)
        
        # Mark the secret (y-intercept)
        if secret_marker:
            secret_val = poly(0)
            self.ax.scatter([0], [secret_val], s=100, marker='*', zorder=5)

    def show_underdetermined_security(self):
        """
        SCENARIO 1: We have 2 points, but need 3.
        Visualizes infinite possibilities (Perfect Secrecy).
        """
        self._setup_figure("Scenario 1: Underdetermined (2 Shares known, 3 Needed)")
        
        # 1. The Fixed Shares (What the attacker has)
        known_x = [2, 4]
        known_y = [20, 30] # Arbitrary values
        
        self.ax.scatter(known_x, known_y, color='blue', s=200, zorder=10, label='Stolen Shares')
        
        # 2. Generate "Ghost Curves"
        # We pick random "fake secrets" and fit curves that pass through our fixed shares
        possible_secrets = [5, 15, 25, 35, 45]
        colors = ['red', 'orange', 'purple', 'green', 'gray']
        
        for i, secret in enumerate(possible_secrets):
            # To define a quadratic, we need 3 points. 
            # We use the 2 known points + 1 random secret guess.
            temp_x = known_x + [0]
            temp_y = known_y + [secret]
            
            self.fit_and_plot_quadratic(temp_x, temp_y, 
                                      style={'linestyle': '--', 'alpha': 0.6, 'color': colors[i]}, 
                                      secret_marker=True)

        # Annotations
        self.ax.text(3, 10, "INFINITE POSSIBILITIES:\nAll these curves fit the shares.\nThe Secret could be anything.", 
                     bbox=dict(facecolor='mistyrose', edgecolor='red', boxstyle='round'), fontsize=12)
        
        self.ax.legend(loc='upper right')
        plt.show()

    def show_fully_determined(self):
        """
        SCENARIO 2: We have 3 points.
        Visualizes the unique lock.
        """
        self._setup_figure("Scenario 2: Threshold Met (3 Shares known, 3 Needed)")
        
        # 1. The Fixed Shares
        # We add one more share that forces the curve to be specific
        known_x = [2, 4, 5]
        known_y = [20, 30, 38] 
        
        self.ax.scatter(known_x, known_y, color='green', s=200, zorder=10, label='Valid Shares')
        
        # 2. Fit the ONE true curve
        self.fit_and_plot_quadratic(known_x, known_y, 
                                  style={'color': 'green', 'linewidth': 3}, 
                                  label='Reconstructed Polynomial', 
                                  secret_marker=True)

        # Annotations
        poly = np.poly1d(np.polyfit(known_x, known_y, 2))
        secret = poly(0)
        self.ax.text(0.5, secret+5, f"Secret is locked at: {int(secret)}", fontweight='bold', color='green')
        
        self.ax.text(3, 10, "MATHEMATICAL CERTAINTY:\nWith 3 points, only ONE parabola exists.\nThe Secret is recovered.", 
                     bbox=dict(facecolor='honeydew', edgecolor='green', boxstyle='round'), fontsize=12)
        
        self.ax.legend(loc='upper right')
        plt.show()

if __name__ == "__main__":
    viz = SecurityVisualizer()
    
    print("Opening Scenario 1: Underdetermined System...")
    viz.show_underdetermined_security()
    
    input("Press Enter to show Scenario 2...")
    
    print("Opening Scenario 2: Fully Determined System...")
    viz.show_fully_determined()