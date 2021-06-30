# If error occurs in program then execution of program  gets stopped.
# So we use Exception handling, if there is error by handling it executes remaining code It does not stop execution
# eg. Banking Software
# Always close resources when quiting program eg. file cose, database connection
# use finally: it executes when error occurred or not

a=5
b=3

try:
    print("Resource Opening")
    print(a/b)

    k=int(input("Enter a number: "))
    print(k)

except ZeroDivisionError as e:    # e is object
    print("Hey! User you are divide by zero: ",e)

except ValueError as e:
    print("Invalid Input")


except Exception as e:   # these Exception handles error which are not defined
    print("Something went wrong!!!")

finally:   # it executes with or without error occurs
    print("Resource Closing")

print("bye")


# input: a=5 and b=0
# Resource Opening
# Hey! User you are divide by zero:  division by zero
# Resource Closing
# bye


# Resource Opening
# 1.6666666666666667
# Enter a number: p
# Invalid Input
# Resource Closing
# bye