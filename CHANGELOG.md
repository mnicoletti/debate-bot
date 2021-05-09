# Changelog
Todos los cambios relacionados al bot de la comunidad de Debate Videojuegos en Discord será documento en este archivo.

El formato se basa en [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), y este proyecto adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
* Nuevo enum para ordenar datos de APIs de consulta para Apex.
* Se agrega una nueva frase para Perfect Offline.
* Se agrega un nuevo POI de Olympus a la base de datos.
* Nueva clase ApexStats.
* Enum con configuraciones de APIs.

### Changed
* Se mueve la configuración de la URL de consulta de rotación de mapas a un nuevo enum.
* Se agrega nueva temporada a las imágenes.

## [2.1.2] - 2021-05-04
### Changed
* Si no existe un próximo mapa, no manda mensaje.

## [2.1.1] - 2021-04-21
### Fixed
* Arregla las menciones de bokita y boquita.

## [2.1.0] - 2021-04-17
### Added
* Valor install_path en discord.json para obtener el path de instalación de base.
* PerfectData.retrieve_perfect_message consume las frases relacionadas a Perfect a una base de datos.
* Comando para obtener POIs del mapa actual.
* Listado de rotaciones hasta 5.

### Changed
* Todas las frases del bot relacionadas a Perfect, antes hardcodeadas, viven ahora en la base de datos.
* Se modifica la función channel_messages.remember_perfect para consultar las frases de DB.
* Cambio de diseño en tooltip de ayuda.

### Fixed
* Se modifica el campo de update de fecha de offline de Perfect. Era str, ahora es solo un datetime.

## [2.0.1] - 2021-03-27
### Fixed
* Instancia en la cual no se actualizaban datos en una tabla de MariaDB, por falta de autocommit=True.
* El offline_date de Perfect se obtenía como un str y se calculaba contra un datetime, fue solucionado.
* Se solucionó un problema de actualización de datos en bases de datos por estar en un formato incorrecto.

## [2.0.0] - 2021-03-27
### Added
* Nueva clase "DatabaseManager" dedicada a hacer de interface entre el bot y una base de datos MariaDB.
* Creado esquema de base de datos y scripts .sql de instalación.
* Funciones de consulta a un "mapa" de campos, sin condicionales (SELECT).
* Nueva clase ApexMaps, dedicada a obtener información sobre los mapas de Apex y su rotación.

### Changed
* Se arma servicios por "cogs" para formar comandos.

## [1.3.1] - 2021-03-20
### Fixed
* Agregados intents para solucionar aplicación de nuevas reglas de Discord API.

## [v1.3.0] - 2020-11-13
### Changed
* Se hace un log cuando Perfect se pone online.
* Se mueven eventos al main, ya que discord.Client no permite multiples instancias de uno.
* output_msg es ahora una lista.

### Fixed
* Se re-aplica la función this_is_boca.

## [v1.2.0] - 2020-10-08
### Added
* Respuesta automáticas para boquita, el más grande.

## [v1.1.2] - 2020-10-04
### Added
* Respuestas automáticas si Perfect está jugando Apex.

## [v1.1.1] - 2020-09-19
### Added
* Si se menciona a @Perfect ahora se activa remember_perfect

### Fixed
* Solucionado un problema donde la palabra perfecto llamaba al remember_perfect.
* Eliminado un "|" extra en una expresión regular.

## [v1.1.0] - 2020-09-14
### Added
* Logging
* Registro de excepciones en operaciones criticas.
* Configuración en `discord.json` para `log_path` y `log_file`.
* Constructor de `DiscordBotJsonData` ahora carga los datos de `log_file` y `log_path`.
* Modulo `file_management`. Dedicado al manejo de archivos y directorios.

### Changed
* Se reemplaza nombre de clase `DiscordJsonData` por `DiscordBotJsonData`. 

## [v1.0.2] - 2020-09-13
### Added
* Documentación

## [v1.0.1] - 2020-09-13
### Fixed
* Faltaba un mention en una de las frases aleatorias.
* Error de tipos en la presencia del usuario. Se reemplaza `.activity.name` por `.activity` en validación de actividades.

## [v1.0.0] - 2020-09-12
### Added
* Channel Mentions a usuarios que dicen el mensaje.
* Mención a Perfect.
* Calculo de tiempo online.
* Multiples mensajes aleatorios.
* Reconocimiento de actividad.
