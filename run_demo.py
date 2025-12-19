from src.vss_core.protocol import Dealer
from src.visuals.plotter import Visualizer

def main():
    print("--- Feldman's VSS: Grand Portfolio Demo ---")
    
    # 1. Initialize
    t, n = 3, 5
    dealer = Dealer(t, n)
    visualizer = Visualizer(dealer.engine)

    # 2. Distribute
    secret = 42 # The answer to everything
    print(f"[+] Distributing Secret: {secret}")
    data = dealer.distribute_secret(secret)
    
    # 3. Visualize
    # We pick Participant 2 to show the verification for
    target_id = 2
    print(f"[+] Launching Grandiose Dashboard for Participant {target_id}...")
    
    # We pass the coefficients implicitly via the visualizer's toy logic
    # In a real app, we'd pass the real coefficients, but for visuals we mock the curve shape
    visualizer.show_grand_dashboard(
        secret=secret,
        coefficients=[], # Handled internally for "Toy" visualization
        shares=data['shares'],
        participant_id=target_id
    )

if __name__ == "__main__":
    main()