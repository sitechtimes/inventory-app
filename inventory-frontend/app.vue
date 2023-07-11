<template>
  <div class="app">
    <div id="search">search</div>
    <div id="navHolder">nav</div>
    <div id="itemHeader" class="heading">items</div>
    <div id="itemHolder">
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
body {
  background-color: var(--gray);
  color: black;
  font-family: "Fira Sans", sans-serif;
}
.app {
  height: 100%;
  width: 100%;
  display: grid;
  grid-template-columns: 7rem 1fr;
  grid-template-rows: 3.5rem 3.5rem 1fr;
  position: absolute;
  top: 0;
  left: 0;
  overflow: hidden;
}
#search {
  grid-column: 1 / 3;
  width: 100%;
  height: 100%;
  border-bottom: solid 1px rgb(170, 170, 170);
}
#navHolder {
  grid-row: 2 / 4;
  grid-column: 1 / 2;
  border-right: solid 1px rgb(170, 170, 170);
}
#itemHeader {
  grid-row: 2/3;
  grid-column: 2/3;
  border-bottom: solid 1px var(--darkgray);
}
#itemHolder {
  grid-column: 2 / 3;
  grid-row: 3 / 4;
  display: flex;
  height: 100%;
  width: 100%;
  background-color: rgb(245, 245, 245);
  justify-content: center;
}
</style>

<script>
import Item from "./components/item.vue";

export default {
  name: "app",
  components: { Item },
};
</script>
