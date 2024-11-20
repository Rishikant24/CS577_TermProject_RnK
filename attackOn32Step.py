import math
import random

rotate_by = [7, 12, 17, 22, 7, 12, 17, 22,
             5, 9, 14, 20, 5, 9, 14, 20]

constants = [int(abs(math.sin(i + 1)) * 4294967296) & 0xFFFFFFFF for i in range(32)]

def leftRotate(x, amount):
    x &= 0xFFFFFFFF
    return (x << amount | x >> (32 - amount)) & 0xFFFFFFFF

def fi(b, c, d, i):
    if i < 16:
        return (b & c) | (~b & d)
    else:
        return (d & b) | (~d & c)

def process_block(block, A0, B0, C0, D0):
    A, B, C, D = A0, B0, C0, D0
    for i in range(32):  # Only 32 steps for this attack
        F = fi(B, C, D, i)
        message_index = i % 16
        to_rotate = A + F + constants[i % 32] + block[message_index]
        newB = (B + leftRotate(to_rotate, rotate_by[i % 16])) & 0xFFFFFFFF
        A, B, C, D = D, newB, B, C
    return A, B, C, D

def md5_32_step_preimage_attack(target_hash):
    B0 = 0
    A0, C0, D0 = (random.randint(0, 0xFFFFFFFF) for _ in range(3))
    
    while True:
        M = [random.randint(0, 0xFFFFFFFF) for _ in range(16)]
        
        # Pick M0 such that B1 = 0xFFFFFFFF
        B1_target = 0xFFFFFFFF
        M[0] = (B1_target - D0) & 0xFFFFFFFF
        
        # Compute A30 to D30
        A, B, C, D = process_block(M, A0, B0, C0, D0)
        
        # Modify M2 to set B30 = D32
        M[1] = (target_hash - D) & 0xFFFFFFFF
        
        if B == (target_hash - D0):
            Hstar = (A + C + B0 + C0 + D) & 0xFFFFFFFF  # Final hash comparison
            if Hstar == target_hash:
                return A0, B0, C0, D0, M

if __name__ == '__main__':
    target = 0xDEADBEEF  # Example target hash for preimage attack
    A0, B0, C0, D0, M = md5_32_step_preimage_attack(target)
    print("Preimage found:")
    print(f"A0: {A0}, B0: {B0}, C0: {C0}, D0: {D0}")
    print(f"Message: {M}")