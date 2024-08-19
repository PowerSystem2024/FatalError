const HolaMundo ={
    data(){
        return{
            mensaje :'Hello World'
        }
    }
}
Vue.createApp(HolaMundo).mount('#app')