const HolaMundo ={
    data(){
        return{
            mensaje :'Hola Mundo'
        }
    }
}
Vue.createApp(HolaMundo).mount('#app')