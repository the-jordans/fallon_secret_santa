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
        {giver: 'Jan Fallon', receiver: null},
        {giver: 'Chuck Fallon', receiver: null},
        {giver: 'Jordan Fallon', receiver: null},
        {giver: 'Gabe Fallon', receiver: null},
        {giver: 'Micah Fallon', receiver: null},
        {giver: 'Jordan Hagan', receiver: null},
        {giver: 'Jen Fallon', receiver: null},
        {giver: 'Katie Fallon', receiver: null},
      ]
    }),
    components: {
      SantaHome
    },
    methods: {
      getSantas: function() {
        fetch('http://localhost:5000/gift_data')
          .then(response => response.json())
          .then(data => this.people = data)
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
