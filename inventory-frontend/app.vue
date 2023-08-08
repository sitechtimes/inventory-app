<template>
  <div class="app dismiss">
    <div id="search" class="heading">
      <Header />
    </div>
    <div id="navHolder">
      <UserMenu />
    </div>
    <div id="largeItemHolder">
      <div class="replacer" v-if="store.catalog === true">
        <Catalog />
      </div>
      <div class="replacer" v-if="store.monitor === true">
        <Monitor />
      </div>
      <div class="replacer" v-if="store.vendors === true">
        <Vendors />
      </div>
    </div>
    <div v-if="store.editform">
      <NuxtPage />
    </div>
  </div>
</template>

<script>
import { useItemsStore } from "~/store/ItemsStore";
import Header from "./components/header.vue";
import Catalog from "./components/catalog.vue";
import UserMenu from "./components/UserMenu.vue";
import Search from "./components/search.vue";
import Monitor from "./components/monitor.vue";
import Vendors from "./components/vendors.vue";

export default {
  name: "app",
  components: { Search, Catalog, UserMenu, Header, Monitor, Vendors },
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
  transition: all 0.5s linear;
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
  overflow-y: hidden;
  justify-content: center;
  padding-bottom: 8rem;
  height: 100%;
  width: 100%;
  flex: 1 1 0%;
}

.replacer {
  height: 100%;
  width: 100%;
  overflow-y: scroll;
}
</style>
