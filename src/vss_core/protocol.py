from src.vss_core.crypto_engine import CryptoEngine
import secrets

class Dealer:
    def __init__(self, threshold, num_shares, engine=None):
        """
        Args:
            threshold (int): Minimum shares needed to reconstruct (t).
            num_shares (int): Total shares to distribute (n).
            engine (CryptoEngine): The elliptic curve math wrapper.
        """
        self.t = threshold
        self.n = num_shares
        self.engine = engine if engine else CryptoEngine()

    def generate_polynomial(self, secret):
        """
        Creates a random polynomial f(x) = secret + a1*x + ... + at-1*x^(t-1)
        Returns: List of coefficients [secret, a1, a2, ..., at-1]
        """
        coefficients = [secret]
        # We need t-1 random coefficients
        for _ in range(self.t - 1):
            random_coeff = self.engine.generate_secret()
            coefficients.append(random_coeff)
        return coefficients

    def generate_commitments(self, coefficients):
        """
        Converts coefficients into Public Verification Points.
        C_i = coefficient_i * G
        """
        commitments = []
        for coeff in coefficients:
            comm = self.engine.get_commitment(coeff)
            commitments.append(comm)
        return commitments

    def evaluate_polynomial(self, coefficients, x):
        """
        Evaluates f(x) using Horner's Method or simple summation.
        f(x) = sum( c_i * x^i ) mod order
        """
        result = 0
        for i, coeff in enumerate(coefficients):
            term = coeff * pow(x, i, self.engine.n)
            result = (result + term) % self.engine.n
        return result

    def distribute_secret(self, secret_value=None):
        """
        The Main Event:
        1. Pick a secret (if not provided).
        2. Create the polynomial.
        3. Calculate public commitments.
        4. Generate private shares for n participants.
        
        Returns:
            dict: { 'commitments': [...], 'shares': [(1, y1), (2, y2), ...] }
        """
        if secret_value is None:
            secret_value = self.engine.generate_secret()

        # 1 & 2: Polynomial
        coeffs = self.generate_polynomial(secret_value)

        # 3: Commitments (The "Receipts")
        commitments = self.generate_commitments(coeffs)

        # 4: Shares (The "Keys")
        shares = []
        for i in range(1, self.n + 1):
            share_val = self.evaluate_polynomial(coeffs, i)
            shares.append((i, share_val))

        return {
            "commitments": commitments,
            "shares": shares,
            "secret_kept_by_dealer": secret_value  # For debugging/verification
        }