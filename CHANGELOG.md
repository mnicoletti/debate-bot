# Changelog
Todos los cambios relacionados al bot de la comunidad de Debate Videojuegos en Discord será documento en este archivo.

El formato se basa en [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), y este proyecto adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
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
