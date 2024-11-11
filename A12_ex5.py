def palindromo(string):
    palavra = string[::-1] 

    return palavra == string
   

if __name__ == "__main__":
    str = input("Insira a palavra que deseja verificar se é um palíndromo ")
    print(palindromo(str))