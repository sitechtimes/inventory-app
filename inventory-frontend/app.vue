<template>
  <div class="app">
    <div id="search">search</div>
    <div id="navHolder">nav</div>

    <div id="itemHolder">
      <div id="itemHeader">items</div>
      <Item
        :name="'Hammers Huge Huge hammer'"
        :quantity="2"
        :description="'This is a trial. These hammers are awesome and slay and cool and I love hammers.  '"
        :available="true"
        :updated="'2023-7-10'"
      />
    </div>
  </div>
</template>

<style>
@import url("https://fonts.googleapis.com/css2?family=Fira+Sans:wght@300&display=swap");

body {
  background-color: #ffffff;
  color: black;
  font-family: "Fira Sans", sans-serif;
}
.app {
  height: 100vh;
  width: 100vw;
  display: grid;
  grid-template-columns: 7rem 1fr;
  grid-template-rows: 3.5rem 1fr;
}
#search {
  grid-column: 1 / 3;
  width: 100%;
  height: 100%;
  border: 1px solid red;
}
#navHolder {
  grid-row: 2 / 3;
  grid-column: 1 / 2;
  border: 1px solid red;
}
#itemHolder {
  grid-column: 2 / 3;
  grid-row: 2 / 3;
  display: flex;
  height: 100%;
  width: 100%;
  align-items: center;
  justify-content: center;
  border: 1px solid red;
}
</style>

<script>
import Item from "./components/item.vue";

export default {
  name: "app",
  components: { Item },
};
</script>
