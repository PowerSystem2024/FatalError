<template>
    <div class="animated-background">
      <div class="wave"></div>
    </div>
  </template>
  
  <script>
  export default {
    name: "AnimatedWaves",
  };
  </script>
  
  <style scoped>
  /* Estilos de fondo y animación de gradiente */
  .animated-background {
    position: absolute;
    width: 100vw;
    height: 100vh;
    overflow: hidden;
    background: linear-gradient(
      315deg,
      rgba(101, 0, 94, 1) 3%,
      rgba(60, 132, 206, 1) 38%,
      rgba(48, 238, 226, 1) 68%,
      rgba(255, 25, 25, 1) 98%
    );
    animation: gradient 15s ease infinite;
    background-size: 400% 400%;
    background-attachment: fixed;
  }
  
  /* Keyframes para la animación del fondo */
  @keyframes gradient {
    0% {
      background-position: 0% 0%;
    }
    50% {
      background-position: 100% 100%;
    }
    100% {
      background-position: 0% 0%;
    }
  }
  
  /* Estilos de las olas */
  .wave {
    background: rgba(255, 255, 255, 0.25);
    border-radius: 1000% 1000% 0 0;
    position: fixed;
    width: 200%;
    height: 12em;
    animation: wave 10s -3s linear infinite;
    transform: translate3d(0, 0, 0);
    opacity: 0.8;
    bottom: 0;
    left: 0;
    z-index: -1;
  }
  
  /* Variaciones en las ondas */
  .wave:nth-of-type(2) {
    bottom: -1.25em;
    animation: wave 18s linear reverse infinite;
    opacity: 0.8;
  }
  
  .wave:nth-of-type(3) {
    bottom: -2.5em;
    animation: wave 20s -1s reverse infinite;
    opacity: 0.9;
  }
  
  /* Keyframes para la animación de las olas */
  @keyframes wave {
    2% {
      transform: translateX(1%);
    }
    25% {
      transform: translateX(-25%);
    }
    50% {
      transform: translateX(-50%);
    }
    75% {
      transform: translateX(-25%);
    }
    100% {
      transform: translateX(1%);
    }
  }
  </style>