
def save_file(code):
     """
     
      use this tool to write and save code or to generate pdf and save it  to the local machine ! 
      use the code tool to generate codes
      args:

      code : - > it expects code so to generate any pdf file or python script just pass the code !
     
     """

     with open("try.py","w") as file:
      file.write(code)
      return "Code has been saved in test.py file !"
