<template>
  <section id="habilidades">
    <h2>Mis Habilidades</h2>
    <div class="categorias">
      <!-- Itera sobre cada categoría de habilidades -->
      <div v-for="categoria in habilidades" :key="categoria.id" class="categoria">
        <h3>{{ categoria.nombre }}</h3>
        <ul class="habilidades-lista">
          <!-- Itera sobre cada habilidad dentro de la categoría -->
          <li v-for="habilidad in categoria.habilidades" :key="habilidad.id" class="habilidad-item">
            <!-- Muestra el ícono de la habilidad y su nivel -->
            <img :src="habilidad.icono" :alt="habilidad.nombre" class="habilidad-icono" />
            <div>
              <h4>{{ habilidad.nombre }}</h4>
              <p>Nivel: {{ habilidad.nivel }}</p>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';

// Ejemplo de datos reactivos para las habilidades
const habilidades = ref([
  {
    id: 1,
    nombre: 'Lenguajes de Programación',
    habilidades: [
      { id: 1, nombre: 'JavaScript', nivel: 'Avanzado', icono: 'https://imgs.search.brave.com/H4dFBKxly4jE37AKOa_GMfBrxmcE502XMGF8XyKYpeM/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9kZXNh/cnJvbGxvd2ViLmNv/bS9zdG9yYWdlL3Rh/Z19pbWFnZXMvYWN0/dWFsLzNCcFVEQnND/M29mQnk0dG9yVDFa/aVVGNmhkb25xcFJI/ODQxTWVNRE0ucG5n' },
      { id: 2, nombre: 'Python', nivel: 'Intermedio', icono: 'https://imgs.search.brave.com/UURfYnMhrxwpFe2BgJ2GwMXCmu6u5LR5cpoicsOXtd8/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jbGlw/YXJ0LWxpYnJhcnku/Y29tL2ltYWdlX2dh/bGxlcnkyL1B5dGhv/bi1Mb2dvLUZyZWUt/RG93bmxvYWQtUE5H/LnBuZw' },
      { id: 3, nombre: 'Solidity', nivel: 'Básico', icono: 'https://imgs.search.brave.com/hcFVP3exVpfiqJdoslKKRBqYFNtIOu9pXLbuQhGHkCs/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5saWNkbi5jb20v/ZG1zL2ltYWdlL0Q0/RDEyQVFHeHZOc29l/ckZDU3cvYXJ0aWNs/ZS1jb3Zlcl9pbWFn/ZS1zaHJpbmtfNjAw/XzIwMDAvMC8xNjc2/MjI2MTQ2NzM2P2U9/MjE0NzQ4MzY0NyZ2/PWJldGEmdD1ORnBy/RnQ4X3cxYWFnYlRP/Z3Y4R2FOcjJiVF9v/UzBkWEFuNzFPck5C/ZHZJ' }
    ]
  },
  {
    id: 2,
    nombre: 'Frameworks y Librerías',
    habilidades: [
      { id: 1, nombre: 'React.js', nivel: 'Avanzado', icono: 'https://imgs.search.brave.com/vOOE-z-dNz98PrvEVnF5NDGWqh0pncbI2tsbN0Mvcjg/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9kZXNh/cnJvbGxvd2ViLmNv/bS9zdG9yYWdlL3Rh/Z19pbWFnZXMvYWN0/dWFsL24zbTJBejBW/V0hGZGI0bmczcTlK/YkRyYkNqYXI4aEU3/SzBTVjdNOG4ucG5n' },
      { id: 2, nombre: 'Vue.js', nivel: 'Intermedio', icono: 'https://imgs.search.brave.com/awrWoxCMm_rO4eWHRs4rcYbxjubLb8x0b4HMuJghMj0/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly93d3cu/dzNzY2hvb2xzLmNv/bS93aGF0aXMvaW1n/X3Z1ZS5qcGc' },
      { id: 3, nombre: 'Node.js', nivel: 'Avanzado', icono: 'https://imgs.search.brave.com/LiZbg2M4qKe8a_N_wtwfiRJXBjy3YJXJg41pofNizAY/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9kZXNh/cnJvbGxvd2ViLmNv/bS9zdG9yYWdlL3Nl/cmllX2ltYWdlcy9F/WTlrR2R2MlRQVmFm/NjIzUDJOMmdiTGJy/V05vdFFsQnNRbnpS/QWtOLmpwZWc' },
      { id: 4, nombre: 'Bootstrap', nivel: 'Avanzado', icono: 'https://imgs.search.brave.com/spSRfNho1-JmBVkGlt9s7YS3QGZbsuG3OJB6fj7G6R0/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly93d3cu/dzNzY2hvb2xzLmNv/bS93aGF0aXMvaW1n/X2Jvb3RzdHJhcC5w/bmc' }

    ]
  },
  {
    id: 3,
    nombre: 'Herramientas y Software',
    habilidades: [
      { id: 1, nombre: 'Docker', nivel: 'Intermedio', icono: 'https://imgs.search.brave.com/Wic81hXyVoKnZzItBx-sX_CBCKn_5Y09F3CMsP4Bxu8/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9sb2dv/cy1kb3dubG9hZC5j/b20vd3AtY29udGVu/dC91cGxvYWRzLzIw/MTYvMDkvRG9ja2Vy/X2xvZ28tNzAweDU4/OC5wbmc' },
      { id: 2, nombre: 'Figma', nivel: 'Intermedio', icono: 'https://imgs.search.brave.com/RMDyVusaHu2-no2UZlUFV_GuCZsmcMTQhoO1g3L-Mzg/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9zdGF0/aWMucGxhdHppLmNv/bS9tZWRpYS9hY2hp/ZXZlbWVudHMvcGll/emFzLWxhbmRpbmct/ZmlnbWEtYmFkZ2Ut/YWI4ZGEzYjEtNDE0/ZC00YzBlLWE0ZDct/NzExZGZiYjdiNzcw/LnBuZw' },
      { id: 3, nombre: 'Visual Studio Code', nivel: 'Avanzado', icono: 'https://imgs.search.brave.com/BDx9MCfRPFzWjcX3GAwITaH8rDE7nM5ElWDevSRIdAY/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pbWFn/ZXMtZWRzLXNzbC54/Ym94bGl2ZS5jb20v/aW1hZ2U_dXJsPTRy/dDkubFhEQzRIXzkz/bGFWMV9lSE0wT1lm/aUZlTUkycDlNV2ll/MEN2TDk5VTRHQTFn/ZjZfa2F5VHRfa0Ji/bEZ3SHdvOEJXOEpY/bHFmbll4S1BtbUJS/WHA5MTJMdy4wWXhn/MkRmVk9oMWduS1hS/UWVLYjhtOERBMkpr/eDZYd2sweVlBMjNV/ZGUuSnJIeDNRakp2/OWh2VU5LWmhGWUpG/SlAyUXRGNnpSRURa/ay0mZm9ybWF0PXNv/dXJjZQ' }
    ]
  },
  {
    id: 4,
    nombre: 'Bases de Datos',
    habilidades: [
      { id: 1, nombre: 'MongoDB', nivel: 'Avanzado', icono: 'https://imgs.search.brave.com/NAyWWOOS31IUwBq_A48JOfw2c119eZMg8mBA_4sG3cU/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9zdHls/ZXMucmVkZGl0bWVk/aWEuY29tL3Q1XzJy/andkL3N0eWxlcy9j/b21tdW5pdHlJY29u/X3Zla3pmM29hdHJz/NjEucG5n' },
      { id: 2, nombre: 'MySQL', nivel: 'Intermedio', icono: 'https://imgs.search.brave.com/CnslUfsK0qtHZGqRQpKO0tyHbXI8avmYXCiQydzynNU/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly93d3cu/bG9nby53aW5lL2Ev/bG9nby9NeVNRTC9N/eVNRTC1Mb2dvLndp/bmUuc3Zn' },
      { id: 3, nombre: 'PostgreSQL', nivel: 'Intermedio', icono: 'https://imgs.search.brave.com/cRYMDz-JxHAkAACLKH8kktAvcA23WhZnFBlLKEp51Qk/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly93d3cu/cG9zdGdyZXNxbC5v/cmcvbWVkaWEvaW1n/L2Fib3V0L3ByZXNz/L2VsZXBoYW50LnBu/Zw' }
    ]
  }
]);
</script>

<style scoped>
/* Estilos del contenedor de las categorías */
.categorias {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: space-between;
}

.categoria {
  flex-basis: 48%; /* Para hacer que las categorías ocupen el 48% del ancho del contenedor */
  background-color: #f9f9f9;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.habilidades-lista {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.habilidad-item {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.habilidad-icono {
  width: 40px;
  height: 40px;
  margin-right: 15px;
}

.habilidad-item h4 {
  margin: 0;
  font-size: 1.2em;
}

.habilidad-item p {
  margin: 5px 0 0;
  color: #555;
}

/* Estilos generales */
#habilidades {
  padding: 40px;
  background-color: #f0f0f0;
}

#habilidades h2 {
  text-align: center;
  font-size: 2.5em;
  margin-bottom: 20px;
}

#habilidades h3 {
  font-size: 1.8em;
  color: #333;
}

#habilidades h4 {
  color: #333;
  font-size: 1.2em;
}

</style>
