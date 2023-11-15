def main():
    base = 3
    power = 29
    print(fast_powering(base, power))


def fast_powering(base, power):
    power_in_binary = bin(power)[2:]
    result = 1
    for bit in power_in_binary[::-1]:
        if bit == '1':
            result *= base
            base *= base
            print()
        else:
            base *= base
    return result


if __name__ == '__main__':
    main()
