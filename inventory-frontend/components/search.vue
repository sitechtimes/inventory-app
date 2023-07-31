<template>
  <div class="searchbar compsearchbar">
    <input
      type="text"
      id="searchform"
      v-model="input"
      @keyup.enter="filteredItems(input)"
      placeholder="Search Inventory..."
    />
    <button class="exitbtn heading searchclear" @click="clearSearch">X</button>
  </div>
</template>

<script>
import { useItemsStore } from "~/store/ItemsStore";

export default {
  name: "Search",
  data() {
    return {
      store: useItemsStore(),

      newlist: [],
    };
  },
  methods: {
    filteredItems(i) {
      this.newlist = this.store.returnlist.filter((item) =>
        item.name.toLowerCase().includes(i.toLowerCase())
      );

      console.log(
        this.store.items,
        "items",
        this.newlist,
        "newlist",
        this.store.newlist,
        "storenewlist"
      );
      this.store.$patch({ newlist: this.newlist, search: true });

      this.store.sort();
    },
    clearSearch() {
      this.store.$patch({ search: false });
      this.store.sort();
    },
  },
  mounted() {},
};
</script>

<style>
.compsearchbar {
  min-width: 100%;
  position: relative;
}
#searchform {
  width: 95%;
  height: 80%;
  background-color: var(--halflightgray);
  border-radius: 1rem;
  border: none;
  font-size: 1.5rem;
  padding-left: 1.5rem;
}
.searchclear {
  background-color: var(--halflightgray);
  position: absolute;
  right: 2rem;
  opacity: 0;
}
#searchform:hover ~ .searchclear,
.searchclear:hover {
  opacity: 1;
}
</style>
