import os

# open and read the file after the appending:

if os.path.isfile("demofile2.txt"):

    while True:
        i = int(
            input(
                "File exist:\n1 - read only\n2 - write only\n3 - Quit\nSelect Operation:"
            )
        )

        if i == 1:
            f = open("demofile2.txt", "r")
            print(f.read())
            f.close()  # close the file after reading
            

        elif i == 2:
            f = open("demofile2.txt", "a")
            f.write(str(input("Write:" + "\n")) + "\n")
            f.close()  # close the file after writing
            f = open("demofile2.txt", "r")
            print(f.readline())
            f.close()  # close the file after reading
            
        elif i == 3:
            break

        else:
            print("Invalid option. Please choose 1 for read only or 2 for write only.")
            break  # exit loop on invalid option

else:
    f = open("demofile2.txt", "a")
    f.write("Now the file has more content!")
    f.close()  # close the file after writing
    f = open("demofile2.txt", "r")
    print(f.read())
    f.close()  # close the file after reading

