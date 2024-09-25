<script setup>
const title = 'Fatal Error';
const descripcion = ' Somos Técnicos Universitarios en Programación - UTN';
const residencia = 'San Rafael, Mendoza, Argentina';
const presentacion = 'Hola, Bienvenido a nuestro portafolio de proyectos. Somos  desarrollador web con experiencia en el desarrollo de aplicaciones web y movil';
const redesSociales = [
    { id: 1, name: 'Linkedin', src: '/src/assets/linkedin_icon.svg', url: '' },
    { id: 2, name: 'Instagram', src: '/src/assets/instagram_icon.svg', url: '' },
    { id: 3, name: 'Github', src: '/src/assets/github_icon.svg', url: '' },
    { id: 4, name: 'Curriculum', src: '/src/assets/cv_resume_icon.svg', url: '' },
];
const telefono = '+54 9 2604-820152';
</script>

<template>
<section class="datos-personales">
    <div class="card">
    <h1>{{ title }}</h1>
    <h2>{{ descripcion }}</h2>
    <p>{{ presentacion }}</p>
    <ul class="container-lista">
        <li v-for="red in redesSociales" :key="red.id">
        <a :href="red.url"><img class="icon-redsocial" :src="red.src" width="35rem" :alt="red.name"></a>
        </li>
        </ul>
        <h3>nuestro Teléfono personal: {{ telefono }}</h3>
        <h4>{{ residencia }}</h4>
    </div>
</section>
</template>

<style scoped>
h1{
    font-size: 2.5rem;
}

p{
    font-size: 1.2rem;
    font-weight: 600;
    margin-bottom:1 rem;
}

.card{
    background-color: rgba(28,41,52);
    border-radius: 10px;
    padding: 20px;
    margin : 10px;
    text-align: center;
}

.container-lista{
    display: flex;
    justify-content: center;
    list-style: none;
    padding: 0;
    margin:0;
    text-align: center;
}

.icon-redsocial{
    align-items: center;
    background-color: aliceblue;
    border-radius: 50% ;
    padding: 2px;
    margin :5px;
    box-shadow: 0 0 5px rgba(251,249,240,0.934);
}

h3{
    font-size: 1.2rem;
    font-weight: 600;
}
    
</style>