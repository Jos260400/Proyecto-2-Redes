# Proyecto-2-Redes
Proyecto 2 Redes
Juego "Uno"

El proyecto consiste en implementar un juego de cartas online multijugador que utilice un
protocolo propietario (desarrollado por el equipo) para la sincronización de los distintos clientes de
este. El juego debe:
- Soportar 3+ jugadores.
- Permitir estrategia por parte de los participantes (no estar dado exclusivamente por el azar
como Guerra).
- Tener un estado público y un estado privado por jugador (no ser de información perfecta).
- Estar basado en turnos (no ser concurso de velocidad como Speed).
- Permitir chatear entre los jugadores.
- Permitir elegir un nombre al momento de unirse.
- Poder manejar varias “mesas” o “salas”. Es decir, soportar juegos concurrentes que puedan
ocurrir en el servidor.
Como base deben de utilizar la baraja inglesa (4 palos, 52 cartas), aunque pueden utilizarse otras
que sean utilizados por juegos que cumplan los requisitos, como la baraja española o la japonesa.

El servidor del juego debe instalarse en la nube (Azure, AWS, Heroku, DigitalOcean, etc.) y debe ser
desarrollado en un lenguaje de programación diferente al utilizado para la implementación del
cliente.
Se debe levantar un sitio web en el servidor que incluya la explicación del juego, las reglas, etc., así
como la descarga del cliente y las instrucciones para instalarlo/ejecutarlo. Este sitio debe ser
accesible mediante un nombre de dominio, y debe contar con un certificado SSL. Así mismo, se
debe mostrar el checksum MD5 del cliente, de modo que pueda comprobarse que la descarga no
tuvo errores.
El cliente puede ser desarrollado como una aplicación de consola, escritorio o web.


