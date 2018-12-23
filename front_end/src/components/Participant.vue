<template>
  <div class="participant">
    <img :src="require(`../assets/${name.toLowerCase()}.png`)" />
    <span class="name">{{name }}</span>
  </div>
</template>

<script>
  export default {
    props: {
      name: String
    }
  }
</script>

<style>
  img {
    margin: 5px 10px;
    height: 30px;
    width: 30px;
  }

  .name {
    width: 80px;
  }
</style>