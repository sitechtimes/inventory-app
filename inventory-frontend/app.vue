<template>
  <div class="app">
    <div id="search" class="heading">
      <Search />
    </div>
    <div id="navHolder">nav</div>
    <div id="largeItemHolder">
      <Catalog />
    </div>
  </div>
</template>

<style>
.app {
  height: 100%;
  width: 100%;
  display: grid;
  grid-template-columns: 7rem 1fr;
  grid-template-rows: 5.5rem 1fr;
  position: absolute;
  top: 0;
  left: 0;
  overflow: hidden;
}
#search {
  grid-column: 1 / 3;
  width: 100%;
  height: 100%;
  border-bottom: var(--border);
}
#navHolder {
  grid-row: 2 / 3;
  grid-column: 1 / 2;
  border-right: var(--border);
}
#largeItemHolder {
  grid-row: 2/3;
  grid-column: 2/3;
  display: flex;
  flex-direction: row;
  overflow-y: hidden;
  background-color: var(--lightgray);
}
</style>

<script>
import { useItemsStore } from "~/store/ItemsStore";
import Search from "./components/search.vue";
import Catalog from "./components/catalog.vue";

export default {
  name: "app",
  components: { Search, Catalog },
  data() {
    return {
      store: useItemsStore(),
    };
  },
  methods: {},
  mounted() {},
};
</script>
