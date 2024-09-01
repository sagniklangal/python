for i in range(2,21):
    with open(f"Table of {i}.txt","w") as a:
        for j in range(1,11):
            a.write(f"{i}x{j}={i*j}\n")
