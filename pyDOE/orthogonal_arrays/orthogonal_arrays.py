"""
Provides a collection of commonly used Taguchi orthogonal arrays (OA)
for robust design experiments.

Each array defines a set of experiments using a reduced, statistically
balanced design, enabling efficient exploration of multiple factors and levels.

References
----------
- NIST orthogonal array data files:
    https://www.itl.nist.gov/div898/software/dataplot/designs.htm

- University of York, Department of Mathematics:
    https://www.york.ac.uk/depts/maths/tables/orthogonal.htm
- A Library of Orthogonal Arrays by N. J. A. Sloane:
    https://neilsloane.com/oadir/

"""

from pathlib import Path

import numpy as np


ORTHOGONAL_ARRAYS_DIR = Path(__file__).resolve().parent

#   $$ L_4(2^3) $$
# Taguchi L4 Orthogonal Design
# Number of factors                 = 3
# Number of levels for each factor  = 2
# Number of Experiments             = 4
#
# Reference: https://www.itl.nist.gov/div898/software/dataplot/dex/L4.DAT

L_4_2_3 = np.loadtxt(f"{ORTHOGONAL_ARRAYS_DIR}/L_4_2_3.oa", dtype=int) - 1

#   $$ L_8(2^7) $$
# Taguchi L8 Orthogonal Design
# Number of factors                 = 7
# Number of levels for each factor  = 2
# Number of Experiments             = 8
#
# Reference: https://www.itl.nist.gov/div898/software/dataplot/dex/L8.DAT

L_8_2_7 = np.loadtxt(f"{ORTHOGONAL_ARRAYS_DIR}/L_8_2_7.oa", dtype=int) - 1


#   $$ L_9(3^4) $$
# Taguchi L9 Orthogonal Design
# Number of factors                 = 4
# Number of levels for each factor  = 3
# Number of Experiments             = 9
#
# Reference: https://www.itl.nist.gov/div898/software/dataplot/dex/L9.DAT

L_9_3_4 = np.loadtxt(f"{ORTHOGONAL_ARRAYS_DIR}/L_9_3_4.oa", dtype=int) - 1


#   $$ L_{12}(2^{11}) $$
# Taguchi L12 Orthogonal Design
# Number of factors                 = 11
# Number of levels for each factor  = 2
# Number of Experiments             = 12
#
# Reference: https://www.itl.nist.gov/div898/software/dataplot/dex/L12.DAT

L_12_2_11 = np.loadtxt(f"{ORTHOGONAL_ARRAYS_DIR}/L_12_2_11.oa", dtype=int) - 1

#   $$ L_{16}(2^{15}) $$
# Taguchi L16 Orthogonal Design
# Number of factors                 = 15
# Number of levels for each factor  = 2
# Number of Experiments             = 16
#
# Reference: https://www.itl.nist.gov/div898/software/dataplot/dex/L16.DAT

L_16_2_15 = np.loadtxt(f"{ORTHOGONAL_ARRAYS_DIR}/L_16_2_15.oa", dtype=int) - 1

#   $$ L_{16}(4^{5}) $$
# Taguchi L16 (Type B) Orthogonal Design
# Number of factors                 = 5
# Number of levels for each factor  = 4
# Number of Experiments             = 16
#
# Reference: https://www.itl.nist.gov/div898/software/dataplot/dex/L16B.DAT

L_16_4_5 = np.loadtxt(f"{ORTHOGONAL_ARRAYS_DIR}/L_16_4_5.oa", dtype=int) - 1

#   $$ L_{18}(6^1 3^6) $$
# Taguchi L18 Orthogonal Design
# Number of factors                 = 7
# Number of levels for each factor  = 6 for factor 1, 3 for factors 2 to 7
# Number of Experiments             = 18
#
# Reference: https://www.itl.nist.gov/div898/software/dataplot/dex/L18.DAT

L_18_6_1_3_6 = (
    np.loadtxt(f"{ORTHOGONAL_ARRAYS_DIR}/L_18_6_1_3_6.oa", dtype=int) - 1
)

#   $$ L_{25}(5^6) $$
# Taguchi L25 Orthogonal Design
# Number of factors                 = 6
# Number of levels for each factor  = 5
# Number of Experiments             = 25
#
# Reference: https://www.itl.nist.gov/div898/software/dataplot/dex/L25.DAT

L_25_5_6 = np.loadtxt(f"{ORTHOGONAL_ARRAYS_DIR}/L_25_5_6.oa", dtype=int) - 1

# $$ L_{27}(2^1 3^{12}) $$
# Taguchi L27 Orthogonal Design
# Number of factors                 = 13
# Number of levels for each factor  = 2 for factor 1, 3 for factors 2 to 13
# Number of Experiments             = 27
#
# Reference: https://www.itl.nist.gov/div898/software/dataplot/dex/L27.DAT

L_27_2_1_3_12 = (
    np.loadtxt(f"{ORTHOGONAL_ARRAYS_DIR}/L_27_2_1_3_12.oa", dtype=int) - 1
)

#   $$ L_{32}(2^{31}) $$
# Taguchi L32 Orthogonal Design
# Number of factors                 = 31
# Number of levels for each factor  = 2
# Number of Experiments             = 32
#
# Reference: https://www.itl.nist.gov/div898/software/dataplot/dex/L32.DAT

