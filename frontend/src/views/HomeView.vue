<template>
  <div>
    <h1>Ivy List</h1>
    <h2 class="text-muted">The simple to do app to increase your productivity</h2>
    <div class=row>
      <div class="col-sm">
        <button class="btn btn-block btn-primary" @click="$parent.redirectToRegister">Get Started</button>
      </div>
      <div class="col-sm">
        <button class="btn btn-block btn-primary" @click="$parent.redirectToToDos">Already have an account?</button>
      </div>
    </div>
    <div id="description" class="text-left">
      <h2 class="heading-break">How does it work?</h2>
      <p>Ivy list encourages you to use a technique called The Ivy Lee Method which was invented by Ivy Lee in 1918.</p>

      <h4 class="heading-break">Here are the steps:</h4>
      <ol>
        <li>At the end of your day, write down 6 things you would like to achieve the next day. You may not add any more than 6 items.</li>
        <li>Prioritise those 6 items from the most important and must be done first, to the least important and can be left until last.</li>
        <li>At the start of the next day, start working on the first item on your list. Do not work on anything else until the first item is finished.</li>
        <li>Once that item is done, check it off the list and move onto the next item.</li>
        <li>If you reach the end of the day and there are still items on your list, move them to the top of tomorrows list, and repeat the process.</li>
      </ol>
      <p>You can read more about the Ivy Lee method <a target="_blank" href="https://www.businessinsider.com/ivy-lee-method-productivity-2018-9?r=US&IR=T">here!</a></p>
    </div>
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
  .btn {
    margin-top: 10px;
  }
  .heading-break {
    margin-top: 30px;
  }
</style>
