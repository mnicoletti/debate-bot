# Debate Bot
Bot "oficial" de la comunidad de Debate Videojuegos. Único bot con recuerdos reales de la existencia de Perfect.  
Se detalla la instalación, configuración y funciones de 

# Tabla de Contenidos
* [Dependencias](#dependencias)
* [Instalación](#instalacion)
* [Configuración](#configuracion)  
  * [Conectarse como bot](#conectarse-como-bot)  
  * [Persistir datos de Perfect](#persistir-datos-de-perfect)  
* [Uso](#uso)
  * [Linea de comandos](#linea-de-comandos)  
  * [SystemD](#systemd)  
* [Changelog](#changelog)  

# Dependencias
  * [discord.py](https://discordpy.readthedocs.io/en/latest/)

# Instalacion
Por el momento, el bot está pensado para que se corra dentro de una **Raspberry Pi**.  
Clonamos el código del repositorio.

```bash
> cd /opt/
> git clone https://github.com/mnicoletti/debate-bot.git
```

Instalamos python3 y las dependencias que sean necesarias
```bash
> sudo apt-get update
> sudo apt-get upgrade
> sudo apt-get install python3 python3-pip
> sudo apt-get install libmariadb-dev
> pip3 install discord
> pip3 install mariadb
> pip3 install pycurl
```

# Configuracion
## Conectarse como bot
Crear directorio etc/ con archivo **discord.json**. Debe contener los valores de token y nombre de la guild a conectarse.

```json
{
    "token": "valor de token",
    "guild": "nombre de server",
    "log_path": "/var/log/debate-bot",
    "log_file": "debate-bot",
}
```

## Configuración de base de datos
Crear archivo **db_config.json** con la siguiente estructura.
```json
{
    "host": "localhost",
    "port": 3306,
    "user": "debate",
    "pass": "debate",
    "database": "debate"
}
```

## Persistir datos de Perfect
Crear archivo **perfect.json** con la siguiente estructura.

```json
{
    "id": "123123123123123123123", 
    "nickname": "Perfect", 
    "offline_date": "09/11/20 23:17:10"
}
```

# Uso
## Linea de comandos
Podemos utilizar el bot una vez configurado.
```bash
> sudo python3 /opt/debate-bot/__init__.py
```

## SystemD
Podemos dejar el bot como un servicio para systemd utilizando el siguiente template.  

```bash
[Unit]
Description=Debate Discord Bot
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /opt/debate-bot/__init__.py
Restart=on-abort

[Install]
WantedBy=multi-user.target
```

# Changelog
Por ahora, [revisá la página de releases](https://github.com/mnicoletti/debate-bot/releases) para ver los cambios en cada versión.