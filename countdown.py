from time import sleep

for i in range(3, 0, -1):
    print(i)  # run in terminal with and without -u
    # print(f"{i}\n", end="")
    # print(i, "s", sep="\n", end="")
    # print(i, end=" ")  # run in terminal
    # print(i, end=" ", flush=True)  # run in terminal
    # print(i, flush=True)  # run in terminal
    sleep(1)
print("Go!")
