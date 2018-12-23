<template>
  <div>
    <h3>Participants:</h3>
    <div id="participants">
      <div class="participant" v-for="(person) in people" :key="person.name">
        <Participant v-bind:name="person.name"></Participant>
        <span v-if="person.receiver" class="arrow">➡️</span>
        <Participant v-if="person.receiver" v-bind:name="person.receiver"></Participant>
      </div>
    </div>
    <button v-on:click="$emit('generate-santas')">Generate</button>
  </div>
</template>

<script>
  import Participant from "./Participant"
  export default {
    name: 'SantaHome',
    components: {Participant},
    props: {
      people: Array
    }
  }
</script>

<style>
  h3 {
    margin: 0;
  }

  ul {
    margin: 0;
  }

  #participants {
    display: flex;
    flex-direction: column;
    width: 500px;
  }

  .participant {
    display: flex;
    flex-direction: row;
    align-items: center;
  }

  .arrow {
    margin-right: 20px;
  }

  button {
    padding: 5px 10px;
    font-size: 16px;
    border-radius: 5px;
    border-color: #2c3e50;
    background-color: #2c3e5020;
    margin: 10px;
  }
</style>
