#### USO DE GITHUB Parte 1

GitHub es una plataforma que nos permite guardar repositorios de Git que podemos usar como servidores remotos y ejecutar algunos comandos de forma visual e interactiva (sin necesidad de la consola de comandos).

Luego de crear nuestra cuenta, podemos crear o importar repositorios, crear organizaciones y proyectos de trabajo, descubrir repositorios de otras personas, contribuir a esos proyectos, dar estrellas y muchas otras cosas.

### COMANDOS

**Import repository**, **New repository**, **New organization**: significa que es como tu empresa.  
**New project**: significa que es como un grupo de repositorios que puedes tener dentro de una empresa.  
**New gist**: es un pedacito de código que puedes compartir.

**New repository**  
Ponemos el nombre: `class-git`, descripción: Haremos un blog increíble, hay muchas licencias para publicar el código: NO lo hacemos ahora.

**Create repository**  
Lo ponemos en privado o en público.

El `README.md` es el archivo que veremos por defecto al entrar a un repositorio. Es una muy buena práctica configurarlo para describir el proyecto, los requerimientos y las instrucciones que debemos seguir para contribuir correctamente.

Para clonar un repositorio desde GitHub (o cualquier otro servidor remoto) debemos copiar la URL (por ahora, usando HTTPS) y ejecutar el comando: git clone + URL


Esto descargará la versión de nuestro proyecto que se encuentra en GitHub.

**ATENCIÓN**: ¿Por qué? Porque a través de HTTPS nos pedirá usuario (nombre de perfil) y contraseña.

Sin embargo, esto solo funciona para las personas que quieren empezar a contribuir en el proyecto.

### Cómo conectar un repositorio de GitHub a nuestro documento local

Si queremos conectar el repositorio de GitHub con nuestro repositorio local que creamos, aconsejo que al trabajar desde GitHub no utilicemos localmente el comando `git init`. En su lugar, debemos ejecutar las siguientes instrucciones:

1. Guardar la URL del repositorio de GitHub con el nombre de `origin`:

    ```bash
    git remote add origin URL
    ```

2. Verificar que la URL se haya guardado correctamente:

    ```bash
    git remote
    git remote -v
    ```

3. Traer la versión del repositorio remoto y hacer merge para crear un commit con los archivos de ambas partes. Podemos usar `git fetch` y `git merge` o solo `git pull` con el flag `--allow-unrelated-histories`:

    ```bash
    git pull origin master --allow-unrelated-histories
    ```

4. Por último, ahora sí podemos hacer `git push` para guardar los cambios de nuestro repositorio local en GitHub:

    ```bash
    git push origin master
    ```

### Cómo autenticarte en GitHub 2022

Antes de empezar, debemos renombrar la rama ‘master’ a ‘main’, este es el nuevo estándar en GitHub. Para esto:

1. Primero nos posicionamos en la rama a la que queremos cambiarle el nombre.
2. Ejecutamos el siguiente comando:

    ```bash
    git branch -M main
    ```

### Pasos para crear un token de acceso personal

Desde el 2022, GitHub ya no permite hacer el push con la contraseña del propio GitHub. Para esto, tenemos que crear un token, y este token es la contraseña que vamos a colocar cuando nos pida clave.

### Descubre el uso de tags en Github

Sigue la secuencia:

1. Ingresamos a nuestra cuenta de GitHub.
2. Buscamos **Settings**.
3. Click en **Developer settings**.
4. Click en **Personal access tokens**.
5. Click en **Generate new token**. Aquí se puede colocar un nombre, la fecha de expiración.
6. Tildar en **repo** y luego click en el botón verde **Generate token**.

### PORTAFOLIO

Vamos a ver unos videos de cómo avanzar en lo que es un portafolio por el Tutor:

**Dante Nicolás Martínez**

**Segundo Semestre Parte 1:**

- IntroYpractica
- PDF

Revisar y ejecutar cada comando, hacerlo como práctica. NO olvidar hacer lo requerido por el Tutor **Nico**, lo que sea tarea o investigación.

**Profesor Ariel Betancud**

###### CLASE 02 MIÉRCOLES 21 DE AGOSTO DEL 2024 - Portafolio 2

Vamos a cargar la llave SSH pública en GitHub.

Para copiar la llave pública, debes ir al archivo `.ssh` y allí encontrarás el archivo `.pub`. Lo puedes abrir con un editor de texto, luego copiar el contenido que está dentro.

**Copiar la llave pública**

