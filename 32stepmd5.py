import math

rotate_by = [7, 12, 17, 22, 7, 12, 17, 22,
             5, 9, 14, 20, 5, 9, 14, 20]

constants = [int(abs(math.sin(i + 1)) * 4294967296) & 0xFFFFFFFF for i in range(32)]

def pad(msg):
    msg_len_in_bits = (8 * len(msg)) & 0xffffffffffffffff
    msg.append(0x80)

    while len(msg) % 64 != 56:
        msg.append(0)

    msg += msg_len_in_bits.to_bytes(8, byteorder='little')
    return msg

init_MDBuffer = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476]

def leftRotate(x, amount):
    x &= 0xFFFFFFFF
    return (x << amount | x >> (32 - amount)) & 0xFFFFFFFF

def processMessage(msg):
    init_temp = init_MDBuffer[:]
    
    for offset in range(0, len(msg), 64):
        A, B, C, D = init_temp
        block = msg[offset:offset + 64]

        for i in range(16):
            func = lambda b, c, d: (b & c) | (~b & d)
            index_func = lambda i: i

            F = func(B, C, D)
            G = index_func(i)

            to_rotate = A + F + constants[i] + int.from_bytes(block[4 * G:4 * G + 4], byteorder='little')
            newB = (B + leftRotate(to_rotate, rotate_by[i % 16])) & 0xFFFFFFFF

            A, B, C, D = D, newB, B, C

        for i in range(16, 32):
            func = lambda b, c, d: (d & b) | (~d & c)
            index_func = lambda i: (5 * i + 1) % 16

            F = func(B, C, D)
            G = index_func(i)

            to_rotate = A + F + constants[i] + int.from_bytes(block[4 * G:4 * G + 4], byteorder='little')
            newB = (B + leftRotate(to_rotate, rotate_by[i % 16])) & 0xFFFFFFFF

            A, B, C, D = D, newB, B, C

        for i, val in enumerate([A, B, C, D]):
            init_temp[i] += val
            init_temp[i] &= 0xFFFFFFFF

    return sum(buffer_content << (32 * i) for i, buffer_content in enumerate(init_temp))

def MD_to_hex(digest):
    raw = digest.to_bytes(16, byteorder='little')
    return '{:032x}'.format(int.from_bytes(raw, byteorder='big'))

def md5(msg):
    msg = bytearray(msg, 'ascii')
    msg = pad(msg)
    processed_msg = processMessage(msg)
    message_hash = MD_to_hex(processed_msg)
    print("Message Hash: ", message_hash)

if __name__ == '__main__':
    message = "hello"
    md5(message)