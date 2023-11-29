from modules import eqs, myplot as plot, data
import numpy as np

if __name__ == "__main__":
    int_en_stp = eqs.en_integral(1, 220)
    print(int_en_stp)