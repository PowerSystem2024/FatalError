
<script setup>
import navBar from './components/icons/navBar.vue'
import DatosPersonales from './components/icons/DatosPersonales.vue';
import Educacion from './components/icons/Educacion.vue';
import Experiencia from './components/icons/Experiencia.vue';

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
    <section id="Habilidades"><h2>Habilidades</h2></section>
    <section id="Intereses"><h2>Intereses</h2></section>
  </main>
</template>

<style scoped>
 
</style>



