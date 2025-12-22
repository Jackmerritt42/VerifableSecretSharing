WIP towards a rework on my SSS with DKG. I was thinking about it one night, and if the dealer just gives out malicious, incorrect shares, there would be no way of knowing without testing them. this implementation of  Feldman’s Verifiable Secret Sharing (VSS) will create a Byzantine Fault-Tolerant Secret Sharing Protocol. It mathematically guarantees that a share is valid before any secret reconstruction takes place, preventing a malicious dealer from corrupting the pool.

(AI GEN PROJECT DESCRIPTION (will change later))

This project implements **Feldman’s Verifiable Secret Sharing (VSS)** scheme using Elliptic Curve Cryptography (`secp256r1`). It improves upon standard Shamir’s Secret Sharing by adding a **verification layer** that allows participants to mathematically prove their share is valid immediately upon receipt, protecting against a dishonest dealer.

### 🚀 Key Features Implemented
* **Elliptic Curve Engine:** Custom wrapper around `tinyec` handling scalar multiplication and point addition.
* **Dealer Protocol:** Generates random polynomials over a finite field and issues public **Cryptographic Commitments**.
* **Non-Interactive Verification:** A mathematical engine that verifies shares using the equation: $s_i \cdot G = \sum C_j \cdot i^j$.

 Installation & Usage
**Prerequisites:** Python 3.10+

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

    Run the Verification Tests: This runs the simulation of a Dealer distributing shares to 5 participants, who then verify their own shares.
    Bash

    python -m pytest tests/test_protocol.py -v

📋 Project Roadmap

    [x] Core Cryptography: Implemented ECC math engine.

    [x] Dealer Logic: Polynomial generation and Commitment broadcast.

    [x] Verification Logic: Share integrity checking.

    [x] Malicious Simulation: Script to simulate a dishonest dealer sending fake shares.

    [x] Visualization: Matplotlib graphs showing the "Point-to-Curve" verification process.

    [x] Reconstruction: Logic to recover the secret from t verified shares.
