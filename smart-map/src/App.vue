<template>
  <div id="app">
    <MainMap msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
import MainMap from './components/MainMap.vue'

export default {
  name: 'App',
  components: {
    MainMap
  }
}
</script>

<style>
html, body, #app {
  height: 100%;
  margin: 0;
}
</style>