<template>
  <div>
    <h2>Home</h2>
    <button class="btn btn-primary" @click="redirectToToDos">View Your To Do's</button>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  methods: {
    redirectToToDos: function () {
      this.$router.push('/todo');
    }
  }
}
</script>

<style scoped>
</style>