- Ir a GitHub, vamos a **Settings**, luego a **SSH and GPG keys**.

**Crear una nueva**

- Hacer click en **New SSH key**, poner un nombre y pegar la llave SSH pública. Con esto estará listo.

Aconsejo que la SSH tenga el nombre del ordenador en el que estás trabajando. Esto se debe hacer con cada PC nueva o dispositivo nuevo que tengamos para acceder a nuestra cuenta de GitHub.

### Comandos útiles

```bash
git branch            # Vemos en qué rama estamos

git checkout master   # Ponernos en la rama master

git branch -M main    # Cambiamos el nombre de la rama master a main

git remote add origin git@github.com:nombreUsuario/class-git.git  # Agregamos el repositorio remoto (ejemplo)

git remote -v         # Verificamos si ya está conectado el repositorio remoto

git merge segunda     # Mergeamos lo que tenemos en la rama "segunda" con la rama "main"

git commit -am "Uso de GitHub parte 20"   # Hacemos el commit de hoy

git push origin main  # Enviamos todo lo hecho a GitHub, revisamos en el repositorio de GitHub

Frente al cambio de nombre de la rama master a main, puede suceder que en el repositorio de GitHub se hayan creado dos ramas, master y main. Se debe ir al repo, Settings y allí se puede cambiar la rama principal. En vez de que siga siendo master, cambiar a main, luego de eso ya podemos borrar la rama master.
PORTAFOLIO

Vamos a ver unos videos de cómo avanzar en lo que es un portafolio por el Tutor:

Dante Nicolás Martínez

Segundo Semestre Parte 2:

    Video Capítulo 01
    PDF

Revisar y ejecutar cada comando, hacerlo como práctica. NO olvidar hacer lo requerido por el Tutor Nico, ya sea tarea o investigación.

Profesor Ariel Betancud


##### CLASE 03 MIÉRCOLES 28 DE AGOSTO DEL 2024 - Portafolio 3

### Cambios en GitHub: de master a main

El escritor argentino Julio Cortázar afirma que las palabras tienen color y peso. Por otro lado, los sinónimos existen por definición, pero no expresan lo mismo. Feo no es lo mismo que desagradable, ni aromático es lo mismo que oloroso.

Por lo anterior, podemos afirmar que los sinónimos no expresan lo mismo, no tienen el mismo “color” ni el mismo “peso”.

Sí, esta lectura es parte de la enseñanza profesional de Git & GitHub.

Desde el 1 de octubre de 2020, GitHub cambió el nombre de la rama principal: ya no es “master” -como aprenderás aquí- sino **main**.

Este cambio fue derivado de una profunda reflexión ocasionada por el movimiento **#BlackLivesMatter**.

La industria de la tecnología lleva muchos años usando términos como _master_, _slave_, _blacklist_ o _whitelist_, y esperamos que pronto estos términos puedan ir desapareciendo.

Y sí, las palabras importan.

Por lo que, de aquí en adelante, cada vez que me escuches mencionar “master”, debes saber que hago referencia a “main”.

### ¿Cuándo sigue siendo master y cuándo sigue siendo main?

Cuando se crea un repositorio desde Git Bash en nuestro ordenador a través de `git init`, sigue siendo el estándar como **master**. ¿Qué hacer con esto? Debes cambiar el nombre de la rama **master** a **main** con el siguiente comando:

```bash
git branch -M main

Ahora, cuando creamos un repositorio desde la nube, es decir, desde GitHub, ya verás que la rama principal tiene por defecto el nombre de main, y al clonar a nuestro ordenador seguirá teniendo este nombre, por lo que no será necesario ningún cambio.
PORTAFOLIO

Vamos a ver unos videos de cómo avanzar en lo que es un portafolio por el Tutor:

Dante Nicolás Martínez

Segundo Semestre Parte 3:

    Video Capítulo 02
    PDF

Revisar y ejecutar cada comando, hacerlo como práctica. NO olvidar hacer lo requerido por el Tutor Nico, ya sea tarea o investigación.

Profesor Ariel Betancud

#### CLASE 04 MIÉRCOLES 4 DE SEPTIEMBRE DEL 2024 - Portafolio 4

### Tu primer push

La creación de las SSH es necesaria solo una vez por cada computadora. Aquí conocerás cómo conectar a GitHub usando SSH.

Luego de crear nuestras llaves SSH, podemos entregarle la llave pública a GitHub para comunicarnos de forma segura y sin necesidad de escribir nuestro usuario y contraseña todo el tiempo.

