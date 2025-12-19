from tinyec import registry
import secrets

class CryptoEngine:
    def __init__(self, curve_name='secp256r1'):
        """
        Initializes the Elliptic Curve Engine.
        We use 'secp256r1' (NIST P-256) by default as it has good support.
        """
        self.curve = registry.get_curve(curve_name)
        self.G = self.curve.g
        self.n = self.curve.field.n  # The order of the subgroup

    def generate_secret(self):
        """Generates a random secret (scalar) within the field order."""
        return secrets.randbelow(self.n)

    def get_commitment(self, scalar):
        """
        Computes the Public Commitment: C = scalar * G
        This is the 'One-Way Function' that secures the Verifiable Secret Sharing.
        """
        return scalar * self.G

    def compute_verification_point(self, share_index, commitments):
        """
        Computes the RHS of Feldman's Equation:
        Prod( C_j ^ (i^j) )  -> which in additive ECC is: Sum( (i^j) * C_j )
        
        Args:
            share_index (int): The 'x' value of the participant (i).
            commitments (list): List of Points [C_0, C_1, ... C_t-1].
        """
        # Start with the Point at Infinity (Identity element)
        # Note: tinyec doesn't expose a clean 'Infinity' object easily, 
        # so we initialize with the first term and add the rest.
        
        # Term 0: (i^0) * C_0 = 1 * C_0 = C_0
        result_point = commitments[0]

        for j in range(1, len(commitments)):
            # Calculate weight: i^j mod n
            weight = pow(share_index, j, self.n)
            
            # Calculate term: weight * C_j
            term = weight * commitments[j]
            
            # Add to total: result + term
            result_point = result_point + term
            
        return result_point

    def verify_share(self, share_index, share_value, commitments):
        """
        The Core Verification Logic.
        LHS: share_value * G
        RHS: Sum( (i^j) * C_j )
        """
        # 1. Compute LHS (Left Hand Side)
        lhs = share_value * self.G

        # 2. Compute RHS (Right Hand Side)
        rhs = self.compute_verification_point(share_index, commitments)

        # 3. Compare coordinates
        return lhs == rhs