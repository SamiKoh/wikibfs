<template>
  <div id="app">
    <FrontPage/>
  </div>
</template>

<script>
import FrontPage from './components/FrontPage.vue';

export default {
  name: 'app',
  components: {
    FrontPage,
  },
};
</script>

<style lang="scss">
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
