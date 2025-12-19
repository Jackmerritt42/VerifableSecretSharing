import pytest
from src.vss_core.protocol import Dealer
from src.vss_core.crypto_engine import CryptoEngine

class MaliciousDealer(Dealer):
    def distribute_corrupted_secret(self, secret, victim_id):
        """
        Runs the normal distribution, but intentionally modifies
        the share for 'victim_id' so it no longer matches the polynomial.
        """
        # 1. Run honest distribution first
        data = self.distribute_secret(secret)
        
        # 2. Corrupt the specific victim's share
        corrupted_shares = []
        for participant_id, share_val in data['shares']:
            if participant_id == victim_id:
                print(f"    [!] SABOTAGE: Corrupting share for Participant {participant_id}...")
                # Add 1 to the share value (breaking the point on the curve)
                fake_val = (share_val + 1) % self.engine.n
                corrupted_shares.append((participant_id, fake_val))
            else:
                corrupted_shares.append((participant_id, share_val))
        
        # 3. Return the bundle with the fake share
        data['shares'] = corrupted_shares
        return data

def test_catch_cheater():
    print("\n[+] STARTING SECURITY AUDIT: Malicious Dealer Simulation")
    
    # Setup
    t, n = 3, 5
    dealer = MaliciousDealer(t, n)
    engine = CryptoEngine()
    
    secret = 99999
    victim_id = 2  # We will target Participant 2
    
    # Malicious Distribution
    result = dealer.distribute_corrupted_secret(secret, victim_id)
    commitments = result['commitments']
    
    # Verification Phase (The Firewall)
    print("[+] Verifying all shares against public commitments...")
    
    caught_cheater = False
    
    for pid, share_val in result['shares']:
        is_valid = engine.verify_share(pid, share_val, commitments)
        
        if is_valid:
            print(f"    Participant {pid}: Verified OK")
        else:
            print(f"    Participant {pid}: 🚨 VERIFICATION FAILED! (Fraud Detected)")
            if pid == victim_id:
                caught_cheater = True

    # Assert that we successfully caught the attack
    assert caught_cheater == True
    print("\n[SUCCESS] System successfully identified the fake share.")

if __name__ == "__main__":
    test_catch_cheater()