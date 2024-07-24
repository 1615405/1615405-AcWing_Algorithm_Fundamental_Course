def main():
    x = float(input())
    
    if x == 0:
        print(f"{x:.6f}")
        return
    
    C = x
    x0 = x
    EPS = 1e-8

    while True:
        xi = (2 * x0 * x0 * x0 + C) / (3 * x0 * x0)
        if abs(xi - x0) < EPS:
            break
        x0 = xi
    
    print(f"{x0:.6f}")


if __name__ == "__main__":
    main()