Para esto, debes entrar a la **Configuración de Llaves SSH** en GitHub, crear una nueva llave con el nombre que le quieras dar y el contenido de la llave pública de tu computadora.

Ahora podemos actualizar la URL que guardamos en nuestro repositorio remoto, solo que, en vez de guardar la URL con HTTPS, vamos a usar la URL con SSH:

```bash
ssh

git remote set-url origin url-ssh-del-repositorio-en-github

Comandos para copiar la llave SSH:

Estas son las rutas del SSH público:

    Mac:pbcopy < ~/.ssh/id_rsa.pub

    Windows (Git Bash):clip < ~/.ssh/id_rsa.pub

    Linux (Ubuntu):cat ~/.ssh/id_rsa.pub

mportante

Las buenas costumbres nos enseñan que antes de hacer un push, siempre debemos hacer un pull o un fetch, esto es para que, si alguien ya hizo algún cambio, no se genere un conflicto.
Invitar a un colaborador

Para invitar a un colaborador debemos ir a GitHub y seleccionar:

Settings -> Collaborators -> ingresar contraseña o un F2A de verificación y enviar la invitación escribiendo el nombre de usuario.

Del otro lado, el usuario invitado solo debe aceptar y listo, ya puede participar del proyecto haciendo commit.
PORTAFOLIO

Vamos a ver unos videos de cómo avanzar en lo que es un portafolio por el Tutor:

Dante Nicolás Martínez

Segundo Semestre Parte 4:

    Video Capítulo 03
    PDF

Revisar y ejecutar cada comando, hacerlo como práctica. NO olvidar hacer lo requerido por el Tutor Nico, ya sea tarea o investigación.

Profesor Ariel Betancud

### CLASE 05 MIÉRCOLES 11 DE SEPTIEMBRE DEL 2024 - Portafolio 5

## Git tag y versiones en GitHub

En Git, las etiquetas o **Git tags** tienen un papel importante al asignar versiones a los commits más significativos de un proyecto. Aprender a utilizar el comando `git tag`, entender los diferentes tipos de etiquetas, cómo crearlas, eliminarlas y compartirlas, es esencial para un flujo de trabajo eficiente.

### Creación de etiquetas en Git

```sh
git tag

Las etiquetas anotadas almacenan información adicional como la fecha, etiquetador y correo electrónico, y son ideales para publicaciones públicas. Las etiquetas ligeras son más simples y se emplean como “marcadores” de una confirmación específica.

Esto mostrará una lista de las etiquetas existentes, como:

    v1.0
    v1.1
    v1.2

Para perfeccionar la lista, puedes utilizar opciones adicionales, como -l con una expresión comodín.
Uso compartido de etiquetas

Compartir etiquetas requiere un enfoque explícito al usar el comando git push. Por defecto, las etiquetas no se envían automáticamente. Para enviar etiquetas específicas, utiliza:
git push origin <nombre-de-etiqueta>

Para enviar varias etiquetas a la vez, usa:
git push origin --tags

Eliminación de etiquetas

Para eliminar una etiqueta, usa el siguiente comando:
git tag -d <nombre-de-etiqueta>


Esto eliminará la etiqueta identificada en el repositorio local.

En resumen, las etiquetas en Git son esenciales para asignar versiones y capturar instantáneas importantes en el historial de un proyecto. Aprender a crear, listar, compartir y eliminar etiquetas mejorará tu flujo de trabajo con Git.
PORTAFOLIO

Vamos a ver unos videos de cómo avanzar en lo que es un portafolio por el Tutor:

Dante Nicolás Martínez

Segundo Semestre Parte 5:

    Video Capítulo 04
    PDF

Revisar y ejecutar cada comando, hacerlo como práctica. NO olvidar hacer lo requerido por el Tutor Nico, ya sea tarea o investigación.

Profesor Ariel Betancud

### CLASE 06 MIÉRCOLES 18 DE SEPTIEMBRE DEL 2024 - Portafolio 6

## Error con los tags

### Investigación: ¿Qué pasa si por error cargamos un tag dos veces?

¿Cómo solucionarías este problema o error?

La respuesta debe ser enviada antes de las 23 horas por cada grupo. Deben enviar comandos y todos los pasos que harían frente a este conflicto.

### PORTAFOLIO

Vamos a ver unos videos de cómo avanzar en lo que es un portafolio por el Tutor:

**Dante Nicolás Martínez**

**Segundo Semestre Parte 6:**

- Video Capítulo 05
- PDF

