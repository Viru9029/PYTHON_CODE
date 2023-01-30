filename = input("Enter the filename with extension : ")
extension = filename.split(".")
print("The extension of file is : " + repr(extension[-1]))