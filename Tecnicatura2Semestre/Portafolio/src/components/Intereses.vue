<script setup>
import { ref } from "vue";
import Fondo from './Fondo.vue';

const intereses = ref([
    "Desarrollo y programación de páginas web: Contribuir a proyectos en Github, colaborando con otros programadores para mejorar en mi desarrollo profesional y personal.",
    "Entrenamiento personal: Disfruto de entrenar de forma focalizada, con entrenamiento de fuerza, hipertrofia y running.",
    "Videojuegos y música: Disfruto mucho de jugar videojuegos y de la música, como pasatiempos, me relajan demasiado. También me gustaría aprender a desarrollar videojuegos y crear uno.",
]);
</script>

<template>
    <section id="intereses">
        <div class="intereses-contenedor">
            <Fondo/>
            <ul class="contenedor-lista">
                <li class="item" v-for="interes in intereses" :key="interes">
                    {{ interes }}
                </li>
            </ul>
        </div>
    </section>
</template>

<style scoped>
.intereses-contenedor {
    position: relative;
    width: 100%;
    height: 100vh; /* Asegura que el fondo ocupe toda la altura */
    overflow: hidden; /* Evita desplazamientos no deseados */
    display: flex;
    align-items: center;
    justify-content: center;
}

/* Fondo de lava */
.intereses-contenedor > *:first-child {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1; /* Coloca el fondo detrás del contenido */
}

/* Contenedor de la lista de intereses */
.contenedor-lista {
    position: relative;
    list-style-type: none;
    padding: 1rem;
    color: var(--vt-c-white-soft);
    font-size: 1.4rem;
    text-shadow: 3px 3px 6px rgba(0, 0, 0, 1);
    z-index: 1; /* Coloca el contenido sobre el fondo */
    margin: 0;
}

/* Estilo de cada elemento en la lista */
.item {
    margin-bottom: 1rem;
}
</style>
