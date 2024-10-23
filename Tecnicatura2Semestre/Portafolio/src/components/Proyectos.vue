<script setup>
import { ref } from 'vue';
var misProyectos = ref([])   
misProyectos.value = ([
  // Este es un array de objetos que contiene información sobre los proyectos
  {
    id: 1,
    src: "/src/assets/restaurant.png",  // Ruta de la imagen del proyecto
    titulo: "Aplicación de Reservas para Restaurantes (2023)",
    descripcion: "Creé una aplicación móvil con Flutter que permite a los usuarios reservar mesas en restaurantes locales.",
    projectLink: "https://www.google.com.ar",  // Enlace al proyecto
    githubLink: "https://github.com/usuario/proyecto"  // Enlace al repositorio de GitHub
  },
  {
    id: 2,
    src: "/src/assets/e-learning.png",
    titulo: "Plataforma de E-Learning (2022)",
    descripcion: "Diseñé y desarrollé una plataforma de educación en línea utilizando Django y React. Con diferentes funcionalidades.",
    projectLink: "https://www.google.com.ar",
    githubLink: "https://github.com/usuario/proyecto"
  },
  {
    id: 3,
    src: "/src/assets/blog.png",
    titulo: "Blog Personal con CMS (2022)",
    descripcion: "Construí un blog personal con un sistema de gestión de contenidos (CMS) personalizado en WordPress.",
    projectLink: "https://www.google.com.ar",
    githubLink: "https://github.com/usuario/proyecto"
  },
  {
    id: 4,
    src: "/src/assets/restaurant.png",
    titulo: "Aplicación de Reservas para Restaurantes (2023)",
    descripcion: "Creé una aplicación móvil con Flutter que permite a los usuarios reservar mesas en restaurantes locales.",
    projectLink: "https://www.google.com.ar",
    githubLink: "https://github.com/usuario/proyecto"
  }
]);
</script>

<template>
    <!-- Aquí va el código HTML de la galería de proyectos -->
      <section id="proyectos">
    <div class="galeria">
      <!-- Itera sobre cada proyecto en la lista de misProyectos -->
        <li class="proyecto" v-for="proyecto in misProyectos" :key="proyecto.id">
          <!-- Muestra la imagen del proyecto utilizando v-bind para el atributo src -->
          <img :src="proyecto.src" :alt="proyecto.titulo" />
          <div class="proyecto-info">
            <!-- Muestra el título y la descripción del proyecto utilizando la interpolación de Vue.js -->
            <h3>{{ proyecto.titulo }}</h3>
            <p>{{ proyecto.descripcion }}</p>
            <div class="proyecto-links">
              <a :href="proyecto.proyectoLink" class="btn-ver-mas" target="_blank" rel="noopener noreferrer">Ver Proyecto</a>
              <a :href="proyecto.githubLink" class="github-link" target="_blank" rel="noopener noreferrer">Ver código en GitHub</a>
            </div>
          </div>
        </li>
    </div>
     </section>
  </template>

<style scoped>
.galeria {
    width: 100%;
    height: 100%;
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    padding: 20px;
    justify-content: center;
    background: linear-gradient(-45deg,#021526,#03346e,#6EACDA,#E2E2B6);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
}

/* Define una animacion llamada "gradient" para cambiar la posicion del fondo */
@keyframes gradient {
    /* Al inicio, el fondo esta posicionado en el 0% horizontal y 50% vertical */
    0% {
        background-position: 0% 50%;
    }

    50% {
        background-position: 100% 50%;
    }

    100% {
        background-position: 0% 50%;
    }
}

.proyecto {
    display: flex;
    flex-direction: column;
    border: 2px solid #ddd;
    border-radius: 8px;
    overflow: hidden;
    background-color: #f9f9f9;
    max-width: 222px;
    flex: 1 1 300px;
}
.proyecto img {
    width: 100%;
    height: auto;
    display: block;
}
.proyecto-info {
    padding: 15px;
    text-align: center;
}
.proyecto-info h3 {
    margin: 10px 0;
    font-size: 1.3em;
    color: #333;
}

.proyecto-info p {
    margin: 10px 0;
    font-size: 1em;
    color: #666;
}

.proyecto-links {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-top: 10px;
}

.proyecto-links .btn-ver-mas {
    background-color: #007BFF;
    color: #fff;
    padding: 10px 15px;
    border-radius: 5px;
    text-decoration: none;
    transition: background-color 0.3s;
}

.proyecto-links .btn-ver-mas:hover {
    background-color: #0056b3;
}

.proyecto-links .github-link {
    color: #333;
    text-decoration: none;
    font-size: 0.9em;
}

.proyecto-links .github-link:hover {
    text-decoration: underline;
}
</style>