import pytest
from src.vss_core.crypto_engine import CryptoEngine

def test_engine_initialization():
    """Test that the engine loads the curve correctly."""
    engine = CryptoEngine()
    assert engine.G is not None
    assert engine.n > 0
    print(f"\n[+] Engine initialized with Order: {engine.n}")

def test_manual_verification_logic():
    """
    Simulates a 2-out-of-n scheme manually to prove the math works.
    Polynomial: f(x) = secret + slope * x
    """
    engine = CryptoEngine()
    
    # 1. Setup our "Fake" Dealer variables
    secret_val = 12345
    slope_val = 54321
    
    # 2. Generate Commitments (The "Public Board")
    # C_0 = secret * G
    # C_1 = slope * G
    c_0 = engine.get_commitment(secret_val)
    c_1 = engine.get_commitment(slope_val)
    commitments = [c_0, c_1]
    
    # 3. Create a valid share for Participant ID = 1
    # f(1) = 12345 + 54321 * 1 = 66666
    participant_id = 1
    valid_share_val = secret_val + slope_val 
    
    # 4. Verify the valid share
    print("\n[+] Testing Valid Share...")
    is_valid = engine.verify_share(participant_id, valid_share_val, commitments)
    assert is_valid == True
    print("    -> Valid Share Verified Successfully!")

    # 5. Test an INVALID share (Malicious Dealer Simulation)
    print("[+] Testing Tampered Share...")
    fake_share_val = valid_share_val + 1  # Add 1 to break it
    is_valid_fake = engine.verify_share(participant_id, fake_share_val, commitments)
    assert is_valid_fake == False
    print("    -> Tampered Share Rejected Successfully!")

if __name__ == "__main__":
    # Allow running directly with 'python tests/test_vss.py'
    test_engine_initialization()
    test_manual_verification_logic()