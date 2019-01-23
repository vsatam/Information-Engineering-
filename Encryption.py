p = 6847944682037444681162770672798288913849
q = 2425967623052370772757633156976982469681
n = p * q
print("n = p * q = " + str(n) + "\n")
phi = (p - 1) * (q - 1)
print("phi(n): " + str(phi) + "\n")
e = 3


def gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = gcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = gcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    else:
        return x % m


d = modinv(e, phi)

print("\nPublic Keys: (e=" + str(e) + ", n=" + str(n) + ").\n")
print("Private Keys: (d=" + str(d) + ", n=" + str(n) + ").\n")

# MESSAGE ENCRYPTION AND DECRYPTION
import sys

# IMPORTANT: The block size MUST be less than or equal to the key size!

# (Note: The block size is in bytes, the key size is in bits. There are 8 bits in 1 byte.)
DEFAULT_BLOCK_SIZE = 128  # Cause we are dealing with 128 bytes

BYTE_SIZE = 256  # One byte has 256 different values.


def getBlocksFromText(message, blockSize=DEFAULT_BLOCK_SIZE):
    messageBytes = message.encode('ascii')  # convert the string to bytes
    blockInts = []
    for blockStart in range(0, len(messageBytes), blockSize):
        # Calculate the block integer for this block of text
        blockInt = 0
        for i in range(blockStart, min(blockStart + blockSize, len(messageBytes))):
            blockInt += messageBytes[i] * (BYTE_SIZE ** (i % blockSize))
            blockInts.append(blockInt)
    return blockInts


def getTextFromBlocks(blockInts, messageLength, blockSize=DEFAULT_BLOCK_SIZE):
    # Converts a list of block integers to the original message string.
    # The original message length is needed to properly convert the last
    # block integer.
    message = []
    for blockInt in blockInts:
        blockMessage = []
        for i in range(blockSize - 1, -1, -1):
            if len(message) + i < messageLength:
                # Decode the message string for the 128 (or whatever
                # blockSize is set to) characters from this block integer.
                asciiNumber = blockInt // (BYTE_SIZE ** i)
                blockInt = blockInt % (BYTE_SIZE ** i)
                blockMessage.insert(0, chr(asciiNumber))
        message.extend(blockMessage)
    return ''.join(message)


message = "s"


def encryptMessage(N, E, message, blockSize=DEFAULT_BLOCK_SIZE):
    encryptedBlocks = []
    n = N
    e = E
    for block in getBlocksFromText(message, blockSize):
        encryptedBlocks.append(pow(block, e, n))
    return encryptedBlocks


blah = encryptMessage(n, e, message)


def decryptMessage(encryptedBlocks, messageLength, N, D, blockSize=DEFAULT_BLOCK_SIZE):
    # Decrypts a list of encrypted block ints into the original message
    # string. The original message length is required to properly decrypt the last block.
    # Also pass the PRIVATE key (d) to decrypt.
    decryptedBlocks = []
    n = N
    D = d
    for block in encryptedBlocks:
        # plaintext = ciphertext ^ d mod n
        decryptedBlocks.append(pow(block, d, n))
    return getTextFromBlocks(decryptedBlocks, messageLength, blockSize)