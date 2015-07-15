"""

Geometric vs Arithmetic


Apple
Growth
Year 1: 10,000,000
Year 2: 12,000,000
Year 3: 14,000,000

10,000,000 + 12,000,000 + 14,0000 / 3 = 12,000,000 per year




Google
Year 1: 2.5%
Year 2: 3%
Year 3: 3.5%

Actual:
100000000 * 1.025 * 1.03 * 1.035

$ 109,270,125.00


Arithmetic
(.025 + .030 + .035) / 3.0 = 3.0% = .030

100000000 * 1.03 * 1.03  * 1.03

$ ?


Geometric
geo_mean = (1.025 * 1.03 * 1.035) ** (1/3.0) 

100000000 * geo_mean * geo_mean * geo_mean

$ ?

"""
