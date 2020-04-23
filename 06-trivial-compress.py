from sys import getsizeof

class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1
        for nucleotide in gene.upper():
            self.bit_string <<= 2
            if nucleotide == "A":
                self.bit_string |= 0b00
            elif nucleotide == "C":
                self.bit_string |= 0b01
            elif nucleotide == "G":
                self.bit_string |= 0b10
            elif nucleotide == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotide: {}".format(nucleotide))
    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() -1, 2):
            bits: int = self.bit_string >> i & 0b11
            if bits == 0b00:  # A
                gene += "A"
            elif bits == 0b01:  # B
                gene += "B"
            elif bits == 0b10:  # G
                gene += "G"
            elif bits == 0b11:  # T
                gene += "T"
            else:
                raise ValueError("invalid bits: {}".format(bits))
        return gene

    def __str__(self):
        return self.decompress()


if __name__ == "__main__":
    orig_str = """TAGAGAGAGATTGATGTAGTACATGCATGTGTTGTCATGATCGTACGATCGTACTGTACGTACGTAGCTACGATCGATCTACATCGTAGTGCGTGATCGTACGACGATCTACGTAGCTATCGTAGCAGCTATCGATCTACGTAGCTAGCATCGTAGCTGATCGATCGATCGATGCTAGCTAGCTAGCTAGCTACGTACTAGCTAGCTAGCTAGCTGTTGTGTGTGACGACTTTATTCGCGGATTTACGGCGCGCGTATTCGTAGCTACGTACGTACTAGCTGA"""  * 100
    print("orig size is {} bytes".format(getsizeof(orig_str)))
    compressed: CompressedGene = CompressedGene(orig_str)
    print("compress size is {} bytes".format(getsizeof(compressed.bit_string)))
