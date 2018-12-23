<template>
  <div id="app">
    <h1>Python + Vue Secret Santa</h1>
    <SantaHome v-bind:people="people" v-on:generate-santas="getSantas()"/>
  </div>
</template>

<script>
  import SantaHome from './components/SantaHome.vue'

  export default {
    name: 'app',
    data: () => ({
      people: [
        {name: 'Gabe', receiver: null},
        {name: 'Jen', receiver: null},
        {name: 'JordanF', receiver: null},
        {name: 'JordanH', receiver: null},
        {name: 'Micah', receiver: null},
        {name: 'Katie', receiver: null},
        {name: 'Jan', receiver: null},
        {name: 'Chuck', receiver: null},
      ]
    }),
    components: {
      SantaHome
    },
    methods: {
      getSantas: function() {
        this.people = [
          {name: 'Gabe', receiver: 'JordanH'},
          {name: 'Jen', receiver: 'Jan'},
          {name: 'JordanF', receiver: 'Jen'},
          {name: 'JordanH', receiver: 'Micah'},
          {name: 'Micah', receiver: 'Chuck'},
          {name: 'Katie', receiver: 'JordanF'},
          {name: 'Jan', receiver: 'Gabe'},
          {name: 'Chuck', receiver: 'Katie'},
        ]
      }
    }
  }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    color: #2c3e50;
  }
</style>
