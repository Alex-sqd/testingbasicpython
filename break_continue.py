def main():
    for contador in range(1000):
        if contador % 2 != 0:
            continue
        else:
            print(contador)

if __name__ == '__main__':
    main()