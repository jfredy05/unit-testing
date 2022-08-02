# unit-testing
Python Unit Testing

Comandos

1. Ejecutar test a una función dentro de un archivo
    * pytest \
    -> <name_file>::<name_function> -v

2. Buscar función con un string "add"
    * pytest <name_file> \
    -> -v -k "add"

3. Buscar función con multiples argumentos de cadena.
    * pytest <name_file> \
    -> -v -k "add or string"

4. Buscar función con multiples argumentos de cadena. (pero los contiene ambos)
    * pytest <name_file> \
    -> -v -k "add and string"