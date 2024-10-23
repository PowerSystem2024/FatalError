
<script setup>
import navBar from './components/navBar.vue'
import DatosPersonales from './components/DatosPersonales.vue';
import Educacion from './components/Educacion.vue';
import Experiencia from './components/Experiencia.vue';
import Proyectos from './components/Proyectos.vue';
import Habilidades from './components/Habilidades.vue';
</script>

<template>
  <header>
    <!--Barra de navegacion-->
    <navBar/>
    <!--componentes datos personales-->
    <DatosPersonales/>

   

  </header>
  <main>
    <section id="Educacion"><h2>Educacion-cursos</h2></section>
    <Educacion/>
    <section id="Experiencia"><h2>Experiencia</h2></section>
     <Experiencia/>
    <section id="Proyectos"><h2>Proyectos</h2></section>
    <Proyectos/>

    <section id="Habilidades"><h2>Habilidades</h2></section>
    <Habilidades/>
    <section id="Intereses"><h2>Intereses</h2></section>
  </main>
</template>

<style scoped>
 
</style>