L_32_2_31 = np.loadtxt(f"{ORTHOGONAL_ARRAYS_DIR}/L_32_2_31.oa", dtype=int) - 1

#   $$ L_{32}(2^1 4^9) $$
# Taguchi L32 (Type B) Orthogonal Design
# Number of factors                 = 10
# Number of levels for each factor  = 2 for 1 factor,
#                                     4 for 9 factors
# Number of Experiments             = 32
#
# Reference: https://www.itl.nist.gov/div898/software/dataplot/dex/L32B.DAT

L_32_2_1_4_9 = (
    np.loadtxt(f"{ORTHOGONAL_ARRAYS_DIR}/L_32_2_1_4_9.oa", dtype=int) - 1
)


#   $$ L_{36}(3^{23}) $$
# Taguchi L36 Orthogonal Design
# Number of factors                 = 23
# Number of levels for each factor  = 3
# Number of Experiments             = 36
#
# Reference: https://www.itl.nist.gov/div898/software/dataplot/dex/L36.DAT

L_36_3_23 = np.loadtxt(f"{ORTHOGONAL_ARRAYS_DIR}/L_36_3_23.oa", dtype=int) - 1

#   $$ L_{50}(2^1 5^{11}) $$
# Taguchi L50 Orthogonal Design
# Number of factors                 = 12
# Number of levels for each factor  = 2 (for 1 factor), 5 (for 11 factors)
# Number of Experiments             = 50
#
# Reference: https://www.itl.nist.gov/div898/software/dataplot/dex/L50.DAT

L_50_2_1_5_11 = (
    np.loadtxt(f"{ORTHOGONAL_ARRAYS_DIR}/L_50_2_1_5_11.oa", dtype=int) - 1
)

#   $$ L_{54}(2^1 3^{25}) $$
# Taguchi L54 Orthogonal Design
# Number of factors                 = 26
# Number of levels for each factor  = 2 (for 1 factor), 3 (for 25 factors)
# Number of Experiments             = 54
#
# Reference: https://www.itl.nist.gov/div898/software/dataplot/dex/L54.DAT

L_54_2_1_3_25 = (
    np.loadtxt(f"{ORTHOGONAL_ARRAYS_DIR}/L_54_2_1_3_25.oa", dtype=int) - 1
)

#   $$ L_{64}(2^{31}) $$
# Taguchi L64 Orthogonal Design
# Number of factors                 = 31
# Number of levels for each factor  = 2
# Number of Experiments             = 64
#
# Reference: https://www.itl.nist.gov/div898/software/dataplot/dex/L64.DAT

L_64_2_31 = np.loadtxt(f"{ORTHOGONAL_ARRAYS_DIR}/L_64_2_31.oa", dtype=int) - 1

#   $$ L_{64}(4^{21}) $$
# Taguchi L64 (Type B) Orthogonal Design
# Number of factors                 = 21
# Number of levels for each factor  = 4
# Number of Experiments             = 64
#
# Reference: https://www.itl.nist.gov/div898/software/dataplot/dex/L64B.DAT

L_64_4_21 = np.loadtxt(f"{ORTHOGONAL_ARRAYS_DIR}/L_64_4_21.oa", dtype=int) - 1

#   $$ L_{81}(3^{40}) $$
# Taguchi L81 Orthogonal Design
# Number of factors                 = 40
# Number of levels for each factor  = 3
# Number of Experiments             = 81
#
# Reference: https://www.itl.nist.gov/div898/software/dataplot/dex/L81.DAT

L_81_3_40 = np.loadtxt(f"{ORTHOGONAL_ARRAYS_DIR}/L_81_3_40.oa", dtype=int) - 1


L_4_2_3.flags.writeable = False
L_8_2_7.flags.writeable = False
L_9_3_4.flags.writeable = False
L_12_2_11.flags.writeable = False
L_16_2_15.flags.writeable = False
L_16_4_5.flags.writeable = False
L_18_6_1_3_6.flags.writeable = False
L_25_5_6.flags.writeable = False
L_27_2_1_3_12.flags.writeable = False
L_32_2_31.flags.writeable = False
L_32_2_1_4_9.flags.writeable = False
L_36_3_23.flags.writeable = False
L_50_2_1_5_11.flags.writeable = False
L_54_2_1_3_25.flags.writeable = False
L_64_2_31.flags.writeable = False
L_64_4_21.flags.writeable = False
L_81_3_40.flags.writeable = False


ORTHOGONAL_ARRAYS = {
    "L4(2^3)": L_4_2_3,
    "L8(2^7)": L_8_2_7,
    "L9(3^4)": L_9_3_4,
    "L12(2^11)": L_12_2_11,
    "L16(2^15)": L_16_2_15,
    "L16(4^5)": L_16_4_5,
    "L18(6^1 3^6)": L_18_6_1_3_6,
    "L25(5^6)": L_25_5_6,
    "L27(2^1 3^12)": L_27_2_1_3_12,
    "L32(2^31)": L_32_2_31,
    "L32(2^1 4^9)": L_32_2_1_4_9,
    "L36(3^23)": L_36_3_23,
    "L50(2^1 5^11)": L_50_2_1_5_11,
    "L54(2^1 3^25)": L_54_2_1_3_25,
    "L64(2^31)": L_64_2_31,
    "L64(4^21)": L_64_4_21,
    "L81(3^40)": L_81_3_40,
}
