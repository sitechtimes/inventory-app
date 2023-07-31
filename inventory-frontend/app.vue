<template>
  <div class="app">
    <div id="search" class="heading">
      <Search />
    </div>
    <div id="navHolder">
      <UserMenu />
    </div>
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
import UserMenu from "./components/UserMenu.vue";

export default {
  name: "app",
  components: { Search, Catalog, UserMenu },
  data() {
    return {
      store: useItemsStore(),
    };
  },
  methods: {},
  mounted() {},
};
</script>

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
#mainItems {
  display: flex;

  flex-direction: column;
}
#itemHeader {
  min-height: 5.5rem;
  border-bottom: var(--border);
  background-color: var(--whitebg);
  position: sticky;
  top: 0;
  z-index: 500;
}
#itemHolderAll {
  grid-column: 2 / 3;
  grid-row: 3 / 4;
  overflow-y: scroll;
  justify-content: center;

  height: 100%;
  width: 100%;
  flex: 1 1 0%;
}

.infoDesc {
  height: 100%;
  width: 70%;
  min-width: 50rem;
  position: sticky;
  top: 0;
  overflow: hidden;
  flex: 1 1 0%;
  border-left: var(--border);
}
@media screen and (min-width: 1600px) {
  .infoDesc {
    min-width: 80rem;
  }
}
@media screen and (max-width: 760px) {
  .infoDesc {
    width: auto;
    align-self: flex-start;
    justify-self: flex-start;
    position: fixed;
    margin-top: 5.5rem;
    margin-left: 7rem;
    left: 0;
    right: 0;
    border: none;
    z-index: 2000;
  }
}
</style>
