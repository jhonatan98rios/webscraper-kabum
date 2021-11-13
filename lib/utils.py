def writeFile(file_path, data):
    # Writing to file
    with open(file=file_path, mode="w", encoding="utf-8") as file:
        # Writing data to a file
        file.write(data)
        file.close()