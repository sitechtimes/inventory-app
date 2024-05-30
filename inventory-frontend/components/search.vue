<template>
  <div class="searchbar compsearchbar">
    <input
      type="text"
      id="searchform"
      v-model="input"
      @keyup="filteredItems(input)"
      placeholder="Search Inventory"
    />
    <span class="material-symbols-outlined searchicon"> search </span>
    <button class="exitbtn heading searchclear" @click="store.clearSearch">
      <span class="material-symbols-outlined"> close </span>
    </button>
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
      empties: 0,
    };
  },
  methods: {
    filteredItems(i) {
      this.newlist = [];
      this.store.returnlist.forEach((arr) => {
        let itemsCategory = Array.from(
          arr.itemsCategory.filter(
            (item) =>
              item.name.toLowerCase().includes(i.toLowerCase()) ||
              item.item_id.toLowerCase().includes(i.toLowerCase())
          )
        );
        let categories = [arr.category_name, itemsCategory];

        this.newlist.push(categories);
      });

      this.store.$patch({
        items: this.newlist,
        search: true,
        info: false,
        editform: false,
      });
      this.empties = 0;
      this.store.items.forEach((item) => {
        if (item[1].length < 1) {
          this.empties++;

        }
      });
      if (this.empties >= this.store.items.length) {
        this.store.$patch({ empty: true });
      } else {
        this.store.$patch({ empty: false });
      }
    },
  },
  mounted() {},
};
</script>

<style>
.searchicon {
  position: absolute;
  margin-left: 1rem;
}
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
  padding-left: 4.5rem;
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
    right: -1.5rem;
  }
}
</style>
