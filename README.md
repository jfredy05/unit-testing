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

5. Detenerse en un error.
    * pytest -v -x

6. Detenerse en un máximo de 2 errores.
    * pytest -v -x --maxfail=2

7. No enviar los detalles de la salida en la consola.
    * pytest -v -x --maxfail=2 --tb=no

8. Decoradores para mostrar por tipo
    * pytest -v -m number
    @pytest.mark.number

9. omitir una prueba con un decorador
    @pytest.mark.skip

10. Debugger
    * pytest --pdb
    * pytest --trace

11. Pasar parametros en el test
    @pytest.mark.parametrize(...

12. Definir una función principal de los pasos que se deben realizar antes de ejecutar cualquier prueba
    @pytest.fixture
    @pytest.fixture(scope='module')