Revisar y ejecutar cada comando, hacerlo como práctica. NO olvidar hacer lo requerido por el Tutor **Nico**, ya sea tarea o investigación.

**Profesor Ariel Betancud**

# CLASE 07 - MIÉRCOLES 25 DE SEPTIEMBRE DEL 2024

## Portafolio 7

### Error con los tags
**Investigación:** Si un tag es imposible generarlo dos veces, ¿cómo es que existe el error de dos tags con el mismo nombre?

#### ¿Cómo se origina este problema o error?

La respuesta debe ser enviada antes de las **23 horas** por cada grupo. Deben enviar comandos y todos los pasos que harían frente a este conflicto.

---

## PORTAFOLIO

Vamos a ver unos videos de cómo avanzar en el portafolio proporcionados por el tutor:

### Tutor: Dante Nicolás Martinez

#### Segundo Semestre Parte 6:

- **Video:** Capítulo 06

- **PDF:** Revisar y ejecutar cada comando. 

Realizarlo como práctica y **no olvidar** hacer lo requerido por el tutor Nico, ya sea tarea o investigación.

---

### Profesor: Ariel Betancud


# CLASE 08 - MIÉRCOLES 2 DE OCTUBRE DEL 2024

## Portafolio 8

### Manejo de ramas en GitHub

Si no te funciona el comando `gitk`, es posible que no lo tengas instalado por defecto.
Para instalar `gitk` debemos ejecutar los siguientes comandos:

```sh
  sudo apt-get update
  sudo apt-get install gitk

Repasa: ¿Qué es Git?

Las ramas nos permiten hacer cambios a nuestros archivos sin modificar la versión principal (main). Puedes trabajar con ramas que nunca envías a GitHub, así como pueden haber ramas importantes en GitHub que nunca usas en el repositorio local. Lo crucial es que aprendas a manejarlas para trabajar profesionalmente.

Si, estando en otra rama, modificamos los archivos y hacemos commit, tanto el historial (git log) como los archivos serán afectados. La ventaja que tiene usar ramas es que las modificaciones solo afectarán a esa rama en particular. Si luego de "guardar" los archivos (usando commit) nos movemos a otra rama (git checkout otraRama), veremos que las modificaciones de la rama pasada no aparecen en otraRama.
Comandos para manejo de ramas en GitHub

    Crear una rama:

git branch branchName # Crear una rama
git checkout branchName # Movernos a otra rama 
git checkout -b nombre-de-la-rama # Crear una rama en el repositorio local
git push origin nombre-de-la-rama # Publicar una rama local al repositorio remoto

Recuerda que podemos ver gráficamente nuestro entorno y flujo de trabajo local con Git utilizando el comando gitk. Gitk fue el primer visor gráfico desarrollado para ver de manera gráfica el historial de un repositorio de Git.
PORTAFOLIO

Vamos a ver unos videos de cómo avanzar en el portafolio proporcionados por el tutor:
Tutor: Dante Nicolás Martinez
Segundo Semestre Parte 7:

    Video: Capítulo 07

    PDF: Revisar y ejecutar cada comando.

Realizarlo como práctica y no olvidar hacer lo requerido por el tutor Nico, ya sea tarea o investigación.

## CLASE 09

**MIÉRCOLES 9 DE OCTUBRE DEL 2024 - Portafolio 9**

### Tarea para antes de las 23 horas
Investigar cómo se puede clonar un repositorio con el HTTPS del mismo, siendo ustedes los dueños del repositorio. Desde la nube quieren traer este repo a nuestro ordenador. Se les pedirá **Username** y **password**: ¿qué se debe hacer para lograr hacer cambios y así utilizar **pull**, **push**, y todo lo necesario para trabajar? Como referencia, solo usuario y contraseña no serán suficientes; esto cambió desde el año 2021 y ahora hay algo más para poder hacer esto y tener así acceso total.

### Configurar múltiples colaboradores en un repositorio de GitHub
Por defecto, cualquier persona puede clonar o descargar tu proyecto desde GitHub, pero no pueden crear commits ni ramas. Esto significa que pueden copiar tu proyecto, pero no colaborar con él. Si el repositorio es privado, es necesario que realmente estés haciendo una invitación; de lo contrario, no lo van a poder ver. Existen varias formas de solucionar esto para aceptar contribuciones. Una de ellas es añadir a cada persona de nuestro equipo como colaborador de nuestro repositorio.

#### Cómo agregar colaboradores en GitHub
1. Entrar a la configuración de colaboradores de nuestro proyecto:
   - Repositorio > Settings > Collaborators
2. Ahí, debemos añadir el email o username de los nuevos colaboradores.

### Cambiar el mensaje del commit
Si, como colaborador, agregaste erróneamente el mensaje del commit, lo puedes cambiar de la siguiente manera:
```bash
git commit --amend # Corregimos el mensaje
git pull origin main # Traer el repositorio remoto
git push --set-upstream origin main # Ejecutar el cambio, error arreglado

