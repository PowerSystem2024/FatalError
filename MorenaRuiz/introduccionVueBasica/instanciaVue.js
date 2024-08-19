const holaMundo ={
    data(){
        return{
            mensaje: "Hola mundo"
        }
    }
}
Vue.createApp(holaMundo).mount('#app')