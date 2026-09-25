def read_text(message):
    while True:
        value=input(message).strip()

        if value!="":
            return value

        print("This Field Cannot Be Empty.")


def read_amount(message):
    while True:
        try:
            amount=float(input(message))

            if amount>0:
                return amount

            print("Amount Must Be Greater Than Zero.")

        except ValueError:
            print("Please Enter A Valid  Number.")




            