Comienzo del colaborador

    Abre git bash:

    bash
    cd Documentos # Abre git bash
    mkdir class-git # Crea la carpeta o directorio de trabajo
    ls -al # Revisa los archivos o directorios que tienes

No debe hacer un git init, debe buscar el repositorio en el cual está invitado a participar en GitHub.
Clona desde HTTPS, copia la URL:

bash
git clone url-copiada-github # Esto hace que clonemos el repositorio

    No pide ni usuario ni contraseña si el repositorio es público.

Realizando cambios

    Abre Visual Studio Code y comienza con cambios:

    bash
    code . # Abre VSC y comienza con cambios
    vim historia.txt # Vamos a escribir: Aquí está un nuevo colaborador

Para modificar el mensaje del commit en Ubuntu:

bash
ctrl + x # Para salir de vim 
s # Para un sí 
enter # Terminado el mensaje del commit 

En git bash window:

bash
esc # Presionamos esc después de terminar de escribir
:wq! # Para salir del editor vim en Windows

Comandos adicionales

bash
git status 
git commit -am "Mi primer commit, estoy muy emocionado!!!" 
git pull origin main 
git fetch 
git branch # Para ver las ramas que se trajo 
git log # Para ver toda la historia 
git log --graph # Vemos el gráfico de las diferentes ramas 
git push origin main # Pedirá email y contraseña del colaborador 

Problemas comunes y soluciones

    Si se recibe un error denegado:
        El dueño del repositorio no le dio acceso: el dueño debe agregar al colaborador.
    Ir a settings del repositorio:
        Agregar correo o nombre de usuario: el colaborador debe tener un email público.
    Enviar un email con la URL; GitHub envía una notificación al usuario invitado.
    El colaborador debe aceptar la invitación para tener acceso total.

Reparto del trabajo entre colaboradores
A partir de ahora, el dueño del repositorio y el colaborador deberán repartir el trabajo utilizando distintas ramas:

    El dueño trabajará desde la rama header.
    El colaborador desde la rama footer.
    Al final, cuando se termine, se hará un merge para finalizar el proyecto.

PORTAFOLIO
Vamos a ver unos videos sobre cómo avanzar en lo que es un portafolio por el Tutor:

    Dante Nicolás Martinez
    Segundo Semestre Parte 8:
        Video Capítulo 08

PDF Revisar y ejecutar cada comando, hacerlo como práctica: NO olvidar hacer lo requerido por el Tutor Nico, lo que sea tarea o investigación. Profesor Ariel Betancudull origin main

# Clase 10 - Miércoles 16 de Octubre de 2024

## Tema: Flujo de Trabajo Profesional - Merge de ramas de desarrollo a main

En esta clase aprendimos a realizar merges de ramas de desarrollo hacia la rama `main` siguiendo un flujo de trabajo profesional, el cual es fundamental para el desarrollo de software colaborativo de manera ordenada y sin interrupciones.

### Flujo de trabajo sugerido:

1. Crear ramas para cada funcionalidad o tarea.
2. Asignar una rama a cada desarrollador.
3. El programador baja el repositorio con `git pull origin master`.
4. El programador cambia a su rama con `git checkout #nombre_rama`.
5. Trabaja en su rama, haciendo commits regularmente.
6. Sube su trabajo al repositorio remoto con `git push origin #nombre_rama`.
7. El encargado del proyecto baja, revisa y unifica los cambios mediante un merge hacia `main`.

### Portafolio

Además, trabajamos en la creación de un portafolio guiados por el tutor **Dante Nicolás Martinez**. Actualmente estamos en el segundo semestre, siguiendo la parte 8 del material.

- **Video:** Capítulo 9
- **Material adicional:** PDF con los comandos y flujo de trabajo para Git

**Nota importante:** No olvidar revisar y ejecutar cada comando como práctica y realizar las tareas o investigaciones solicitadas por el tutor **Nico**.

---


**Profesor:** Ariel Betancud  
**Tutor:** Dante Nicolás Martinez
