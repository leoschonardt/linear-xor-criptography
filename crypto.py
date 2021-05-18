palavra_a_ser_criptografada = "CRIPTOGRAFIA" # palavra que será criptografada
chave = "3073246" # chave de criptografia (meu RU)

# está função atribui o valor numérico para cada um dos caracteres ascii e retorna num dicionário do Python
def criar_dicionario_ascii():
  ascii_dict = dict()
  for i in range(0, 256):
    ascii_dict[chr(i)] = i
  return ascii_dict

# esta função insere os zeros a frente dos números binários, para deixá-los todos com os 8 dígitos de um byte
def ajusta_zeros(binario):
  while len(binario) < 8:
    binario = "0" + binario
  return binario

# esta função converte um número decimal em número binário
def decimal_para_binario(num):
  binario = ""
  while num >= 1:
    binario = str(num % 2) + binario
    num = num // 2
  return ajusta_zeros(binario)

# esta função recebe uma string, e transforma seus caracteres em números da tabela ascii e converte os números em binário, por fim retorna uma lista com todos os bytes da palavra
def transmutar_str_para_lista_bytes(str):
  lista = []
  dicionario = criar_dicionario_ascii()
  for char in str:
    lista.append(decimal_para_binario(dicionario[char]))
  return lista

# esta função deixa a lista de bytes da chave com o mesmo tamanho da lista de bytes da palavra, trazendo os primeiros elementos para o final
def ajustar_tamanho_chave(tamanho_palavra, chave):
  tamanho = len(chave)
  for byte in chave:
    chave.append(byte)
    tamanho += 1
    if (tamanho == tamanho_palavra):
      break

# esta função executa a porta lógica xor em dois bytes
def xor(byte1, byte2):
  byte = ""
  for i in range(0, len(byte1)):
    if (byte1[i] != byte2[i]):
      byte = byte + "1"
    else:
      byte = byte + "0"
  return byte

# esta função recebe os bytes da palavra e da chave e aplica a porta xor
def criptografar_lista_bytes(palavra, chave):
  lista = []
  for i in range(0, len(palavra)):
    lista.append(xor(palavra[i], chave[i]))
  return lista

# está função transforma um valor binário em decimal
def binario_para_decimal(byte):
  soma = 0
  invertido = byte[::-1]
  for i in range(0, len(byte)):
    if (invertido[i] == "1"):
      soma += (2 ** i)
  return soma

# esta função converte os bytes em um valor decimal e o esse valor no seu respectivo caracter e concatena todos
def converte_bytes_para_palavra(bytes):
  palavra = ""
  for byte in bytes:
    palavra = palavra + chr(binario_para_decimal(byte))
  return palavra

def realizar_criptografia():
  print("Palavra a ser criptografa: " + palavra_a_ser_criptografada + "\n"
        + "Usando a chave: " + chave + "\n"
        + "Através do algoritmo da porta lógica XOR" + "\n"
        + "========================================================")

  #########################
  # - Para realizar a criptografia criei um dicionário Python com os caracteres Ascii e seus respectivos valores decimais.
  # - Usei esse dicionário para converter os valores decimais de cada caracter da palavra "CRIPTOGRAFIA" .
  # e da chave de criptografica (meu RU), em seus valores binários e os inseri em uma lista. A Lista com os bytes 
  # da chave foi submetida a um tratamento para trazer os primeiros itens e duplicá-los ao final, até as duas listas 
  # terem o mesmo tamanho.
  # - Então peguei essas duas listas com valores binários e submeti os valores à uma validação de porta XOR, e obtive
  # uma lista de bytes com os valores criptografados.
  # - Usei essa lista para converter os valores binários criptografados em valores decimais, e busquei pelos caracteres
  # da tabela Ascii para cada um dos valores.

  # - Para realizar a decriptografia foi o mesmo processo, porém partindo da palavra já criptografada
  #########################

  # converto a chave em bytes e ajusto seu tamanho, para ficar igual à palavra
  lista_bytes_chave = transmutar_str_para_lista_bytes(chave)
  ajustar_tamanho_chave(len(palavra_a_ser_criptografada), lista_bytes_chave)

  # processo de criptografia
  lista_bytes_palavra_criptografar = transmutar_str_para_lista_bytes(palavra_a_ser_criptografada)
  lista_bytes_criptografados = criptografar_lista_bytes(lista_bytes_palavra_criptografar, lista_bytes_chave)
  palavra_criptografada = converte_bytes_para_palavra(lista_bytes_criptografados)

  print("Palavra criptografada:", palavra_criptografada)

  # processo de decriptografia, é o mesmo que o de criptografia
  lista_bytes_palavra_criptografada = transmutar_str_para_lista_bytes(palavra_criptografada)
  lista_bytes_descriptografados = criptografar_lista_bytes(lista_bytes_palavra_criptografada, lista_bytes_chave)
  palavra_descriptografada = converte_bytes_para_palavra(lista_bytes_descriptografados)

  print("Palavra descriptografada:", palavra_descriptografada)

realizar_criptografia()