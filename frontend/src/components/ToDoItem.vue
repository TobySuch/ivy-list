<template>
  <div v-bind:id="'ToDoItem-' + item.id" class="ToDoItem mt-2 row d-block rounded text-justify container align-items-top" v-bind:class="{ completed: item.completed_at !== null }">
    <div class="row">
      <!-- Hamburger menu to reorder to do items -->
      <div class="col-1">
        <h3><font-awesome-icon icon="bars" fixed-width class="grab_cursor"/></h3>
      </div>

      <!-- Title of to do item -->
      <div class="col">
        <h3 class="title">
          {{ item.title }}
          <font-awesome-icon icon="caret-down" fixed-width v-show="!this.description_visible" @click="showDescription(item);" class="point_cursor"/>
          <font-awesome-icon icon="caret-up" fixed-width v-show="this.description_visible" @click="hideDescription(item);" class="point_cursor"/>
        </h3>
      </div>

      <!-- Buttons at the end of the item -->
      <div class="col-auto align-self-end">
        <h3>
          <font-awesome-icon icon="check" fixed-width class="ml-2 point_cursor" v-if="item.completed_at === null" @click="complete();"/> 
          <font-awesome-icon icon="times" fixed-width class="ml-2 point_cursor" v-if="item.completed_at !== null" @click="uncomplete();"/> 
          <font-awesome-icon icon="pencil-alt" fixed-width class="ml-2 point_cursor"/> 
          <font-awesome-icon icon="trash-alt" fixed-width class="ml-2 point_cursor"/>
        </h3>
      </div>
    </div>

    <!-- To do item description -->
    <div class="row">
      <div class="col-1"></div>
      <div class="col" v-show="this.description_visible">
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
  data: function () {
    return {
      description_visible: false
    }
  },
  methods: {
    showDescription: function() {
      this.description_visible = true;
    },
    hideDescription: function() {
      this.description_visible = false;
    },
    complete: function() {
      this.axios.get("/todo_item/" + this.item.id + "/complete/",
        {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + localStorage.access_token
        }
      }).then(response => {

        this.item.completed_at = response.data.completed_at;
      });
    },
    uncomplete: function() {
      this.axios.get("/todo_item/" + this.item.id + "/uncomplete/",
        {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + localStorage.access_token
        }
      }).then(response => {
        this.item.completed_at = response.data.completed_at;
      });
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

  .grab_cursor {
    cursor: -webkit-grab; cursor: grab;
  }

  .point_cursor {
    cursor: pointer;
  }

  .description {
    margin: 0px;
  }

  h3 {
    margin: 0px;
  }
</style>
