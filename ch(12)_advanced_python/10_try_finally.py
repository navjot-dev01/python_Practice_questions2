# try:
#     num=int(input("Enter the number:"))
#     print(num) 

# except Exception as e:
#     print(e)

# #finally:  # if finally work in any condition then without finally it also work just write print then why need
# print("I am inside .")

# finally meant for functions .only print dont respond.

def main():
    try:
        num=int(input("Enter the number:"))
        print(num)
        return  

    except Exception as e:
        print(e)
        return

    # finally:
    print("i am inside of finally.")

main() 


