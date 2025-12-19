from src.visuals.story_plotter import StoryVisualizer

def main():
    print("--- Starting Visual Story Mode ---")
    print("Press Enter in this terminal to advance slides.")
    
    viz = StoryVisualizer()
    
    # Toy coefficients for visuals: Secret=10, Slope=2, Curve=-0.5
    coeffs = [10, 2, -0.5]

    input("\n[1/6] Enter for Stage 1: The Secret (Shamir)...")
    viz.plot_stage_1_the_secret(secret=10, coefficients=coeffs)

    input("\n[2/6] Enter for Stage 2: The One-Way Function...")
    viz.plot_stage_2_the_oneway_mirror()

    input("\n[3/6] Enter for Stage 3: The Equation...")
    viz.plot_stage_3_the_equation()

    input("\n[4/6] Enter for Stage 4: The Proof (Success)...")
    viz.plot_stage_4_the_proof()

    input("\n[5/6] Enter for Stage 5: The ATTACK (Tampering)...")
    viz.plot_stage_5_the_attack()

    input("\n[6/6] Enter for Stage 6: Threshold Reconstruction...")
    viz.plot_stage_6_threshold(secret=10, coefficients=coeffs)
    
    print("\n[End] Presentation Complete.")

if __name__ == "__main__":
    main()