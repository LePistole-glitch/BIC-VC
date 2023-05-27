import numpy as np

def size(sbytes):
    if sbytes <= 0:
        return "0B"
    size_log = int(np.log(sbytes)/np.log(2))
    size_unit = ["B", "KB", "MB", "GB", "TB", "PB", "EB"][size_log//10]
    size_name = "{:.2f} {}".format(sbytes / 1024 ** (size_log//10), size_unit)
    return size_name


if __name__ == "__main__":
    print(size(int(input("Ingresa la cantidad: "))))
