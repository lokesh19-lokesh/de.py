while True:
    try:
        n= int(input("Plese enter an integer :"))
        break
    except IOError:
        print("not an integer! plese again 123")
    except ValueError:
        print("Not an integer! plese again 456")

        print("You successfully entered ")

