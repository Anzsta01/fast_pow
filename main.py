def main():
    base = 3
    power = 29
    fast_powering(base, power)


def fast_powering(base, power):
    starting_base = base
    power_in_binary = bin(power)[2:]
    print(power_in_binary)
    result = 1
    dupa = 0b1
    for bit in power_in_binary[::-1]:
        if bit == '1':
            result *= base
            base *= base
            dupa <<= 1
            print(f"{starting_base}^{dupa} = {base}, current bit = {bit} result = {result}")
        else:
            base *= base
            dupa <<= 1
            print(f"{starting_base}^{dupa} = {base}, current bit = {bit} result = {result}")
    print(f"{starting_base}^{power} = {result}")
    return result


if __name__ == '__main__':
    main()
