import pytest
from src.vss_core.protocol import Dealer
from src.vss_core.crypto_engine import CryptoEngine

def test_dealer_distribution_and_verification():
    # 1. Setup: A 3-out-of-5 Scheme
    t = 3
    n = 5
    dealer = Dealer(t, n)
    
    print(f"\n[+] Dealer initialized (t={t}, n={n})")

    # 2. Distribute a secret
    secret = 123456789
    result = dealer.distribute_secret(secret)
    
    shares = result['shares']
    commitments = result['commitments']
    
    print(f"[+] Secret distributed. Generated {len(shares)} shares and {len(commitments)} commitments.")

    # 3. Verify EVERY share using the CryptoEngine
    # This mimics 5 different participants checking their own receipt
    engine = CryptoEngine()
    
    all_valid = True
    for idx, share_val in shares:
        # idx is the x-coordinate (1, 2, 3...)
        # share_val is the y-coordinate (the private piece)
        is_valid = engine.verify_share(idx, share_val, commitments)
        
        status = "VALID" if is_valid else "INVALID"
        print(f"    Participant {idx}: Share verification -> {status}")
        
        if not is_valid:
            all_valid = False

    assert all_valid == True
    print("[+] SUCCESS: All participants verified their shares against the public commitments.")

if __name__ == "__main__":
    test_dealer_distribution_and_verification()