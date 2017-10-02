

x = [str(x) for x in raw_input(">>> ").split(",") if int(x)%2 != 0]

print ",".join(x)
