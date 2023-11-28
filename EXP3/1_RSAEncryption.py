import math


def calculate_minimal_unconcealed_sum(primes):
    """
    计算给定质数 P 和 Q 的条件下，产生最少未隐藏信息数量的指数 e 的总和。
    """
    P, Q = primes
    totient = (P - 1) * (Q - 1)
    min_unconcealed_p = min_unconcealed_messages(P)
    min_unconcealed_q = min_unconcealed_messages(Q)

    return sum(
        e for e in range(totient)
        if min_unconcealed_p[e % (P - 1)] and min_unconcealed_q[e % (Q - 1)]
    )


def min_unconcealed_messages(prime):
    """
    返回一个列表，指示给定质数的每个指数 e 是否产生最小的未隐藏信息数量。
    """
    unconcealed_counts = [
        unconcealed_count(prime, e) if math.gcd(e, prime - 1) == 1 else float('inf')
        for e in range(1, prime)
    ]
    min_count = min(unconcealed_counts)
    return [count == min_count for count in unconcealed_counts]


def unconcealed_count(modulus, exponent):
    """
    对于给定的模数和指数，计算未隐藏信息的数量。
    """
    return sum(pow(m, exponent, modulus) == m for m in range(modulus))


primes = (1009, 3643)
result = calculate_minimal_unconcealed_sum(primes)
print(f"具有最小未隐藏信息的指数总和: {result}")
