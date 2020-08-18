<template>
  <div v-bind:id="'ToDoItem-' + item.id" class="ToDoItem mt-2 row d-block rounded text-justify container align-items-top" v-bind:class="{ completed: item.completed_at !== null }">
    <div class="row">
      <!-- Hamburger menu to reorder to do items -->
      <div class="col-1">
        <h3><font-awesome-icon icon="bars" /></h3>
      </div>

      <!-- Title of to do item -->
      <div class="col">
        <h3 class="title">
          {{ item.title }}
          <font-awesome-icon icon="caret-down" v-show="!item.description_visible" v-on:click="showDescription(item);"/>
          <font-awesome-icon icon="caret-up" v-show="item.description_visible" v-on:click="hideDescription(item);"/>
        </h3>
      </div>

      <!-- Buttons at the end of the item -->
      <div class="col-auto align-self-end">
        <h3>
          <font-awesome-icon icon="check" class="ml-2"/> 
          <font-awesome-icon icon="pencil-alt" class="ml-2"/> 
          <font-awesome-icon icon="trash-alt" class="ml-2"/>
        </h3>
      </div>

    </div>
    <!-- To do item description -->
    <div class="row">
      <div class="col-1"></div>
      <div class="col" v-show="item.description_visible">
        <p class="description">{{ item.description }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ToDoItem',
  props: {
    item: Object
  },
  methods: {
    showDescription: function (item) {
      item.description_visible = true;
    },
    hideDescription: function (item) {
      item.description_visible = false;
    }

  }
}
</script>

<style scoped>
  .ToDoItem {
    padding:10px;
    background-color: lightblue;
  }

  .completed{
    background-color: lightgreen
  }

  .description {
    margin: 0px;
  }

  h3 {
    margin: 0px;
  }
</style>
