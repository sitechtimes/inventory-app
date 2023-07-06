<template>
  <div>
    wow?
    <div id="itemHolder">
      <Item
        :name="'Hammers Huge Huge hammer'"
        :quantity="2"
        :description="'This is a trial. These hammers are awesome and slay and cool and I love hammers.  '"
      />
    </div>
  </div>
</template>

<style>
@import url("https://fonts.googleapis.com/css2?family=Fira+Sans:wght@300&display=swap");

body {
  background-color: #343e66;
  color: #fbf7e4;
  font-family: "Fira Sans", sans-serif;
}
#itemHolder {
  display: flex;
  height: 100%;
  width: 100%;
  align-items: center;
  justify-content: center;
}
</style>

<script>
import { Item } from "./components/item.vue";

export default {
  name: "app",
  components: { Item },
};
</script>
