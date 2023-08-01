<template>
  <div class="searchbar compsearchbar">
    <input
      type="text"
      id="searchform"
      v-model="input"
      @keyup="filteredItems(input)"
      placeholder="Search Inventory"
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
      this.store.returnlist.forEach(
        (arr) =>
          (this.newlist = arr.filter((item) =>
            item.name.toLowerCase().includes(i.toLowerCase())
          ))
      );

      console.log(
        this.store.items,
        "items",
        this.newlist,
        "newlist",
        this.store.newlist,
        "storenewlist"
      );
      this.store.$patch({ newlist: this.newlist, search: true, info: false });

      this.store.sort();
      this.store.resizing();
    },
    clearSearch() {
      this.store.$patch({ search: false, info: false });
      this.store.sort();
      this.store.resizing();
      document.getElementById("searchform").value = "";
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
#searchform:focus,
input:focus {
  outline: none;
  background-color: var(--whitebg);
  border: solid 1px rgba(0, 0, 0, 0);
  box-shadow: 0.2rem 0.2rem 1rem var(--darkergray);
}
.searchclear {
  margin-right: 2rem;
  position: absolute;
  right: 4rem;
  opacity: 0;
}
#searchform:hover ~ .searchclear,
.searchclear:hover {
  opacity: 1;
}

@media screen and (max-width: 1500px) {
  .searchclear {
    right: 2rem;
  }
}
@media screen and (max-width: 760px) {
  .searchclear {
    right: 0;
  }
}
</style>
